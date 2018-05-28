import unittest

import transaction
from pyramid import testing
from pyramid.httpexceptions import HTTPNotFound

from dbas.database import DBDiscussionSession
from dbas.database.discussion_model import User
from dbas.handler.password import get_hashed_password
from dbas.helper.test import verify_dictionary_of_view
from dbas.views import main_imprint, main_news, main_discussions_overview, main_privacy, main_experiment, \
    main_notifications, main_page, main_settings, main_user


class MainImprintViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_imprint(request)
        verify_dictionary_of_view(response)

        # place for additional stuff


class MainFieldexperimentViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_experiment(request)
        verify_dictionary_of_view(response)

        # place for additional stuff


class MainMyDiscussionViewTestsNotLoggedIn(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_discussions_overview(request)
        verify_dictionary_of_view(response)

        self.assertIn('title', response)
        self.assertIn('project', response)
        self.assertIn('extras', response)
        self.assertIn('issues', response)


class MainMyDiscussionViewTestsLoggedIn(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_discussions_overview(request)
        verify_dictionary_of_view(response)

        self.assertIn('title', response)
        self.assertIn('project', response)
        self.assertIn('extras', response)
        self.assertIn('issues', response)


class MainNewsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_news(request)
        verify_dictionary_of_view(response)


class MainPrivacyViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_privacy(request)
        verify_dictionary_of_view(response)


class MainNotificationsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_notifications(request)
        verify_dictionary_of_view(response)

        # place for additional stuff


class MainPageViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_page(request)
        verify_dictionary_of_view(response)

        # place for additional stuff


class MainSettingsViewTestsNotLoggedIn(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        self.assertEqual(400, main_settings(request).status_code)


class MainSettingsViewTestsLoggedIn(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        request = testing.DummyRequest()
        response = main_settings(request)
        verify_dictionary_of_view(response)

        # check settings
        self.assertIn('send_notifications', response['settings'])
        self.assertIn('send_mails', response['settings'])
        self.assertIn('public_nick', response['settings'])


class MainSettingsViewTestsPassword(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

    def tearDown(self):
        testing.tearDown()

    def test_page_failure(self):
        request = testing.DummyRequest(params={
            'form.passwordchange.submitted': '',
            'passwordold': 'tobia',
            'password': 'tobias',
            'passwordconfirm': 'tobias'
        })
        response = main_settings(request)
        verify_dictionary_of_view(response)

        # check settings
        self.assertTrue(len(response['settings']['passwordold']) != 0)
        self.assertTrue(len(response['settings']['password']) != 0)
        self.assertTrue(len(response['settings']['passwordconfirm']) != 0)

    def test_page_success(self):
        db_user = DBDiscussionSession.query(User).filter_by(nickname='Tobias').first()
        db_user.password = get_hashed_password('tobias')
        transaction.commit()

        request = testing.DummyRequest(params={
            'form.passwordchange.submitted': '',
            'passwordold': 'tobias',
            'password': 'tobiass',
            'passwordconfirm': 'tobiass'
        })
        response = main_settings(request)
        verify_dictionary_of_view(response)

        # check settings
        self.assertTrue(len(response['settings']['passwordold']) == 0)
        self.assertTrue(len(response['settings']['password']) == 0)
        self.assertTrue(len(response['settings']['passwordconfirm']) == 0)

        db_user = DBDiscussionSession.query(User).filter_by(nickname='Tobias').first()
        db_user.password = get_hashed_password('tobias')
        transaction.commit()


class MainUserView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_chameleon')
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        db_user = DBDiscussionSession.query(User).filter_by(nickname='Tobias').first()
        db_settings = db_user.settings
        db_settings.set_show_public_nickname(True)
        transaction.commit()

    def tearDown(self):
        testing.tearDown()

    def test_page(self):
        db_user = DBDiscussionSession.query(User).filter_by(nickname='Tobias').first()

        request = testing.DummyRequest(matchdict={'uid': db_user.uid})
        response = main_user(request)
        verify_dictionary_of_view(response)
        self.assertIn('user', response)
        self.assertIn('can_send_notification', response)
        self.assertFalse(response['can_send_notification'])

    def test_page_myself(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)
        db_user = DBDiscussionSession.query(User).filter_by(nickname='Tobias').first()

        request = testing.DummyRequest(matchdict={'uid': db_user.uid})
        response = main_user(request)
        verify_dictionary_of_view(response)
        self.assertIn('user', response)
        self.assertIn('can_send_notification', response)
        self.assertFalse(response['can_send_notification'])

    def test_page_other(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)
        db_user = DBDiscussionSession.query(User).filter_by(nickname='Christian').first()

        request = testing.DummyRequest(matchdict={'uid': db_user.uid})
        response = main_user(request)
        verify_dictionary_of_view(response)
        self.assertIn('user', response)
        self.assertIn('can_send_notification', response)
        self.assertTrue(response['can_send_notification'])

    def test_page_error1(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        request = testing.DummyRequest(matchdict={'uid': 0})
        try:
            main_user(request)
        except HTTPNotFound:
            pass

    def test_page_error2(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        request = testing.DummyRequest(matchdict={'uid': 1000})
        try:
            main_user(request)
        except HTTPNotFound:
            pass

    def test_page_error3(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        request = testing.DummyRequest(matchdict={'uid1': 3})
        try:
            main_user(request)
        except HTTPNotFound:
            pass

    def test_page_error4(self):
        self.config.testing_securitypolicy(userid='Tobias', permissive=True)

        request = testing.DummyRequest(matchdict={'uid': 'a'})
        try:
            main_user(request)
        except HTTPNotFound:
            pass
