from api_tests_framework.src.handlers import BaseHandler


class ValidateUsernameHandler( BaseHandler ):
    def get(self, username):

        params = {"username": username}
        # Send request
        response = self._get(
            url="/validate/username",
            params=params
        )

        return response
