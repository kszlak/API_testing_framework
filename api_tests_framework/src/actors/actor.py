from requests import session
from uuid import uuid4

class Actor(object):
    def __init__(self):
        self.session = session()

        #Generate actor details
        self.firstname = uuid4().hex[:20]
        self.lastname = uuid4().hex[:20]
        self.username = uuid4().hex[:20]
        self.password = uuid4().hex[:20]