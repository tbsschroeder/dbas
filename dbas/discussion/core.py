import logging

import dbas.handler.issue as issue_helper
from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import Argument, User, Issue, Statement
from dbas.handler import user
from dbas.handler.voting import add_click_for_argument
from dbas.helper.dictionary.discussion import DiscussionDictHelper
from dbas.helper.dictionary.items import ItemDictHelper
from dbas.helper.steps import handle_justification_statement, handle_justification_dontknow, \
    handle_justification_argument
from dbas.lib import Relations
from dbas.review.reputation import ReputationReasons, add_reputation_and_check_review_access
from dbas.strings.keywords import Keywords as _
from dbas.strings.translator import Translator

LOG = logging.getLogger(__name__)


def init(db_issue: Issue, db_user: User) -> dict:
    """
    Initialize the discussion. Creates helper and returns a dictionary containing the first elements needed for the
    discussion.

    :param db_issue: Issue
    :param db_user: User
    :return: prepared collection with first elements for the discussion
    """
    LOG.debug("Entering init of discussion.core")
    slug = db_issue.slug

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    disc_ui_locales = issue_dict['lang']

    _ddh = DiscussionDictHelper(disc_ui_locales, nickname=db_user.nickname, slug=slug)

    item_dict = ItemDictHelper(disc_ui_locales, db_issue).get_array_for_start(db_user)
    discussion_dict = _ddh.get_dict_for_start(position_count=(len(item_dict['elements'])))

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def attitude(db_issue: Issue, db_user: User, db_statement: Statement, history: str, path: str) -> dict:
    """
    Initialize the attitude step for a position in a discussion. Creates helper and returns a dictionary containing
    the first elements needed for the discussion.

    :param db_issue: Issue
    :param db_user: User
    :param db_statement: Statement with is_position == True
    :param history: Current history
    :param path:
    :return: prepared collection dict for the discussion
    :rtype: dict
    """
    LOG.debug("Entering attitude function of discussion.core")

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    disc_ui_locales = db_issue.lang

    _ddh = DiscussionDictHelper(disc_ui_locales, db_user.nickname, slug=db_issue.slug)
    discussion_dict = _ddh.get_dict_for_attitude(db_statement)

    _idh = ItemDictHelper(disc_ui_locales, db_issue, path=path, history=history)
    item_dict = _idh.prepare_item_dict_for_attitude(db_statement.uid)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def justify_statement(db_issue: Issue, db_user: User, db_statement: Statement, user_attitude: str, history,
                      path) -> dict:
    """
    Initialize the justification step for a statement or an argument in a discussion. Creates helper and
    returns a dictionary containing the necessary elements needed for the discussion.

    :param db_issue:
    :param db_user:
    :param db_statement:
    :param user_attitude:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering justify_statement")

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    item_dict, discussion_dict = handle_justification_statement(db_issue, db_user, db_statement, user_attitude,
                                                                history, path)
    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def dont_know_argument(db_issue: Issue, db_user: User, db_argument: Argument, history: str, path: str) -> dict:
    """
    Initialize the justification step for a statement or an argument in a discussion. Creates helper and
    returns a dictionary containing the necessary elements needed for the discussion.

    :param db_issue:
    :param db_user:
    :param db_argument:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering dont_know_argument")

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    item_dict, discussion_dict = handle_justification_dontknow(db_issue, db_user, db_argument, history, path)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def justify_argument(db_issue: Issue, db_user: User, db_argument: Argument, user_attitude: str, relation: str,
                     history: str, path: str) -> dict:
    """
    Initialize the justification step for a statement or an argument in a discussion. Creates helper and
    returns a dictionary containing the necessary elements needed for the discussion.

    :param db_issue:
    :param db_user:
    :param db_argument:
    :param user_attitude:
    :param relation:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering justify_argument")

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    item_dict, discussion_dict = handle_justification_argument(db_issue, db_user, db_argument, user_attitude, relation,
                                                               history, path)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def reaction(db_issue: Issue, db_user: User, db_arg_user: Argument, db_arg_sys: Argument, relation: Relations, history,
             path) -> dict:
    """
    Initialize the reaction step for a position in a discussion. Creates helper and returns a dictionary containing
    different feedback options for the confrontation with an argument in a discussion.

    :param db_issue:
    :param db_user:
    :param db_arg_user:
    :param db_arg_sys:
    :param relation:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering reaction function")
    # set votes and reputation
    broke_limit = add_reputation_and_check_review_access(db_user, ReputationReasons.first_argument_click)

    add_click_for_argument(db_arg_user, db_user)

    _ddh = DiscussionDictHelper(db_issue.lang, db_user.nickname, history, slug=db_issue.slug, broke_limit=broke_limit)
    _idh = ItemDictHelper(db_issue.lang, db_issue, path=path, history=history)
    discussion_dict = _ddh.get_dict_for_argumentation(db_arg_user, db_arg_sys.uid, relation, history, db_user)
    item_dict = _idh.get_array_for_reaction(db_arg_sys.uid, db_arg_user.uid, db_arg_user.is_supportive, relation,
                                            discussion_dict['gender'])

    return {
        'issues': issue_helper.prepare_json_of_issue(db_issue, db_user),
        'discussion': discussion_dict,
        'items': item_dict,
        'title': db_issue.title
    }


def support(db_issue: Issue, db_user: User, db_arg_user: Argument, db_arg_sys: Argument, history: str,
            path: str) -> dict:
    """
    Initialize the support step for the end of a branch in a discussion. Creates helper and returns a dictionary
    containing the first elements needed for the discussion.

    :param db_issue:
    :param db_user:
    :param db_arg_user:
    :param db_arg_sys:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering support function")
    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    disc_ui_locales = issue_dict['lang']

    _ddh = DiscussionDictHelper(disc_ui_locales, db_user.nickname, history, slug=db_issue.slug)
    _idh = ItemDictHelper(disc_ui_locales, db_issue, path=path, history=history)
    discussion_dict = _ddh.get_dict_for_supporting_each_other(db_arg_sys.uid, db_arg_user.uid, db_user.nickname)
    item_dict = _idh.get_array_for_support(db_arg_sys.uid, db_issue.slug)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def choose(db_issue: Issue, db_user: User, pgroup_ids: [int], history: str, path: str) -> dict:
    """
    Initialize the choose step for more than one premise in a discussion. Creates helper and returns a dictionary
    containing several feedback options regarding this argument.

    :param db_issue:
    :param db_user:
    :param pgroup_ids:
    :param history:
    :param path:
    :return:
    """
    LOG.debug("Entering choose function")
    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    disc_ui_locales = issue_dict['lang']

    created_argument: Argument = DBDiscussionSession.query(Argument).filter(
        Argument.premisegroup_uid == pgroup_ids[0]).one()
    is_supportive = created_argument.is_supportive
    conclusion_is_argument = created_argument.attacks is not None
    if conclusion_is_argument:
        conclusion = created_argument.attacks
    else:
        conclusion = created_argument.conclusion

    _ddh = DiscussionDictHelper(disc_ui_locales, db_user.nickname, history, slug=db_issue.slug)
    _idh = ItemDictHelper(disc_ui_locales, db_issue, path=path, history=history)
    discussion_dict = _ddh.get_dict_for_choosing(conclusion.uid, conclusion_is_argument, is_supportive)
    item_dict = _idh.get_array_for_choosing(conclusion.uid, pgroup_ids, conclusion_is_argument, is_supportive,
                                            db_user.nickname)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def jump(db_issue: Issue, db_user: User, db_argument: Argument, history: str, path: str) -> dict:
    """
    Initialize the jump step for an argument in a discussion. Creates helper and returns a dictionary containing
    several feedback options regarding this argument.

    :param db_issue: The issue that shall be jumped to
    :param db_user: The concerning user
    :param db_argument:
    :param history:
    :param path:
    :rtype: dict
    :return: prepared collection matchdict for the discussion
    """
    LOG.debug("Entering jump function")

    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)
    disc_ui_locales = issue_dict['lang']

    _ddh = DiscussionDictHelper(disc_ui_locales, db_user.nickname, history, slug=db_issue.slug)
    _idh = ItemDictHelper(disc_ui_locales, db_issue, path=path, history=history)
    discussion_dict = _ddh.get_dict_for_jump(db_argument.uid)
    item_dict = _idh.get_array_for_jump(db_argument.uid, db_issue.slug)

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def finish(db_issue: Issue, db_user: User, db_argument: Argument, history: str) -> dict:
    issue_dict = issue_helper.prepare_json_of_issue(db_issue, db_user)

    _ddh = DiscussionDictHelper(db_issue.lang, db_user.nickname, history, slug=db_issue.slug)
    discussion_dict = _ddh.get_dict_for_argumentation(db_argument, None, None, history, db_user)
    item_dict = ItemDictHelper.get_empty_dict()

    return {
        'issues': issue_dict,
        'discussion': discussion_dict,
        'items': item_dict,
        'title': issue_dict['title']
    }


def exit(ui_locales: str, db_user: User) -> dict:
    """
    Exit the discussion. Creates helper and returns a dictionary containing the summary of today.

    :param ui_locales:
    :param db_user:
    :rtype: dict
    :return: prepared collection with summary of current day's actions of the user
    """
    return {
        'title': Translator(ui_locales).get(_.finishTitle),
        'summary': user.get_summary_of_today(db_user)
    }
