from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from dbas.database.discussion_model import ReviewDelete, ReviewEdit, ReviewDuplicate, ReviewOptimization, ReviewSplit, \
    ReviewMerge
from dbas.handler.language import get_language_from_cookie
from dbas.helper.query import revoke_author_of_statement_content, revoke_author_of_argument_content
from dbas.lib import get_discussion_language
from dbas.logger import logger
from dbas.review import flags as review_flag_helper, queues as review_queue_helper
from dbas.review.mapper import get_review_model_by_key
from dbas.review.queue import key_edit, key_delete, key_duplicate, key_optimization, key_merge, key_split
from dbas.review.queue.adapter import QueueAdapter
from dbas.review.queue.delete import DeleteQueue
from dbas.review.queue.duplicate import DuplicateQueue
from dbas.review.queue.edit import EditQueue
from dbas.review.queue.merge import MergeQueue
from dbas.review.queue.optimization import OptimizationQueue
from dbas.review.queue.split import SplitQueue
from dbas.strings.translator import Translator
from dbas.validators.core import validate, has_keywords, has_maybe_keywords
from dbas.validators.database import valid_database_model
from dbas.validators.discussion import valid_premisegroup, valid_text_values, valid_statement, valid_argument
from dbas.validators.reviews import valid_review_reason, valid_not_executed_review, valid_uid_as_row_in_review_queue
from dbas.validators.user import valid_user, valid_user_as_author, valid_user_as_author_of_statement, \
    valid_user_as_author_of_argument
from websocket.lib import send_request_for_recent_reviewer_socketio


@view_config(route_name='flag_argument_or_statement', renderer='json')
@validate(valid_user, valid_review_reason, has_keywords(('uid', int), ('is_argument', bool)),
          has_maybe_keywords(('extra_uid', int, None)))
def flag_argument_or_statement(request):
    """
    Flags an argument or statement for a specific reason

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    uid = request.validated['uid']
    reason = request.validated['reason']
    extra_uid = request.validated['extra_uid']
    is_argument = request.validated['is_argument']
    db_user = request.validated['user']
    return review_flag_helper.flag_element(uid, reason, db_user, is_argument, ui_locales, extra_uid)


@view_config(route_name='split_or_merge_statement', renderer='json')
@validate(valid_user, valid_premisegroup, valid_text_values, has_keywords(('key', str)))
def split_or_merge_statement(request):
    """
    Flags a statement for a specific reason

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    _tn = Translator(ui_locales)
    db_user = request.validated['user']
    pgroup = request.validated['pgroup']
    key = request.validated['key']
    tvalues = request.validated['text_values']

    if key not in ['merge', 'split']:
        raise HTTPBadRequest()
    return review_flag_helper.flag_statement_for_merge_or_split(key, pgroup, tvalues, db_user, _tn)


@view_config(route_name='split_or_merge_premisegroup', renderer='json')
@validate(valid_user, valid_premisegroup, has_keywords(('key', str)))
def split_or_merge_premisegroup(request):
    """
    Flags a premisegroup for a specific reason

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.params))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    _tn = Translator(ui_locales)
    db_user = request.validated['user']
    pgroup = request.validated['pgroup']
    key = request.validated['key']

    if key not in ['merge', 'split']:
        raise HTTPBadRequest()
    return review_flag_helper.flag_pgroup_for_merge_or_split(key, pgroup, db_user, _tn)


@view_config(route_name='review_delete_argument', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewDelete), has_keywords(('should_delete', bool)))
def review_delete_argument(request):
    """
    Values for the review for an argument, which should be deleted

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    should_delete = request.validated['should_delete']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(DeleteQueue(), db_user, main_page, _t).add_vote(db_review, should_delete)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_delete)
    return True


@view_config(route_name='review_edit_argument', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewEdit), has_keywords(('is_edit_okay', bool)))
def review_edit_argument(request):
    """
    Values for the review for an argument, which should be edited

    :param request: current request of the server
    :return: json-dict()
    """
    logger('Views', 'main: {} - {}'.format(request.json_body, request.authenticated_userid))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    is_edit_okay = request.validated['is_edit_okay']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(EditQueue(), db_user, main_page, _t).add_vote(db_review, is_edit_okay)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_edit)
    return True


@view_config(route_name='review_duplicate_statement', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewDuplicate), has_keywords(('is_duplicate', bool)))
def review_duplicate_statement(request):
    """
    Values for the review for an argument, which is maybe a duplicate

    :param request: current request of the server
    :return: json-dict()
    """
    logger('Views', 'main: {} - {}'.format(request.json_body, request.authenticated_userid))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    is_duplicate = request.validated['is_duplicate']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(DuplicateQueue(), db_user, main_page, _t).add_vote(db_review, is_duplicate)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_duplicate)
    return True


@view_config(route_name='review_optimization_argument', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewOptimization),
          has_keywords(('should_optimized', bool), ('new_data', list)))
def review_optimization_argument(request):
    """
    Values for the review for an argument, which should be optimized

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {} - {}'.format(request.json_body, request.authenticated_userid))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    should_optimized = request.validated['should_optimized']
    new_data = request.validated['new_data']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(OptimizationQueue(), db_user, main_page, _t, new_data=new_data).add_vote(db_review, should_optimized)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_optimization)
    return True


@view_config(route_name='review_splitted_premisegroup', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewSplit), has_keywords(('should_split', bool)))
def review_splitted_premisegroup(request):
    """
    Values for the review for a premisegroup, which should be splitted

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {} - {}'.format(request.json_body, request.authenticated_userid))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    should_split = request.validated['should_split']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(SplitQueue(), db_user, main_page, _t).add_vote(db_review, should_split)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_split)
    return True


@view_config(route_name='review_merged_premisegroup', renderer='json')
@validate(valid_user, valid_not_executed_review('review_uid', ReviewMerge), has_keywords(('should_merge', bool)))
def review_merged_premisegroup(request):
    """
    Values for the review for a statement, which should be merged

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {} - {}'.format(request.json_body, request.authenticated_userid))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    db_review = request.validated['db_review']
    db_user = request.validated['user']
    should_merge = request.validated['should_merge']
    main_page = request.application_url
    _t = Translator(ui_locales)

    QueueAdapter(MergeQueue(), db_user, main_page, _t).add_vote(db_review, should_merge)
    send_request_for_recent_reviewer_socketio(db_user.nickname, main_page, key_merge)
    return True


@view_config(route_name='undo_review', renderer='json')
@validate(valid_user_as_author, valid_uid_as_row_in_review_queue, has_keywords(('queue', str)))
def undo_review(request):
    """
    Trys to undo a done review process

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    db_user = request.validated['user']
    queue = request.validated['queue']
    db_review = request.validated['review']
    _tn = Translator(get_language_from_cookie(request))

    queue = get_review_model_by_key(queue)
    adapter = QueueAdapter(queue(), db_user, request.application_url, _tn)
    return adapter.revoke_ballot(db_review)


@view_config(route_name='cancel_review', renderer='json')
@validate(valid_user_as_author, valid_uid_as_row_in_review_queue, has_keywords(('queue', str)))
def cancel_review(request):
    """
    Trys to cancel an ongoing review

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    db_user = request.validated['user']
    queue = request.validated['queue']
    db_review = request.validated['review']
    _tn = Translator(get_language_from_cookie(request))

    queue = get_review_model_by_key(queue)
    adapter = QueueAdapter(queue(), db_user, request.application_url, _tn)
    return adapter.cancel_ballot(db_review)


@view_config(route_name='review_lock', renderer='json', require_csrf=False)
@validate(valid_user, valid_database_model('review_uid', ReviewOptimization), has_keywords(('lock', bool)))
def review_lock(request):
    """
    Locks an optimization review so that the user can do an edit

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    ui_locales = get_discussion_language(request.matchdict, request.params, request.session)
    _tn = Translator(ui_locales)
    lock = request.validated['lock']
    db_review = request.validated['db_model']
    db_user = request.validated['user']

    if lock:
        return review_queue_helper.lock_optimization_review(db_user, db_review, _tn)
    else:
        return review_queue_helper.unlock_optimization_review(db_review, _tn)


@view_config(route_name='revoke_statement_content', renderer='json', require_csrf=False)
@validate(valid_user_as_author_of_statement, valid_statement(location='json_body'))
def revoke_statement_content(request):
    """
    Revokes the given user as author from a statement

    :param request: current request of the server
    :return: json-dict()
    """
    logger('views', 'main: {}'.format(request.json_body))
    db_user = request.validated['user']
    statement = request.validated['statement']
    return revoke_author_of_statement_content(statement, db_user)


@view_config(route_name='revoke_argument_content', renderer='json', require_csrf=False)
@validate(valid_user_as_author_of_argument, valid_argument(location='json_body'))
def revoke_argument_content(request):
    db_user = request.validated['user']
    argument = request.validated['argument']
    return revoke_author_of_argument_content(argument, db_user)
