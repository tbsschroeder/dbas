"""
TODO

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""

from pyramid.security import Allow, Everyone
from dbas.views import logger
from .database import DBDiscussionSession
from .database.discussion_model import User, Group
from sqlalchemy.exc import InternalError as sqlie


class RootFactory(object):
    """
    Defines the ACL
    """
    __acl__ = [(Allow, Everyone, 'everybody'),
               (Allow, 'group:admins', ('admin', 'edit', 'use')),
               (Allow, 'group:authors', ('edit', 'use')),
               (Allow, 'group:users', 'use')]

    def __init__(self, request):
        pass


def groupfinder(nick, request):
    """
    Finds group for the user id in given request
    :param nick: current user id
    :param request: request
    :return: given group as list or empty list
    """
    logger('security', 'groupfinder', 'parameter nick = ' + nick)
    try:
        user = DBDiscussionSession.query(User).filter_by(nickname=nick).first()
    except sqlie:
        return []

    if user:
        group = DBDiscussionSession.query(Group).filter_by(uid=user.group_uid).first()
        if group:
            logger('security', 'groupfinder', 'return [group:' + group.name + ']')
            return ['group:' + group.name]

    logger('security', 'groupfinder', 'return []')
    return []
