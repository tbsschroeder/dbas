# Adaptee for the optimizations queue. Every accepted optimization will be an edit.
import random

import transaction
from beaker.session import Session

from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import User, LastReviewerOptimization, ReviewOptimization, ReviewEdit, \
    ReviewEditValue, Statement, Issue, Argument, Premise, ReviewCanceled
from dbas.lib import get_text_for_argument_uid, get_all_arguments_by_statement, get_text_for_statement_uid
from dbas.logger import logger
from dbas.review.queue import max_votes, key_optimization
from dbas.review.queue.abc_queue import QueueABC
from dbas.review.queue.lib import get_issues_for_statement_uids, \
    get_reporter_stats_for_review, get_all_allowed_reviews_for_user, revoke_decision_and_implications
from dbas.review.reputation import get_reason_by_action, add_reputation_and_check_review_access
from dbas.strings.keywords import Keywords as _
from dbas.strings.translator import Translator


class OptimizationQueue(QueueABC):

    def __init__(self):
        super().__init__()
        self.key = key_optimization

    def key(self, key=None):
        """

        :param key:
        :return:
        """
        if not key:
            return key
        else:
            self.key = key

    def get_queue_information(self, db_user: User, session: Session, application_url: str, translator: Translator):
        """
        Setup the subpage for the optimization queue

        :param db_user: User
        :param session: session of current webserver request
        :param application_url: current url of the app
        :param translator: Translator
        :return: dict()
        """
        logger('OptimizationQueue', 'main')
        all_rev_dict = get_all_allowed_reviews_for_user(session, f'already_seen_{self.key}', db_user,
                                                        ReviewOptimization, LastReviewerOptimization)

        extra_info = ''
        # if we have no reviews, try again with fewer restrictions
        if not all_rev_dict['reviews']:
            all_rev_dict['already_seen_reviews'] = list()
            extra_info = 'already_seen' if not all_rev_dict['first_time'] else ''
            db_reviews = DBDiscussionSession.query(ReviewOptimization).filter(ReviewOptimization.is_executed == False,
                                                                              ReviewOptimization.detector_uid != db_user.uid)
            if len(all_rev_dict['already_voted_reviews']) > 0:
                db_reviews = db_reviews.filter(~ReviewOptimization.uid.in_(all_rev_dict['already_voted_reviews']))
            all_rev_dict['reviews'] = db_reviews.all()

        if not all_rev_dict['reviews']:
            return {
                'stats': None,
                'text': None,
                'reason': None,
                'issue_titles': None,
                'context': [],
                'extra_info': None,
                'session': session
            }

        rnd_review = random.choice(all_rev_dict['reviews'])
        if rnd_review.statement_uid is None:
            db_argument = DBDiscussionSession.query(Argument).get(rnd_review.argument_uid)
            text = get_text_for_argument_uid(db_argument.uid)
            issue_titles = [DBDiscussionSession.query(Issue).get(db_argument.issue_uid).title]
            parts = self.__get_text_parts_of_argument(db_argument)
            context = [text]
        else:
            db_statement = DBDiscussionSession.query(Statement).get(rnd_review.statement_uid)
            text = db_statement.get_text()
            issue_titles = [issue.title for issue in get_issues_for_statement_uids([rnd_review.statement_uid])]
            parts = [self.__get_part_dict('statement', text, 0, rnd_review.statement_uid)]
            context = []
            args = get_all_arguments_by_statement(rnd_review.statement_uid)
            if args:
                html_wrap = '<span class="text-info"><strong>{}</strong></span>'
                context = [get_text_for_argument_uid(arg.uid).replace(text, html_wrap.format(text)) for arg in args]

        reason = translator.get(_.argumentFlaggedBecauseOptimization)

        stats = get_reporter_stats_for_review(rnd_review, translator.get_lang(), application_url)

        all_rev_dict['already_seen_reviews'].append(rnd_review.uid)
        session[f'already_seen_{self.key}'] = all_rev_dict['already_seen_reviews']

        return {
            'stats': stats,
            'text': text,
            'reason': reason,
            'issue_titles': issue_titles,
            'extra_info': extra_info,
            'context': context,
            'parts': parts,
            'session': session
        }

    def __get_text_parts_of_argument(self, db_argument: Argument):
        """
        Get all parts of an argument as string

        :param db_argument: Argument.uid
        :return: list of strings
        """
        logger('OptimizationQueue', 'main')
        ret_list = list()

        # get premise of current argument
        db_premises = DBDiscussionSession.query(Premise).filter_by(premisegroup_uid=db_argument.premisegroup_uid).all()
        premises_uids = [premise.uid for premise in db_premises]
        for uid in premises_uids:
            logger('OptimizationQueue', 'add premise of argument ' + str(db_argument.uid))
            text = get_text_for_statement_uid(uid)
            ret_list.append(self.__get_part_dict('premise', text, db_argument.uid, uid))

        if db_argument.argument_uid is None:  # get conclusion of current argument
            conclusion = db_argument.get_conclusion_text()
            logger('OptimizationQueue', 'add statement of argument ' + str(db_argument.uid))
            ret_list.append(self.__get_part_dict('conclusion', conclusion, db_argument.uid, db_argument.conclusion_uid))
        else:  # or get the conclusions argument
            db_conclusions_argument = DBDiscussionSession.query(Argument).get(db_argument.argument_uid)

            while db_conclusions_argument.argument_uid is not None:  # get further conclusions arguments

                # get premise of conclusions arguments
                db_premises = DBDiscussionSession.query(Premise).filter_by(
                    premisegroup_uid=db_argument.premisegroup_uid).all()
                premises_uids = [premise.uid for premise in db_premises]
                for uid in premises_uids:
                    text = get_text_for_statement_uid(uid)
                    logger('OptimizationQueue', 'add premise of argument ' + str(db_conclusions_argument.uid))
                    ret_list.append(self.__get_part_dict('premise', text, db_conclusions_argument.uid, uid))

                db_conclusions_argument = DBDiscussionSession.query(Argument).get(db_conclusions_argument.argument_uid)

            # get the last conclusion of the chain
            conclusion = db_conclusions_argument.get_conclusion_text()
            logger('OptimizationQueue', 'add statement of argument ' + str(db_conclusions_argument.uid))
            ret_list.append(self.__get_part_dict('conclusion', conclusion, db_conclusions_argument.uid,
                                                 db_conclusions_argument.conclusion_uid))

        return ret_list[::-1]

    @staticmethod
    def __get_part_dict(typeof: str, text: str, argument_uid: int, conclusion_uid: int):
        """
        Collects the aprts of the argument-string and builds up a little dict

        :param typeof: String
        :param text: String
        :param argument_uid: Argument.uid
        :return: dict()
        """
        return {
            'type': typeof,
            'text': text,
            'argument_uid': argument_uid,
            'statement_uid': conclusion_uid
        }

    def add_vote(self, db_user: User, db_review: ReviewOptimization, is_okay: bool, application_url: str,
                 translator: Translator, **kwargs):
        """

        :param db_user:
        :param db_review:
        :param is_okay:
        :param application_url:
        :param translator:
        :param kwargs:
        :return:
        """
        logger('OptimizationQueue', 'main')
        # add new review
        db_new_review = LastReviewerOptimization(db_user.uid, db_review.uid, not is_okay)
        DBDiscussionSession.add(db_new_review)
        DBDiscussionSession.flush()
        transaction.commit()

        if is_okay:
            self.__proposal_for_the_element(db_review, kwargs['new_data'], db_user)
        else:
            self.__keep_the_element_of_optimization_review(db_review, application_url, translator)

        DBDiscussionSession.add(db_review)
        DBDiscussionSession.flush()
        transaction.commit()

        return True

    @staticmethod
    def __keep_the_element_of_optimization_review(db_review: ReviewOptimization, main_page: str,
                                                  translator: Translator):
        """
        Adds row for LastReviewerOptimization

        :param db_review: ReviewOptimization
        :param main_page: URL
        :param translator: Translator
        :return: None
        """
        # add new vote
        db_user_created_flag = DBDiscussionSession.query(User).get(db_review.detector_uid)

        # get all keep and delete votes
        db_keep_version = DBDiscussionSession.query(LastReviewerOptimization).filter(
            LastReviewerOptimization.review_uid == db_review.uid,
            LastReviewerOptimization.is_okay == True).all()

        if len(db_keep_version) > max_votes:
            add_reputation_and_check_review_access(db_user_created_flag, get_reason_by_action('bad_flag'),
                                                   main_page, translator)

            db_review.set_executed(True)
            db_review.update_timestamp()
            DBDiscussionSession.add(db_review)
            DBDiscussionSession.flush()
            transaction.commit()

    def __proposal_for_the_element(self, db_review: ReviewOptimization, data: dict, db_user: User):
        """
        Adds proposal for the ReviewEdit

        :param db_review: ReviewEdit
        :param data: dict
        :param db_user: User
        :return: None
        """
        # sort the new edits by argument uid
        argument_dict, statement_dict = self.__prepare_dicts_for_proposals(data)

        logger('OptimizationQueue',
               'detector {}, statements {}, arguments {}'.format(db_user.uid, statement_dict, argument_dict))

        # add reviews
        new_edits = list()
        for argument_uid in argument_dict:
            DBDiscussionSession.add(ReviewEdit(detector=db_user.uid, argument=argument_uid))
            DBDiscussionSession.flush()
            transaction.commit()
            db_review_edit = DBDiscussionSession.query(ReviewEdit).filter(
                ReviewEdit.detector_uid == db_user.uid,
                ReviewEdit.argument_uid == argument_uid).order_by(ReviewEdit.uid.desc()).first()
            logger('OptimizationQueue', 'New ReviewEdit with uid ' + str(db_review_edit.uid) + ' (argument)')

            for edit in argument_dict[argument_uid]:
                new_edits.append(ReviewEditValue(review_edit=db_review_edit.uid,
                                                 statement=edit['uid'],
                                                 typeof=edit['type'],
                                                 content=edit['val']))

        for statement_uid in statement_dict:
            DBDiscussionSession.add(ReviewEdit(detector=db_user.uid, statement=statement_uid))
            DBDiscussionSession.flush()
            transaction.commit()
            db_review_edit = DBDiscussionSession.query(ReviewEdit).filter(
                ReviewEdit.detector_uid == db_user.uid,
                ReviewEdit.statement_uid == statement_uid).order_by(ReviewEdit.uid.desc()).first()
            logger('OptimizationQueue', 'New ReviewEdit with uid ' + str(db_review_edit.uid) + ' (statement)')

            for edit in statement_dict[statement_uid]:
                new_edits.append(ReviewEditValue(review_edit=db_review_edit.uid,
                                                 statement=statement_uid,
                                                 typeof=edit['type'],
                                                 content=edit['val']))

        if len(new_edits) > 0:
            DBDiscussionSession.add_all(new_edits)

        # edit given, so this review is executed
        db_review.set_executed(True)
        db_review.update_timestamp()
        DBDiscussionSession.add(db_review)
        DBDiscussionSession.flush()
        transaction.commit()

    @staticmethod
    def __prepare_dicts_for_proposals(data):
        """

        :param data:
        :return:
        """
        argument_dict = {}
        statement_dict = {}
        for d in data:
            is_argument = d['argument'] > 0
            if is_argument:
                if d['argument'] in argument_dict:
                    argument_dict[d['argument']].append(d)
                else:
                    argument_dict[d['argument']] = [d]
            else:
                if d['statement'] in statement_dict:
                    statement_dict[d['statement']].append(d)
                else:
                    statement_dict[d['statement']] = [d]
        return argument_dict, statement_dict

    def add_review(self, db_user: User):
        pass

    def get_review_count(self, review_uid: int):
        db_reviews = DBDiscussionSession.query(LastReviewerOptimization).filter_by(review_uid=review_uid)
        count_of_okay = db_reviews.filter_by(is_okay=True).count()
        count_of_not_okay = db_reviews.filter_by(is_okay=False).count()

        return count_of_okay, count_of_not_okay

    def cancel_ballot(self, db_user: User, db_review: ReviewOptimization):
        """

        :param db_user:
        :param db_review:
        :return:
        """
        DBDiscussionSession.query(ReviewOptimization).get(db_review.uid).set_revoked(True)
        DBDiscussionSession.query(LastReviewerOptimization).filter_by(review_uid=db_review.uid).delete()
        db_review_canceled = ReviewCanceled(author=db_user.uid, review_data={key_optimization: db_review.uid},
                                            was_ongoing=True)

        DBDiscussionSession.add(db_review_canceled)
        DBDiscussionSession.flush()
        transaction.commit()

    def revoke_ballot(self, db_user: User, db_review: ReviewOptimization):
        """

        :param db_user:
        :param db_review:
        :return:
        """
        revoke_decision_and_implications(ReviewOptimization, LastReviewerOptimization, db_review.uid)
        db_review_canceled = ReviewCanceled(author=db_user.uid, review_data={key_optimization: db_review.uid})
        DBDiscussionSession.add(db_review_canceled)
        DBDiscussionSession.flush()
        transaction.commit()
