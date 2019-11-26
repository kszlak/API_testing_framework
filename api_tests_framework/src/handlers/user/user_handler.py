from api_tests_framework.src.handlers import BaseHandler


class UserHandler( BaseHandler ):
    def get(self):

        # Send request
        response = self._get(
            url="/user"
        )

        return response