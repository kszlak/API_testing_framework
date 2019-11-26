from api_tests_framework.utils.unittest_wrappers import ModelValidationTestCase
from api_tests_framework.src.handlers.validate.username import ValidateUsernameHandler
from api_tests_framework.src.actors import Actor
from api_tests_framework.src.actions.user import UserActions
from uuid import uuid4


class ValidateTestSuite(ModelValidationTestCase):
    def setUp(self):
        self.actor = Actor()

    def test_validate_username(self):
        username_validation_model = UserActions(actor=self.actor).validate_username()

        self.assertUsernameValidationModel(username_validation_model)
