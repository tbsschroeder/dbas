# coding=utf-8
from cornice import Errors
from cornice.util import json_error

import dbas.handler.issue as issue_handler
from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import User, Issue, Statement
from dbas.handler.language import get_language_from_cookie
from dbas.logger import logger
from dbas.strings.keywords import Keywords as _
from dbas.strings.translator import Translator


def combine(*decorators):
    """
    Requires a list of decorators, which will be chained together

    :param decorators:
    :return:
    """

    def floo(view_callable):
        for decorator in decorators:
            view_callable = decorator(view_callable)
        return view_callable

    return floo


def valid_user(request):
    db_user = DBDiscussionSession.query(User).filter_by(nickname=request.authenticated_userid).one_or_none()

    if db_user:
        request.validated['user'] = db_user
    else:
        logger('validation', 'valid_user', 'no user is given', error=True)
        _tn = Translator(get_language_from_cookie(request))
        request.errors.add('body', 'Invalid user', _tn.get(_.checkNickname))
        request.errors.status = 400


def valid_issue(request):
    db_issue = DBDiscussionSession.query(Issue).get(issue_handler.get_issue_id(request))

    if db_issue:
        request.validated['issue'] = db_issue
        return True
    else:
        logger('validation', 'valid_issue', 'no issue is given', error=True)
        request.errors.add('body', 'Invalid issue')
        request.errors.status = 400
        return False


def valid_issue_not_readonly(request):
    if valid_issue(request) and not request.validated.get('issue').is_read_only:
        return True

    logger('validation', 'valid_issue_not_readonly', 'issue is read only', error=True)
    _tn = Translator(get_language_from_cookie(request))
    request.errors.add('body', 'Issue readonly', _tn.get(_.discussionIsReadOnly))
    request.errors.status = 400
    return False


def valid_conclusion(request):
    conclusion_id = request.json_body.get('conclusion_id')
    issue_id = request.validated['issue'].uid if 'issue' in request.validated else issue_handler.get_issue_id(request)

    if conclusion_id:
        db_conclusion = DBDiscussionSession.query(Statement).filter_by(uid=conclusion_id, issue_uid=issue_id).first()
        request.validated['conclusion'] = db_conclusion
    else:
        logger('validation', 'valid_conclusion', 'conclusion id is missing', error=True)
        _tn = Translator(get_language_from_cookie(request))
        request.errors.add('body', 'Invalid conclusion id', _tn.get(_.wrongConclusion))
        request.errors.status = 400


def valid_statement_text(request):
    min_length = 10
    text = request.json_body.get('statement', '')

    if len(text) < min_length:
        _tn = Translator(get_language_from_cookie(request))
        a = _tn.get(_.notInsertedErrorBecauseEmpty)
        b = _tn.get(_.minLength)
        c = _tn.get(_.eachStatement)
        error = '{} ({}: {} {})'.format(a, b, min_length, c)
        request.errors.add('body', 'Text too short', error)
        request.errors.status = 400

    else:
        request.validated['statement'] = text


def has_keywords(*keywords):
    def valid_keywords(request):
        for keyword in keywords:
            value = request.json_body.get(keyword)

            if value:
                request.validated[keyword] = value
            else:
                logger('validation', 'valid_keywords', 'keyword: {} is not there'.format(keyword), error=True)
                request.errors.add('body', '{} is missing'.format(keyword))
                request.errors.status = 400

    return valid_keywords


class validate(object):
    """
        Applies all validators to this function.
        If one of the validators adds an error, the function will not be called.
        In this situation a response is given with a json body, containing all errors from all validators.

        Decorate a function like this

        .. code-block:: python
        @validate(validators=(check_for_user, check_for_issue, )
        def my_view(request)
    """

    def __init__(self, *validators):
        self.validators = validators

    def __call__(self, func):
        def inner(request):
            if not hasattr(request, 'validated'):
                setattr(request, 'validated', {})
            if not hasattr(request, 'errors'):
                setattr(request, 'errors', Errors())
            if not hasattr(request, 'info'):
                setattr(request, 'info', {})

            for validator in self.validators:
                validator(request=request)

            if len(request.errors) > 0:
                return json_error(request)

            return func(request)

        return inner
