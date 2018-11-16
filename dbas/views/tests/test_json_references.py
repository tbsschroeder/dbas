import unittest

import transaction
from pyramid import testing

from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import StatementReferences, StatementToIssue
from dbas.views import set_references, get_reference


class AjaxReferencesTest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        # test every ajax method, which is not used in other classes


    def test_get_references_empty(self):
        from dbas.views import get_reference as ajax
        request = testing.DummyRequest(json_body={
            'uids': [14],
            'is_argument': False
        })
        response = ajax(request)
        self.assertIsNotNone(response)
        for uid in response['data']:
            self.assertTrue(len(response['data'][uid]) == 0)
            self.assertTrue(len(response['text'][uid]) != 0)

    def test_get_references(self):
        from dbas.views import get_reference as ajax
        request = testing.DummyRequest(json_body={
            'uids': [15],
            'is_argument': False
        })
        response = ajax(request)
        self.assertIsNotNone(response)
        for uid in response['data']:
            self.assertTrue(len(response['data'][uid]) != 0)
            self.assertTrue(len(response['text'][uid]) != 0)

    def test_get_references_failure(self):
        from dbas.views import get_reference as ajax
        request = testing.DummyRequest(json_body={
            'uids': 'ab',
            'is_argument': False
        })
        response = ajax(request)
        self.assertIsNotNone(response)
        self.assertEqual(400, response.status_code)

    def test_set_references(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)
        issue_uid = DBDiscussionSession.query(StatementToIssue).filter_by(statement_uid=17).first().issue_uid
        request = testing.DummyRequest(json_body={
            'statement_id': 17,
            'issue': issue_uid,
            'reference': 'This is a source',
            'ref_source': 'http://www.google.de/some_source',
        })
        self.assertTrue(set_references(request))

        request = testing.DummyRequest(json_body={
            'uids': [17],
            'is_argument': False
        })
        response = get_reference(request)
        self.assertIsNotNone(response)
        for uid in response['data']:
            self.assertTrue(17, uid)
            self.assertTrue(len(response['data'][uid]) != 0)
            self.assertTrue(len(response['text'][uid]) != 0)

        DBDiscussionSession.query(StatementReferences).filter_by(statement_uid=17).delete()
        transaction.commit()
