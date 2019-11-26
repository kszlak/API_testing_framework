from api_tests_framework.utils.unittest_wrappers import ModelValidationTestCase
from api_tests_framework.src.handlers.signup import SignupHandler
from api_tests_framework.src.actions.user import UserActions
from api_tests_framework.src.actors import Actor
from api_tests_framework.utils.errors import http_exceptions
from uuid import uuid4


class SignupTestSuite(ModelValidationTestCase):
    def setUp(self):

        self.actor = Actor()

    def test_signup_with_correct_credentials(self):
        user_model = UserActions(actor=self.actor).signup()

        self.assertUserModel(user_model)

    def test_sign_up_with_incorrect_username(self):
        with self.assertRaises(http_exceptions.UnprocessableEntity):
            UserActions(actor=self.actor).signup(
                username="4666"
            )

    def test_sign_up_with_incorrect_password_too_long(self):
        with self.assertRaises(http_exceptions.UnprocessableEntity):
            UserActions(actor=self.actor).signup(
                password=uuid4().hex[0:21]
            )


    def test_sign_up_with_incorrect_password_too_short(self):
        with self.assertRaises(http_exceptions.UnprocessableEntity):
            UserActions(actor=self.actor).signup(
                password=uuid4().hex[0:1]
            )


    """def test_sign_up_with_incorrect_password(self):
        req = SignupHandler( actor=self.actor ).post(
            username = "Nelka",
            password=self.actor.password,
            firstname=self.actor.firstname,
            lastname=self.actor.lastname
        )

        print (req.content)
        response3 = req.json()

        # Assert already existing username
        self.assertIn("Username already taken", response3["message"])"""