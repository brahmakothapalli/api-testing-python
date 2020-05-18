import requests
from requests.auth import HTTPBasicAuth


class TestAuthenticationInRequests:

    base_uri = "https://api.github.com/user"

    def test_basic_auth(self):
        res = requests.get(self.base_uri, auth=HTTPBasicAuth('user', 'pass'))
        print(res.status_code)
        # or
        res = requests.get(self.base_uri, auth=('user', 'pass'))
        print(res.status_code)
