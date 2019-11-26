from api_tests_framework.utils.unittest_wrappers import ModelValidationTestCase
from api_tests_framework.src.handlers.user import UserHandler
from api_tests_framework.src.actions.user import UserActions
from api_tests_framework.src.actors import Actor
from api_tests_framework.utils.errors import http_exceptions


class ValidateTestSuite(ModelValidationTestCase):
    def setUp(self):
        self.actor = Actor()

    def test_user(self):
        with self.assertRaises( http_exceptions.Unauthorized ):
            UserActions( actor=self.actor ).user()

        #sign up and then make call