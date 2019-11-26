from api_tests_framework.src.actions import BaseActions
from api_tests_framework.src.handlers.signup import SignupHandler
from api_tests_framework.src.handlers.validate.username import ValidateUsernameHandler
from api_tests_framework.src.handlers.user import UserHandler


class UserActions(BaseActions):
    def signup(self, username=None, password=None, firstname=None, lastname=None):
        # Send request
        response = SignupHandler(actor=self.actor).post(
            username=self.actor.username if username is None else username,
            password=self.actor.password if password is None else password,
            firstname=self.actor.firstname if firstname is None else firstname,
            lastname=self.actor.lastname if lastname is None else lastname
        )

        # Parse model
        model = response.json()

        return model

    def validate_username(self, username=None):
        # Send request
        response = ValidateUsernameHandler(actor=self.actor).get(
            username=self.actor.username if username is None else username
        )

        # Parse model
        model = response.json()

        return model

    def user(self):
        # Send request
        response = UserHandler(actor=self.actor).get()

        # Parse model
        model = response.json()

        return model