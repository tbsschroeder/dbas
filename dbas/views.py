import transaction
import datetime
import requests

from validate_email import validate_email
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, notfound_view_config, forbidden_view_config
from pyramid.security import remember, forget
from pyramid.session import check_csrf_token
from pyramid.renderers import get_renderer
from pyramid.threadlocal import get_current_registry
from pyshorteners.shorteners import Shortener

from .database import DBDiscussionSession
from .database.discussion_model import User, Group, Issue
from .database_helper import DatabaseHelper
from .user_management import PasswordGenerator, PasswordHandler, UserHandler
from .query_helper import QueryHelper
from .email import EmailHelper
from .dictionary_helper import DictionaryHelper
from .logger import logger
from .strings import Translator
from .security import escape_string

name = 'D-BAS'
version = '0.4.1'
header = name + ' ' + version
issue_fallback = 1

class Dbas(object):
	def __init__(self, request):
		"""
		Object initialization
		:param request: init http request
		:return:
		"""
		self.request = request
		self.issue_fallback = DBDiscussionSession.query(Issue).first().uid


	def base_layout(self):
		renderer = get_renderer('templates/basetemplate.pt')
		layout = renderer.implementation().macros['layout']
		return layout

	# main page
	@view_config(route_name='main_page', renderer='templates/index.pt', permission='everybody')
	@forbidden_view_config(renderer='templates/index.pt')
	def main_page(self):
		"""
		View configuration for the main page
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_page', 'def', 'main page')
		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Main',
			'project': header,
			'logged_in': self.request.authenticated_userid
		}

	# contact page
	@view_config(route_name='main_contact', renderer='templates/contact.pt', permission='everybody')
	def main_contact(self):
		"""
		View configuration for the contact view.
		:return: dictionary with title and project username as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_contact', 'def', 'contact page')

		token = self.request.session.new_csrf_token()
		logger('main_contact', 'new token', str(token))

		contact_error = False
		send_message = False
		message = ''
		username = ''
		email = ''
		phone = ''
		content = ''
		spam = ''

		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		if 'form.contact.submitted' in self.request.params:
			logger('main_contact', 'form.contact.submitted', 'requesting params')
			username = self.request.params['name']
			email = self.request.params['mail']
			phone = self.request.params['phone']
			content = self.request.params['content']
			spam = self.request.params['spam']
			request_token = self.request.params['csrf_token']

			t = Translator(lang)

			logger('main_contact', 'form.contact.submitted', 'validating email')
			is_mail_valid = validate_email(email, check_mx=True)

			## sanity checks
			# check for empty username
			if not username:
				logger('main_contact', 'form.contact.submitted', 'username empty')
				contact_error = True
				message = t.get('emptyName')

			# check for non valid mail
			elif not is_mail_valid:
				logger('main_contact', 'form.contact.submitted', 'mail is not valid')
				contact_error = True
				message = t.get('emptyEmail')

			# check for empty content
			elif not content:
				logger('main_contact', 'form.contact.submitted', 'content is empty')
				contact_error = True
				message = t.get('emtpyContent')

			# check for empty username
			elif (not spam) or (not spam.isdigit()) or (not int(spam) == 4):
				logger('main_contact', 'form.contact.submitted', 'empty or wrong anti-spam answer')
				contact_error = True
				message = t.get('maliciousAntiSpam')

			# is the token valid?
			elif request_token != token :
				logger('main_contact', 'form.contact.submitted', 'token is not valid')
				logger('main_contact', 'form.contact.submitted', 'request_token: ' + str(request_token))
				logger('main_contact', 'form.contact.submitted', 'token: ' + str(token))
				message = t.get('nonValidCSRF')
				contact_error = True

			else:
				subject = 'contactDBAS''Contact D-BAS'
				body = t.get('name') + ': ' + username + '\n'\
				       + t.get('mail') + ': ' + email + '\n'\
				       + t.get('phone') + ': ' + phone + '\n'\
				       + t.get('message') + ':\n' + content
				send_message, contact_error, message = EmailHelper().send_mail(self.request, subject, body, email, lang)

		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Contact',
			'project': header,
			'logged_in': self.request.authenticated_userid,
			'was_message_send': send_message,
			'contact_error': contact_error,
			'message': message,
			'name': username,
			'mail': email,
			'phone': phone,
			'content': content,
			'spam': spam,
			'csrf_token': token
		}

	# content page, after login
	@view_config(route_name='main_discussion', renderer='templates/content.pt', permission='everybody')
	@view_config(route_name='main_discussion_start', renderer='templates/content.pt', permission='everybody')
	@view_config(route_name='main_discussion_issue', renderer='templates/content.pt', permission='everybody')
	def main_discussion(self):
		"""
		View configuration for the content view. Only logged in user can reach this page.
		:return: dictionary with title and project name as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_discussion', 'def', 'main')

		parameters = self.request.matchdict['parameters'] if 'parameters' in self.request.matchdict else '-'

		logger('main_discussion', 'def', 'is issue in params ' + str('issue' in self.request.params))
		logger('main_discussion', 'def', 'is issue in session ' + str('issue' in self.request.session))
		logger('main_discussion', 'def', 'is issue in matchdict ' + str('issue' in self.request.matchdict))

		# first matchdict, then params, then session, afterwards fallback
		if 'issue' in self.request.matchdict:
			issue = self.request.matchdict['issue']
			where = 'self.request.matchdict[issue]'
		elif 'issue' in self.request.params:
			issue = self.request.params['issue']
			where = 'self.request.params[issue]'
		elif 'issue' in self.request.session:
			issue = self.request.session['issue']
			where = 'self.request.session[issue]'
		else:
			where = 'fallback'
			issue = issue_fallback

		if issue == 'undefined':
			where = 'fallback because undefined'
			issue = issue_fallback

		logger('main_discussion', 'def', 'self.request.matchdict[parameters]: ' + parameters)
		logger('main_discussion', 'def', where + ': ' + str(issue))

		# save issue in session
		self.request.session['issue'] = issue
		logger('main_discussion', 'def', 'set session[issue] to ' + str(issue))

		token = self.request.session.get_csrf_token()
		logger('main_discussion', 'new token', str(token))

		# checks whether the current user is admin
		is_admin = UserHandler().is_user_admin(self.request.authenticated_userid)

		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		logger('main_discussion', 'def', 'return')
		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Content',
			'project': header,
			'logged_in': self.request.authenticated_userid,
			'is_admin': is_admin,
			'parameters': parameters,
			'issue': issue
		}

	# settings page, when logged in
	@view_config(route_name='main_settings', renderer='templates/settings.pt', permission='use')
	def main_settings(self):
		"""
		View configuration for the content view. Only logged in user can reach this page.
		:return: dictionary with title and project name as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_settings', 'def', 'main')

		token = self.request.session.get_csrf_token()
		logger('main_settings', 'new token', str(token))

		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']
		logger('main_settings', 'language', lang)

		old_pw = ''
		new_pw = ''
		confirm_pw = ''
		message = ''
		error = False
		success = False

		db_user = DBDiscussionSession.query(User).filter_by(nickname=str(self.request.authenticated_userid)).join(Group).first()
		logger('main_settings', 'db_user', db_user.nickname)
		logger('main_settings', 'db_user.groups', str(db_user.groups.uid))
		logger('main_settings', 'db_user.groups', str(db_user.groups.name))
		if db_user and 'form.passwordchange.submitted' in self.request.params:
			logger('main_settings', 'form.changepassword.submitted', 'requesting params')
			old_pw = self.request.params['passwordold']
			new_pw = self.request.params['password']
			confirm_pw = self.request.params['passwordconfirm']

			message, error, success = DatabaseHelper().change_password(transaction, db_user, old_pw, new_pw, confirm_pw, lang)



		logger('main_settings', 'return change_error', str(error))
		logger('main_settings', 'return change_success', str(success))
		logger('main_settings', 'return message', str(message))
		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Settings',
			'project': header,
			'logged_in': self.request.authenticated_userid,
			'passwordold': '' if success else old_pw,
			'password': '' if success else new_pw,
			'passwordconfirm': '' if success else confirm_pw,
			'change_error': error,
			'change_success': success,
			'message': message,
			'db_firstname': db_user.firstname if db_user else 'unknown',
			'db_surname': db_user.surname if db_user else 'unknown',
			'db_nickname': db_user.nickname if db_user else 'unknown',
			'db_mail': db_user.email if db_user else 'unknown',
			'db_group': db_user.groups.name if db_user and db_user.groups else 'unknown',
			'csrf_token': token
		}

	# news page for everybody
	@view_config(route_name='main_news', renderer='templates/news.pt', permission='everybody')
	def main_news(self):
		"""
		View configuration for the news.
		:return: dictionary with title and project name as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_news', 'def', 'main')
		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		is_author = UserHandler().is_user_author(self.request.authenticated_userid)

		# get date
		now = datetime.datetime.now()
		yyyy = str(now.year)
		mm = str(now.month) if now.month > 9 else '0' + str(now.month)
		dd = str(now.day) if now.day > 9 else '0' + str(now.day)
		date = dd + "." + mm + "." + yyyy

		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'News',
			'project': header,
			'logged_in': self.request.authenticated_userid,
			'date':date,
			'is_author': is_author
		}

	# imprint
	@view_config(route_name='main_imprint', renderer='templates/imprint.pt', permission='everybody')
	def main_imprint(self):
		"""
		View configuration for the imprint.
		:return: dictionary with title and project name as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('main_imprint', 'def', 'main')
		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Imprint',
			'project': header,
			'logged_in': self.request.authenticated_userid
		}

	# 404 page
	@notfound_view_config(renderer='templates/404.pt')
	def notfound(self):
		"""
		View configuration for the 404 page.
		:return: dictionary with title and project name as well as a value, weather the user is logged in
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('notfound', 'def', 'main in ' + str(self.request.method) + '-request')

		logger('notfound', 'def', 'path: ' + self.request.path)
		logger('notfound', 'def', 'view name: ' + self.request.view_name)

		# TODO: Dirty bugfix
		# if 'ajax_get_start_statements' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_get_start_statements')
		# 	return self.get_start_statements()
		# elif 'ajax_get_premises_for_statement' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_get_premises_for_statement')
		# 	return self.get_premises_for_statement()
		# elif 'ajax_reply_for_premisegroup' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_reply_for_premisegroup')
		# 	return self.reply_for_premisegroup()
		# elif 'ajax_reply_for_response_of_confrontation' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_reply_for_response_of_confrontation')
		# 	return self.reply_for_response_of_confrontation()
		# elif 'ajax_reply_for_argument' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_reply_for_argument')
		# 	return self.reply_for_argument()
		#
		# elif 'ajax_set_new_start_statement' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: set_new_start_statement')
		# 	return self.set_new_start_statement()
		# elif 'ajax_set_new_start_premise' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_set_new_start_premise')
		# 	return self.set_new_start_premise()
		# elif 'ajax_set_new_premises_for_x' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_set_new_premises_for_x')
		# 	return self.set_new_premises_for_x()
		# elif 'ajax_set_correcture_of_statement' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_set_correcture_of_statement')
		# 	return self.set_correcture_of_statement()
		# elif 'ajax_get_logfile_for_statement' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_get_logfile_for_statement')
		# 	return self.get_logfile_for_statement()
		# elif 'ajax_set_correcture_of_statement' in self.request.path:
		# 	logger('notfound', 'def', 'redirect to: ajax_set_correcture_of_statement')
		# 	return self.set_correcture_of_statement()

		logger('notfound', 'def', 'params:')
		for param in self.request.params:
			logger('notfound', 'def', '    ' + param + ' -> ' + self.request.params[param])

		self.request.response.status = 404
		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		return {
			'layout': self.base_layout(),
			'language': str(lang),
			'title': 'Error',
			'project': header,
			'page_notfound_viewname': self.request.view_name,
			'logged_in': self.request.authenticated_userid
		}

	# ajax - getting every user, and returns dicts with name <-> group
	@view_config(route_name='ajax_all_users', renderer='json', check_csrf=False)
	def get_all_users(self):
		"""
		Returns all users as dictionary with name <-> group
		:return: list of all users
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('get_all_users', 'def', 'main')

		return_dict = DatabaseHelper().get_all_users(self.request.authenticated_userid)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - return all start statements in the database
	@view_config(route_name='ajax_get_start_statements', renderer='json', check_csrf=False)
	def get_start_statements(self):
		"""
		Returns all positions as dictionary with uid <-> value
		:return: list of all positions
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('get_start_statements', 'def', 'main')

		# update timestamp
		logger('get_start_statements', 'def',  'update login timestamp')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		return_dict = dict()
		try:
			logger('get_start_statements', 'def', 'read params')
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback

			if issue == 'undefined':
				logger('get_start_statements', 'def', 'issue is undefined -> fallback')
				issue = issue_fallback
				return_dict['reset_url'] = 'true'
				return_dict['reset_issue'] = issue
			else:
				logger('get_start_statements', 'def', 'issue found')

			return_dict.update(DatabaseHelper().get_start_statements(issue))
		except KeyError as e:
			logger('get_start_statements', 'error', repr(e))

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - getting text for a statement
	@view_config(route_name='ajax_get_text_for_statement', renderer='json', check_csrf=False)
	def get_text_for_statement(self):
		"""
		Returns text of a statement
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('get_text_for_statement', 'def', 'main')

		return_dict = {}
		try:
			logger('get_premises_for_statement', 'def', 'read params: ' + str(self.request.params))
			uids = self.request.params['uid'].split('=')
			uid = uids[1]
			logger('get_text_for_statement', 'def', 'issue in params ' + str('issue' in self.request.params))
			logger('get_text_for_statement', 'def', 'issue in session ' + str('issue' in self.request.session))
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			logger('get_text_for_statement', 'def', 'uid: ' + uid + ', issue ' + str(issue))
			return_dict = DatabaseHelper().get_text_for_statement(transaction, uid, self.request.authenticated_userid, issue)
			return_dict['status'] = '1'
		except KeyError as e:
			logger('get_text_for_statement', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - getting text for a statement
	@view_config(route_name='ajax_get_premise_for_statement', renderer='json', check_csrf=False)
	def get_premise_for_statement(self):
		"""
		Returns random premisses for a statement
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('ajax_get_premise_for_statement', 'def', 'main')

		return_dict = {}
		try:
			logger('ajax_get_premise_for_statement', 'def', 'read params: ' + str(self.request.params))
			uids = self.request.params['uid'].split('=')
			uid = uids[1]
			logger('ajax_get_premise_for_statement', 'def', 'issue in params ' + str('issue' in self.request.params))
			logger('ajax_get_premise_for_statement', 'def', 'issue in session ' + str('issue' in self.request.session))
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			logger('ajax_get_premise_for_statement', 'def', 'uid: ' + uid + ', issue ' + str(issue))

			return_dict = DatabaseHelper().get_premise_for_statement(transaction, uid, self.request.authenticated_userid,
			                                                           self.request.session.id, issue)

			return_dict['status'] = '1'
		except KeyError as e:
			logger('ajax_get_premise_for_statement', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - getting all premisses for a statement
	@view_config(route_name='ajax_get_premises_for_statement', renderer='json', check_csrf=False)
	def get_premises_for_statement(self):
		"""
		Returns all premisses for a statement
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('get_premises_for_statement', 'def', 'main')

		return_dict = {}
		try:
			logger('get_premises_for_statement', 'def', 'read params: ' + str(self.request.params))
			uid = self.request.params['uid'].split('=')[1]
			supportive = True if self.request.params['supportive'].split('=')[1].lower() == 'true' else False

			logger('get_premises_for_statement', 'def', 'issue in params ' + str('issue' in self.request.params))
			logger('get_premises_for_statement', 'def', 'issue in session ' + str('issue' in self.request.session))
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue

			logger('get_premises_for_statement', 'def', 'uid: ' + uid + ', supportive ' + str(supportive) + ', issue ' + str(issue))

			return_dict = DatabaseHelper().get_premises_for_statement(transaction, uid, supportive, self.request.authenticated_userid,
			                                                           self.request.session.id, issue)
			return_dict['status'] = '1'
		except KeyError as e:
			logger('get_premises_for_statement', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - get reply for a premise group
	@view_config(route_name='ajax_reply_for_premisegroup', renderer='json', check_csrf=False)
	def reply_for_premisegroup(self):
		"""
		Get reply for a premise
		:return: dictionary with every arguments
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('reply_for_premisegroup', 'def', 'main')

		return_dict = {}
		try:
			pgroup = self.request.params['pgroup'].split('=')[1]
			conclusion = self.request.params['conclusion'].split('=')[1]
			supportive = True if self.request.params['supportive'].split('=')[1].lower() == 'true' else False
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			logger('reply_for_argument', 'def', 'issue ' + str(issue))
			logger('reply_for_argument', 'def', 'pgroup ' + str(pgroup))
			logger('reply_for_argument', 'def', 'conclusion ' + str(conclusion))
			# track will be saved in the method
			return_dict, status = DatabaseHelper().get_attack_or_support_for_premisegroup(transaction, self.request.authenticated_userid, pgroup,
			                                                                    conclusion, self.request.session.id, supportive, issue)
			return_dict['supportive'] = str(supportive)
			return_dict['status'] = str(status)
		except KeyError as e:
			logger('reply_for_premisegroup', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - get reply for an argument
	@view_config(route_name='ajax_reply_for_argument', renderer='json', check_csrf=False)
	def reply_for_argument(self):
		"""
		Get reply for ana rgument
		:return: dictionary with every arguments
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('reply_for_argument', 'def', 'main')

		return_dict = {}
		try:
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			id_text = self.request.params['id_text'].split('=')[1]
			pgroup_id = self.request.params['pgroup'].split('=')[1]
			logger('reply_for_argument', 'def', 'issue ' + str(issue))
			logger('reply_for_argument', 'def', 'id_text ' + str(id_text))
			logger('reply_for_argument', 'def', 'pgroup_id ' + str(pgroup_id))
			# track will be saved in the method
			return_dict, status = DatabaseHelper().get_attack_for_argument(transaction, self.request.authenticated_userid, id_text,
			                                                               pgroup_id, self.request.session.id, issue)
			return_dict['status'] = str(status)
		except KeyError as e:
			logger('reply_for_argument', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - get reply for a confrontation
	@view_config(route_name='ajax_reply_for_response_of_confrontation', renderer='json', check_csrf=False)
	def reply_for_response_of_confrontation(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('reply_for_response_of_confrontation', 'def', 'main')

		return_dict = {}
		try:
			uid_text = self.request.params['id'].split('=')[1]
			relation = self.request.params['relation'].split('=')[1]
			confrontation = uid_text.split('_')[2]
			exception_rebut = True if uid_text.split('_')[1] == 'attacking' else False
			issue = self.request.params['issue'].split('=')[1] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue

			# track will be saved in get_reply_confrontation_response
			logger('reply_for_response_of_confrontation', 'def', 'id ' + uid_text
			       + ', last relation ' + relation
			       + ', confrontation ' +  confrontation
			       + ', issue ' + str(issue)
			       + ', exception_rebut ' + str(exception_rebut))
			return_dict, status = DatabaseHelper().get_reply_confrontations_response(transaction, uid_text, self.request.authenticated_userid,
			                                                                         self.request.session.id, exception_rebut, issue)
			return_dict['status'] = status
			return_dict['last_relation'] = relation
			return_dict['confrontation_uid'] = confrontation

			# special case, when we are in the attack-branch
			if exception_rebut:
				logger('reply_for_response_of_confrontation', 'def', 'getting text for the second bootstrap way -> attack')
				text, uids = QueryHelper().get_text_for_arguments_premisesGroup_uid(confrontation, issue)
			else:
				logger('reply_for_response_of_confrontation', 'def', 'getting text for the first bootstrap way -> support')
				text, uids = QueryHelper().get_text_for_premisesGroup_uid(confrontation, issue)
			logger('reply_for_response_of_confrontation', 'def', 'adding confrontation_text: ' + text)
			return_dict['confrontation_text'] = text
		except KeyError as e:
			logger('reply_for_response_of_confrontation', 'error', repr(e))
			return_dict['status'] = '-1'

		return_dict['logged_in'] = self.request.authenticated_userid
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - getting complete track of the user
	@view_config(route_name='ajax_get_user_track', renderer='json', check_csrf=True)
	def get_user_track(self):
		"""
		Request the complete user track
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('get_user_track', 'def', 'main')

		nickname = 'unknown'
		try:
			logger('get_user_track', 'def', 'read params')
			nickname = str(self.request.authenticated_userid)
			logger('get_user_track', 'def', 'nickname ' + nickname)
		except KeyError as e:
			logger('get_user_track', 'error', repr(e))

		logger('manage_user_track', 'def', 'get track data')
		return_dict = QueryHelper().get_track_of_user(nickname)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - deleting complete track of the user
	@view_config(route_name='ajax_delete_user_track', renderer='json', check_csrf=True)
	def delete_user_track(self):
		"""
		Request the complete user track
		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('delete_user_track', 'def', 'main')

		nickname = 'unknown'
		try:
			logger('delete_user_track', 'def', 'read params')
			nickname = str(self.request.authenticated_userid)
			logger('delete_user_track', 'def', 'nickname ' + nickname)
		except KeyError as e:
			logger('delete_user_track', 'error', repr(e))

		logger('delete_user_track', 'def', 'remove track data')
		QueryHelper().del_track_of_user(transaction, nickname)
		return_dict = {}
		return_dict['removed_data'] = 'true' # necessary
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - send new start statement
	@view_config(route_name='ajax_set_new_start_statement', renderer='json', check_csrf=True)
	def set_new_start_statement(self):
		"""
		Inserts a new statement into the database
		:return: a status code, if everything was successfull
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('set_new_start_statement', 'def', 'main')

		return_dict = {}
		try:
			statement = self.request.params['statement']
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			logger('set_new_start_statement', 'def', 'request data: statement ' + str(statement))
			new_statement, is_duplicate = DatabaseHelper().set_statement(transaction, statement, self.request.authenticated_userid, True, issue)
			if not new_statement:
				return_dict['status'] = '0'
			else:
				return_dict['status'] = '0' if is_duplicate else '1'
				return_dict['statement'] = DictionaryHelper().save_statement_row_in_dictionary(new_statement, issue)
		except KeyError as e:
			logger('set_new_start_statement', 'error', repr(e))
			return_dict['status'] = '-1'

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - send new start premise
	@view_config(route_name='ajax_set_new_start_premise', renderer='json', check_csrf=True)
	def set_new_start_premise(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		user_id = self.request.authenticated_userid
		UserHandler().update_last_action(transaction, user_id)

		logger('set_new_start_premise', 'def', 'main')

		return_dict = dict()
		try:
			logger('set_new_start_premise', 'def', 'getting params')
			text = escape_string(self.request.params['text'])
			conclusion_id = self.request.params['conclusion_id']
			support = True if self.request.params['support'].lower() == 'true' else False
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue
			logger('set_new_start_premise', 'def', 'conclusion_id: ' + str(conclusion_id) + ', text: ' + text + ', supportive: ' +
			       str(support) + ', issue: ' + str(issue))

			tmp_dict, is_duplicate = DatabaseHelper().set_premises_for_conclusion(transaction, user_id, text, conclusion_id, support, issue)

			return_dict['pro_0'] = tmp_dict
			if is_duplicate:
				return_dict['premisegroup_uid'] = tmp_dict['premisegroup_uid']
			return_dict['status'] = '0' if is_duplicate else '1'
		except KeyError as e:
			logger('set_new_start_premise', 'error', repr(e))
			return_dict['status'] = '-1'

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - send new premises
	@view_config(route_name='ajax_set_new_premises_for_x', renderer='json', check_csrf=True)
	def set_new_premises_for_x(self):
		"""

		:return:
		"""
		user_id = self.request.authenticated_userid
		UserHandler().update_last_action(transaction, user_id)
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')

		logger('set_new_premises_for_x', 'def', 'main')

		return_dict = dict()
		try:
			logger('set_new_premises_for_x', 'def', 'getting params')
			pro_dict = dict()
			con_dict = dict()

			related_argument  = self.request.params['related_argument'] if 'related_argument' in self.request.params else -1
			premisegroup_id   = self.request.params['premisegroup_id'] if 'premisegroup_id' in self.request.params else -1
			current_attack    = self.request.params['current_attack'] if 'current_attack' in self.request.params else -1
			last_attack       = self.request.params['last_attack'] if 'last_attack' in self.request.params else -1
			confrontation_uid = self.request.params['confrontation_uid'] if 'confrontation_uid' in self.request.params else -1
			premisegroup_con  = self.request.params['premisegroup_con'] if 'premisegroup_con' in self.request.params else '0'
			premisegroup_pro  = self.request.params['premisegroup_pro'] if 'premisegroup_pro' in self.request.params else '0'
			exception_rebut   = self.request.params['exceptionForRebut'] if 'exceptionForRebut' in self.request.params else '0'
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			issue = issue_fallback if issue == 'undefined' else issue

			premisegroup_con = True if premisegroup_con.lower() == 'true' else False
			premisegroup_pro = True if premisegroup_pro.lower() == 'true' else False
			exception_rebut  = True if exception_rebut.lower() == 'true' else False

			logger('set_new_premises_for_x', 'def', 'param related_argument: ' + str(related_argument)
			       + ', param premisegroup_id: ' + str(premisegroup_id)
			       + ', param current_attack: ' + str(current_attack)
			       + ', param last_attack: ' + str(last_attack)
			       + ', param confrontation_uid: ' + str(confrontation_uid)
			       + ', param premisegroup_con: ' + str(premisegroup_con)
			       + ', param premisegroup_pro: ' + str(premisegroup_pro)
			       + ', param issue: ' + str(issue)
			       + ', param exception_rebut: ' + str(exception_rebut))

			# confrontation_uid is a premise group

			# Interpretation of the parameters
			# User says: E => A             | #related_argument
			# System says:
			#   undermine:  F => !E         | #premisegroup_id  =>  !premisegroup of #related_argument
			#   undercut:   D => !(E=>A)    | #premisegroup_id  =>  !#related_argument
			#   rebut:      B => !A         | #premisegroup_id  =>  !conclusion of #related_argument
			# Handle it, based on current and last attack

			# getting all arguments
			for key in self.request.params:
				logger('set_new_premises_for_x', key, self.request.params[key])
				if 'pro_' in key:
					pro_dict[key] = escape_string(self.request.params[key])
				if 'con_' in key:
					con_dict[key] = escape_string(self.request.params[key])

			return_dict['status'] = '1'
			return_dict.update(DatabaseHelper().handle_inserting_new_statements(
				user = user_id,
				pro_dict = pro_dict,
				con_dict = con_dict,
				transaction = transaction,
				argument_id = related_argument,
				premisegroup_id = premisegroup_id,
				current_attack = current_attack,
				last_attack = last_attack,
				premisegroup_con = premisegroup_con,
				premisegroup_pro = premisegroup_pro,
				issue = issue,
				exception_rebut = exception_rebut
			))

		except KeyError as e:
			logger('set_new_premises_for_x', 'error', repr(e))
			return_dict['status'] = '-1'

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		logger('set_new_premises_for_x', 'def', 'returning')
		return return_json

	# ajax - getting all arguments for the island view
	@view_config(route_name='ajax_get_logfile_for_statement', renderer='json', check_csrf=False)
	def get_logfile_for_statement(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('get_logfile_for_statement', 'def', 'main')

		return_dict = dict()
		try:
			uid = self.request.params['uid']
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			logger('get_logfile_for_statement', 'def', 'params uid: ' + str(uid))
			return_dict = DatabaseHelper().get_logfile_for_statement(uid, issue)
		except KeyError as e:
			logger('get_logfile_for_statement', 'error', repr(e))

		# return_dict = DatabaseHelper().get_logfile_for_premisegroup(uid)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - getting all arguments for the island view
	@view_config(route_name='ajax_set_correcture_of_statement', renderer='json', check_csrf=True)
	def set_correcture_of_statement(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('set_correcture_of_statement', 'def', 'main')

		try:
			uid = self.request.params['uid']
			corrected_text = escape_string(self.request.params['text'])
			is_final = self.request.params['final']
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback
			logger('set_correcture_of_statement', 'def', 'params uid: ' + str(uid) + ', corrected_text: ' + str(corrected_text)
			       + ', final ' + str(is_final))
			return_dict = DatabaseHelper().correct_statement(transaction, self.request.authenticated_userid, uid, corrected_text,
			                                                 is_final, issue)
		except KeyError as e:
			return_dict = dict()
			logger('set_correcture_of_statement', 'error', repr(e))

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - for language switch
	@view_config(route_name='ajax_switch_language', renderer='json')
	def switch_language(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('switch_language', 'def', 'main')

		return_dict = {}
		try:
			lang = self.request.params['lang']
			logger('switch_language', 'def', 'params uid: ' + str(lang))
			self.request.response.set_cookie('_LOCALE_', str(lang))
			return_dict['status'] = '1'
		except KeyError as e:
			logger('swich_language', 'error', repr(e))
			return_dict['status'] = '0'

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)
		return return_json

	# ajax - for shorten url
	@view_config(route_name='ajax_get_shortened_url', renderer='json')
	def get_shortened_url(self):
		"""
		Shortens url with the help of a python lib
		:return: dictionary with shortend url
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		UserHandler().update_last_action(transaction, self.request.authenticated_userid)

		logger('get_shortened_url', 'def', 'main')

		return_dict = {}
		# google_api_key = 'AIzaSyAw0aPsBsAbqEJUP_zJ9Fifbhzs8xkNSw0' # browser is
		# google_api_key = 'AIzaSyDneaEJN9FNGUpXHDZahe9Rhb21FsFNS14' # server id
		# bitly_login = 'dbashhu'
		# bitly_token = ''
		# bitly_key = 'R_d8c4acf2fb554494b65529314d1e11d1'

		try:
			url = self.request.params['url']
			# service = 'GoogleShortener'
			# service = 'BitlyShortener'
			service = 'TinyurlShortener'
			# service_url = 'https://goo.gl/'
			# service_url = 'https://bitly.com/'
			service_url = 'http://tinyurl.com/'
			logger('get_shortened_url', 'def', service + ' will shorten ' + str(url))

			# shortener = Shortener(service, api_key=google_api_key) # TODO use google
			# shortener = Shortener(service, bitly_login=bitly_login, bitly_api_key=bitly_key, bitly_token=bitly_token)
			shortener = Shortener(service)

			short_url = format(shortener.short(url))
			return_dict['url'] = short_url
			return_dict['service'] = service
			return_dict['service_url'] = service_url
			logger('get_shortened_url', 'def', 'short url ' + short_url)

			return_dict['status'] = '1'
		except KeyError as e:
			logger('get_shortened_url', 'error', repr(e))
			return_dict['status'] = '0'

		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)
		return return_json

	# ajax - for attack overview
	@view_config(route_name='ajax_get_attack_overview', renderer='json', check_csrf=True)
	def get_attack_overview(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')

		logger('get_attack_overview', 'def', 'main')
		logger('get_attack_overview', 'check_csrf_token', str(check_csrf_token(self.request)))
		issue = self.request.params['issue'] if 'issue' in self.request.params \
			else self.request.session['issue'] if 'issue' in self.request.session \
			else issue_fallback
		return_dict = DatabaseHelper().get_attack_overview(self.request.authenticated_userid, issue)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - for attack overview
	@view_config(route_name='ajax_get_issue_list', renderer='json')
	def get_issue_list(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')

		logger('get_issue_list', 'def', 'main')

		try:
			lang = str(self.request.cookies['_LOCALE_'])
		except KeyError:
			lang = get_current_registry().settings['pyramid.default_locale_name']

		return_dict = DatabaseHelper().get_issue_list(lang)
		issue = self.request.params['issue'] if 'issue' in self.request.params \
			else self.request.session['issue'] if 'issue' in self.request.session \
			else issue_fallback
		return_dict['current_issue'] = issue
		return_dict['current_issue_arg_count'] = QueryHelper().get_number_of_arguments(issue)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - user login
	@view_config(route_name='ajax_user_login', renderer='json')
	def user_login(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('user_login', 'def', 'main')

		success = '0'
		message = ''
		return_dict = {}

		try:
			nickname = escape_string(self.request.params['user'])
			password = escape_string(self.request.params['password'])
			url = self.request.params['url']
			logger('user_login', 'def', 'params nickname: ' + str(nickname) + ', password: ' + str(password) + ', url: ' + url)

			db_user = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()

			# check for user and password validations
			if not db_user:
				logger('user_login', 'no user', 'user \'' + nickname + '\' does not exists')
				message = 'User does not exists'
			elif not db_user.validate_password(password):
				logger('user_login', 'password not valid', 'wrong password')
				message = 'Wrong password'
			else:
				logger('user_login', 'login', 'login successful')
				headers = remember(self.request, nickname)

				# update timestamp
				logger('user_login', 'login', 'update login timestamp')
				db_user.update_last_logged()
				transaction.commit()

				return HTTPFound(
					location=url,
					headers=headers,
				)

		except KeyError as e:
			logger('user_login', 'error', repr(e))

		return_dict['success'] = str(success)
		return_dict['message'] = str(message)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - user login
	@view_config(route_name='ajax_user_logout', renderer='json')
	def user_logout(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('user_logout', 'def', 'main')

		url = self.request.params['url']
		logger('user_logout', 'def', 'url: ' + url)

		if ('setting' in url):
			url = self.request.application_url
			logger('user_logout', 'def', 'redirect: ' + url)

		headers = forget(self.request)
		return HTTPFound(
			location=url,
			headers=headers,
		)

	# ajax - registration of users
	@view_config(route_name='ajax_user_registration', renderer='json')
	def user_registration(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('user_registration', 'def', 'main')

		success = '0'
		message = ''
		return_dict = {}

		for param in self.request.params:
			logger('user_registration', 'def', param)

		try:
			firstname       = escape_string(self.request.params['firstname'])
			lastname        = escape_string(self.request.params['lastname'])
			nickname        = escape_string(self.request.params['nickname'])
			email           = escape_string(self.request.params['email'])
			gender          = escape_string(self.request.params['gender'])
			password        = escape_string(self.request.params['password'])
			passwordconfirm = escape_string(self.request.params['passwordconfirm'])
			lang            = self.request.params['lang']
			logger('user_registration', 'def', 'params firstname: ' + str(firstname)
			       + ', lastname: ' + str(lastname)
			       + ', nickname: ' + str(nickname)
			       + ', email: ' + str(email)
			       + ', password: ' + str(password)
			       + ', passwordconfirm: ' + str(passwordconfirm)
			       + ', lang: ' + lang)

			t = Translator(lang)

			# database queries mail verification
			db_nick = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
			db_mail = DBDiscussionSession.query(User).filter_by(email=email).first()
			logger('user_registration', 'main', 'Validating email')
			is_mail_valid = validate_email(email, check_mx=True)

			# are the password equal?
			if not password == passwordconfirm:
				logger('user_registration', 'main', 'Passwords are not equal')
				message = t.get('pwdNotEqual')
			# is the nick already taken?
			elif db_nick:
				logger('user_registration', 'main', 'Nickname \'' + nickname + '\' is taken')
				message = t.get('nickIsTaken')
			# is the email already taken?
			elif db_mail:
				logger('user_registration', 'main', 'E-Mail \'' + email + '\' is taken')
				message = t.get('mailIsTaken')
			# is the email valid?
			elif not is_mail_valid:
				logger('user_registration', 'main', 'E-Mail \'' + email + '\' is not valid')
				message = t.get('mailNotValid')
			# is the token valid?
			# elif request_token != token :
			# 	logger('user_registration', 'main', 'token is not valid')
			# 	logger('user_registration', 'main', 'request_token: ' + str(request_token))
			# 	logger('user_registration', 'main', 'token: ' + str(token))
			# 	message = 'CSRF-Token is not valid'
			else:
				# getting the editors group
				db_group = DBDiscussionSession.query(Group).filter_by(name="editors").first()

				# does the group exists?
				if not db_group:
					message = t.get('errorTryLateOrContant')
					logger('user_registration', 'main', 'Error occured')
				else:
					# creating a new user with hased password
					logger('user_registration', 'main', 'Adding user')
					hashedPassword = PasswordHandler().get_hashed_password(password)
					newuser = User(firstname=firstname,
					               surname=lastname,
					               email=email,
					               nickname=nickname,
					               password=hashedPassword,
					               gender=gender,
					               group=db_group.uid)
					DBDiscussionSession.add(newuser)
					transaction.commit()

					# sanity check, whether the user exists
					checknewuser = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
					if checknewuser:
						logger('user_registration', 'main', 'New data was added with uid ' + str(checknewuser.uid))
						message = t.get('accountWasAdded')
						success = '1'

						# sending an email
						subject = 'D-BAS Account Registration'
						body = t.get('accountWasRegistered')
						EmailHelper().send_mail(self.request, subject, body, email, lang)

					else:
						logger('user_registration', 'main', 'New data was not added')
						message = t.get('accoutErrorTryLateOrContant')

		except KeyError as e:
			logger('user_registration', 'error', repr(e))

		return_dict['success'] = str(success)
		return_dict['message'] = str(message)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - password requests
	@view_config(route_name='ajax_user_password_request', renderer='json')
	def user_password_request(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('user_password_request', 'def', 'main')

		success = '0'
		message = ''
		return_dict = {}

		try:
			email = escape_string(self.request.params['email'])
			lang = self.request.params['lang']
			logger('user_password_request', 'def', 'params email: ' + str(email) + ', lang ' + lang)
			success = '1'
			t = Translator(lang)

			db_user = DBDiscussionSession.query(User).filter_by(email=email).first()

			# does the user exists?
			if db_user:
				# get password and hashed password
				pwd = PasswordGenerator().get_rnd_passwd()
				logger('user_password_request', 'form.passwordrequest.submitted', 'New password is ' + pwd)
				hashedpwd = PasswordHandler().get_hashed_password(pwd)
				logger('user_password_request', 'form.passwordrequest.submitted', 'New hashed password is ' + hashedpwd)

				# set the hased one
				db_user.password = hashedpwd
				DBDiscussionSession.add(db_user)
				transaction.commit()

				body = t.get('nicknameIs') + db_user.nickname + '\n'
				body += t.get('newPwdIs') + pwd
				subject = t.get('dbasPwdRequest')
				reg_success, reg_failed, message= EmailHelper().send_mail(self.request, subject, body, email, lang)

				# logger
				if reg_success:
					logger('user_password_request', 'form.passwordrequest.submitted', 'New password was sent')
					success = '1'
				elif reg_failed:
					logger('user_password_request', 'form.passwordrequest.submitted', 'Error occured')
			else:
				logger('user_password_request', 'form.passwordrequest.submitted', 'Mail unknown')
				message = 'emailUnknown'


		except KeyError as e:
			logger('user_password_request', 'error', repr(e))

		return_dict['success'] = str(success)
		return_dict['message'] = str(message)
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - for getting all news
	@view_config(route_name='ajax_get_news', renderer='json')
	def get_news(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')

		logger('get_news', 'def', 'main')
		return_dict = DatabaseHelper().get_news()
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - for sending news
	@view_config(route_name='ajax_send_news', renderer='json')
	def send_news(self):
		"""

		:return:
		"""
		try:
			title = escape_string(self.request.params['title'])
			text = escape_string(self.request.params['text'])
			return_dict = DatabaseHelper().set_news(transaction, title, text, self.request.authenticated_userid)
		except KeyError as e:
			return_dict = dict()
			logger('ajax_send_news', 'error', repr(e))
			return_dict['status'] = '-1'

		logger('send_news', 'def', 'main')
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json

	# ajax - for fuzzy search
	@view_config(route_name='ajax_fuzzy_search', renderer='json')
	def fuzzy_search(self):
		"""

		:return:
		"""
		logger('- - - - - - - - - - - -', '- - - - - - - - - - - -', '- - - - - - - - - - - -')
		logger('fuzzy_search', 'main', 'def')
		try:
			value = self.request.params['value']
			mode = str(self.request.params['type'])
			issue = self.request.params['issue'] if 'issue' in self.request.params \
				else self.request.session['issue'] if 'issue' in self.request.session \
				else issue_fallback

			logger('fuzzy_search', 'main', 'value: ' + str(value) + ', mode: ' + str(mode) + ', issue: ' + str(issue))
			if mode == '0': # start statement
				return_dict = DatabaseHelper().get_fuzzy_string_for_start(value, issue, True)
			elif mode == '1': # edit statement popup
				statement_uid = self.request.params['extra']
				return_dict = DatabaseHelper().get_fuzzy_string_for_edits(value, statement_uid, issue)
			elif mode == '2':  # start premise
				return_dict = DatabaseHelper().get_fuzzy_string_for_start(value, issue, False)
			elif mode == '3':  # adding reasons
				return_dict = DatabaseHelper().get_fuzzy_string_for_reasons(value, issue)
			else:
				logger('fuzzy_search', 'main', 'unkown mode: ' + str(mode))
				return_dict = dict()
		except KeyError as e:
			return_dict = dict()
			logger('fuzzy_search', 'error', repr(e))
		return_json = DictionaryHelper().dictionary_to_json_array(return_dict, True)

		return return_json



	# ajax - for additional service
	@view_config(route_name='ajax_additional_service', renderer='json')
	def additional_service(self):
		"""

		:return:
		"""
		logger('additional_service', 'main', 'def')
		type = self.request.params['type']

		if type == "chuck":
			data = requests.get('http://api.icndb.com/jokes/random')
		else:
			data = requests.get('http://api.yomomma.info/')

		for a in data.json():
			logger('additional_service', 'main', str(a) + ': ' + str(data.json()[a]))

		return data.json()
