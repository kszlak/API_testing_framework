from os import environ
from api_tests_framework.utils.errors.http_exceptions import from_status_code
from requests.auth import HTTPBasicAuth


class BaseHandler(object):
    def __init__(self, actor):
        self._base_url = environ.get("BASE_URL") or "http://18.195.251.80:5000"
        self._timeout = 10
        self.actor = actor

    def _make_request(self, url, method,
                        params=None, files=None, json=None, timeout=None,
                        headers =None, cookies=None, **kwargs):
        if timeout is None:
            timeout = self._timeout
        # Prepared forward slash if, for example, api/user is provided instead of /api/user
        if not url.startswith("/"):
            url = "/" + url

        # Send request
        response = self.actor.session.request(
            url=self._base_url + url,
            method=method,
            params=params,
            files=files,
            json=json,
            timeout=timeout,
            headers=headers,
            cookies=cookies,
            **kwargs
        )

        # Verify status code
        if response.status_code != 200:
            raise from_status_code( status_code=response.status_code, msg=response.content )

        # Authorize user after signup
        if url == "/signup":
            self.actor.session.auth = HTTPBasicAuth(username=self.actor.username, password=self.actor.password)

        return response

    def _get(self, url, params=None, headers=None, cookies=None):
        return self._make_request(
            method="GET",
            url=url,
            params=params,
            headers=headers,
            cookies=cookies
        )

    def _post(self, url, params=None, json=None, files=None, headers=None, cookies=None):
        return self._make_request(
            method="POST",
            url=url,
            params=params,
            json=json,
            files=files,
            headers=headers,
            cookies=cookies
        )

    def _delete(self, url, headers=None, cookies=None):
        return self._make_request(
            method="DELETE",
            url=url,
            headers=headers,
            cookies=cookies
        )