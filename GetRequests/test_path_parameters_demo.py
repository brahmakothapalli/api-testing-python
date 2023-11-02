import requests
from pprint import pprint

class TestPathParametersDemo:

    # https://gorest.co.in/public/v2/users/{id} - sample url with path parameter
    BASE_URI = 'https://gorest.co.in/public/v2'
    ENDPOINT = '/users'

    path_params = {
        'id':5632444
    }
    # sending path parameter using dictionary
    def test_sending_path_parameter(self):        
        request_url = self.BASE_URI+self.ENDPOINT
        response = requests.get(request_url, params=self.path_params) # sending api request by adding the BASE URI, Endpoint, Path parameter
        print(f"\nRequest status code is {response.status_code}")
        data = response.json()
        pprint(data)