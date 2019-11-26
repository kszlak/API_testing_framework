from api_tests_framework.src.handlers import BaseHandler


class SignupHandler(BaseHandler):
    def post(self, username, password, firstname, lastname):

        # Create payload
        json = {
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname
        }
        # Send request
        response = self._post(
            url="/signup",
            json=json
        )

        return response




