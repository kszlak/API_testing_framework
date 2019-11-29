http_exceptions = dict()

def add_http_exception(cls):
    def wrapper():
        http_exceptions[cls.status_code] = cls
    wrapper()
    return cls

def from_status_code(status_code, msg):
    exception_cls = http_exceptions.get(status_code, HttpException)
    return exception_cls(msg=msg)

class HttpException(Exception):
    status_code="Unknown"

    def __init__(self, msg=""):
        self.msg=msg

    def __str__(self):
        return "{status_code} {msg}".format(status_code=self.status_code, msg=self.msg)


@add_http_exception
class UnprocessableEntity(HttpException):
    status_code = 422

@add_http_exception
class Unauthorized( HttpException ):
    status_code = 401

@add_http_exception
class Bad_request( HttpException ):
    status_code = 402
