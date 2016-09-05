"""
Provides helping function for the managing reputation.

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""

import dbas.user_management as _user_manager
from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import User, ReviewDelete, LastReviewerDelete, ReviewOptimization, \
    LastReviewerOptimization, OptimizationReviewLocks, get_now
from dbas.review.helper.reputation import get_reputation_of
from dbas.review.helper.subpage import reputation_borders
from sqlalchemy import and_


def get_review_queues_array(mainpage, translator, nickname):
    """
    Prepares dictionary for the edit section.

    :param mainpage: URL
    :param translator: Translator
    :param nickname: Users nickname
    :return: Array
    """
    db_user = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
    if not db_user:
        return None

    review_list = list()
    review_list.append(__get_delete_dict(mainpage, translator, nickname))
    review_list.append(__get_optimization_dict(mainpage, translator, nickname))
    review_list.append(__get_history_dict(mainpage, translator, nickname))

    return review_list


def __get_delete_dict(mainpage, translator, nickname):
    """
    Prepares dictionary for the a section.

    :param mainpage: URL
    :param translator: Translator
    :param nickname: Users nickname
    :return: Dict()
    """
    task_count = __get_review_count_for(ReviewDelete, LastReviewerDelete, nickname)

    key = 'deletes'
    count, all_rights = get_reputation_of(nickname)
    tmp_dict = {'task_name': 'Deletes',
                'id': 'deletes',
                'url': mainpage + '/review/' + key,
                'icon': 'fa fa-trash-o',
                'task_count': task_count,
                'is_allowed': count >= reputation_borders[key] or all_rights,
                'is_allowed_text': translator.get(translator.visitDeleteQueue),
                'is_not_allowed_text': translator.get(translator.visitDeleteQueueLimitation).replace('XX', str(reputation_borders[key])),
                'last_reviews': __get_last_reviewer_of(LastReviewerDelete, mainpage)
                }
    return tmp_dict


def __get_optimization_dict(mainpage, translator, nickname):
    """
    Prepares dictionary for the a section.

    :param mainpage: URL
    :param translator: Translator
    :param nickname: Users nickname
    :return: Dict()
    """
    task_count = __get_review_count_for(ReviewOptimization, LastReviewerOptimization, nickname)

    key = 'optimizations'
    count, all_rights = get_reputation_of(nickname)
    tmp_dict = {'task_name': 'Optimizations',
                'id': 'optimizations',
                'url': mainpage + '/review/' + key,
                'icon': 'fa fa-flag',
                'task_count': task_count,
                'is_allowed': count >= reputation_borders[key] or all_rights,
                'is_allowed_text': translator.get(translator.visitOptimizationQueue),
                'is_not_allowed_text': translator.get(translator.visitOptimizationQueueLimitation).replace('XX', str(reputation_borders[key])),
                'last_reviews': __get_last_reviewer_of(LastReviewerOptimization, mainpage)
                }
    return tmp_dict


def __get_history_dict(mainpage, translator, nickname):
    """
    Prepares dictionary for the a section.

    :param mainpage: URL
    :param translator: Translator
    :param nickname: Users nickname
    :return: Dict()
    """
    key = 'history'
    count, all_rights = get_reputation_of(nickname)
    tmp_dict = {'task_name': 'History',
                'id': 'flags',
                'url': mainpage + '/review/' + key,
                'icon': 'fa fa-history',
                'task_count': '-',
                'is_allowed': count >= reputation_borders[key] or all_rights,
                'is_allowed_text': translator.get(translator.visitHistoryQueue),
                'is_not_allowed_text': translator.get(translator.visitHistoryQueueLimitation).replace('XX', str(reputation_borders[key])),
                'last_reviews': list()
                }
    return tmp_dict


def __get_review_count_for(review_type, last_reviewer_type, nickname):
    """

    :param review_type:
    :param nickname:
    :return:
    """
    db_user = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
    if db_user:
        db_last_reviews_of_user = DBDiscussionSession.query(last_reviewer_type).filter_by(reviewer_uid=db_user.uid).all()
        already_reviewed = []
        for last_review in db_last_reviews_of_user:
            already_reviewed.append(last_review.review_uid)
        db_reviews = DBDiscussionSession.query(review_type).filter(and_(review_type.is_executed == False,
                                                                        review_type.detector_uid != db_user.uid))
        if len(already_reviewed) > 0:
            db_reviews = db_reviews.filter(~review_type.uid.in_(already_reviewed))
        db_reviews = db_reviews.all()
    else:
        db_reviews = DBDiscussionSession.query(review_type).filter_by(is_executed=False).all()
    return len(db_reviews)


def __get_last_reviewer_of(reviewer_type, mainpage):
    """
    Returns a list with the last reviewers of the given type. Multiple reviewers are filtered

    :param reviewer_type:
    :param mainpage:
    :return:
    """
    users_array = list()
    db_reviews = DBDiscussionSession.query(reviewer_type).order_by(reviewer_type.uid.desc()).all()
    limit = 5 if len(db_reviews) >= 5 else len(db_reviews)
    index = 0
    while index < limit:
        db_review = db_reviews[index]
        db_user = DBDiscussionSession.query(User).filter_by(uid=db_review.reviewer_uid).first()
        if db_user:
            tmp_dict = dict()
            tmp_dict['img_src'] = _user_manager.get_profile_picture(db_user, 40)
            tmp_dict['url'] = mainpage + '/user/' + db_user.get_global_nickname()
            tmp_dict['name'] = db_user.get_global_nickname()
            # skip it, if it is already in
            if tmp_dict in users_array:
                limit += 1 if len(db_reviews) > limit else 0
            else:
                users_array.append(tmp_dict)
        else:
            limit += 1 if len(db_reviews) > limit else 0
        index += 1
    return users_array


def lock(nickname, review_uid, translator, transaction):
    """

    :param nickname:
    :param review_uid:
    :param translator:
    :param transaction:
    :return:
    """
    success = ''
    info = ''
    error = ''
    is_locked = False

    # has user already locked an item?
    db_user  = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
    db_review = DBDiscussionSession.query(ReviewOptimization).filter(and_(ReviewOptimization.uid == review_uid,
                                                                          ReviewOptimization.is_executed == False)).first()
    if not db_user or not db_review:
        error = translator.get(translator.internalKeyError)
        return success, info, error, is_locked

    db_locks = DBDiscussionSession.query(OptimizationReviewLocks).filter_by(author_uid=db_user.uid).first()
    if db_locks:
        info = translator.get(translator.dataAlreadyLockedByYou)
        is_locked = True
        return success, info, error, is_locked

    # is already locked?
    if is_review_locked(review_uid):
        info = translator.get(translator.dataAlreadyLockedByOthers)
        is_locked = True
        return success, info, error, is_locked

    db_new_lock = OptimizationReviewLocks(db_user.uid, review_uid)
    DBDiscussionSession.add(db_new_lock)
    DBDiscussionSession.flush()
    transaction.commit()
    is_locked = True

    return success, info, error, is_locked


def unlock(review_uid, transaction):
    """

    :param review_uid:
    :param transaction:
    :return:
    """
    DBDiscussionSession.query(OptimizationReviewLocks).filter_by(review_optimization_uid=review_uid).delete()
    DBDiscussionSession.flush()
    transaction.commit()
    return True


def is_review_locked(review_uid):
    """

    :param review_uid:
    :return:
    """
    db_lock = DBDiscussionSession.query(OptimizationReviewLocks).filter_by(review_optimization_uid=review_uid).first()
    if not db_lock:
        return False
    return (get_now() - db_lock.locked_since).seconds < 3*60
