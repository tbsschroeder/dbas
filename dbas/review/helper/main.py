"""
Provides helping function for the managing reviews.

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""

from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import User, ReviewDelete, LastReviewerDelete, Argument, Premise, Statement
from dbas.review.helper.reputation import add_reputation_for, rep_reason_success_flag, rep_reason_bad_flag

max_votes = 5
min_difference = 3


def add_review_opinion_for_delete(nickname, should_delete, review_uid, transaction):
    """

    :param nickname:
    :param should_delete:
    :param review_uid:
    :param transaction:
    :return:
    """
    db_user = DBDiscussionSession.query(User).filter_by(nickname=nickname).first()
    db_review = DBDiscussionSession.query(ReviewDelete).filter_by(uid=review_uid).first()
    if db_review.is_executed or not db_user:
        return None

    # get all keep and delete votes
    db_reviews = DBDiscussionSession.query(LastReviewerDelete).filter_by(review_uid=review_uid)
    db_keep_reviews = db_reviews.filter_by(is_okay=True).all()
    db_delete_reviews = db_reviews.filter_by(is_okay=False).all()

    # get sum of all votes
    count_of_keep = len(db_keep_reviews) + (1 if not should_delete else 0)
    count_of_delete = len(db_delete_reviews) + (1 if should_delete else 0)

    # do we reached any limit?
    reached_max = max(count_of_keep, count_of_delete) >= max_votes
    if reached_max:
        if count_of_delete > count_of_keep:  # disable the flagged part
            en_or_disable_arguments_and_premise_of_review(db_review, True)
            add_reputation_for(db_user, rep_reason_success_flag, transaction)
        else:  # just close the review
            db_review.set_executed(False)
            add_reputation_for(db_user, rep_reason_bad_flag, transaction)

    if count_of_keep - count_of_delete >= min_difference:  # just close the review
        db_review.set_executed(False)
        add_reputation_for(db_user, rep_reason_bad_flag, transaction)

    if count_of_delete - count_of_keep >= min_difference:  # disable the flagged part
        en_or_disable_arguments_and_premise_of_review(db_review, True)
        add_reputation_for(db_user, rep_reason_success_flag, transaction)

    # add karma to voter

    # add new vote
    db_new_review = LastReviewerDelete(db_user.uid, db_review.uid, not should_delete)
    DBDiscussionSession.add(db_new_review)
    DBDiscussionSession.flush()
    transaction.commit()

    return None


def en_or_disable_arguments_and_premise_of_review(review, is_disabled):
    """

    :param review:
    :param is_disabled:
    :return:
    """
    db_argument = DBDiscussionSession.query(Argument).filter_by(uid=review.argument_uid).first()
    db_argument.set_disable(is_disabled)
    db_premises = DBDiscussionSession.query(Premise).filter_by(premisesgroup_uid=db_argument.premisesgroup_uid).join(Statement).all()
    for premise in db_premises:
        premise.statements.set_disable(is_disabled)