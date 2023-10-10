import requests


class TestJsonPlaceHolder:
    BASE_URI = "https://jsonplaceholder.typicode.com/posts"

    def test_simple_get_request(self):
        response = requests.get(self.BASE_URI)
        response_data = response.json()
        print(response_data[0]['title'])
        print(len(response_data))

    def test_get_request_with_query_param(self):
        response = requests.get(self.BASE_URI + "?userId=1&id=5")
        response_data = response.json()
        print(response_data)
        print(type(response_data))

    def test_get_request_with_query_params(self):
        query_params = {
            "userId": 1,
            "id": 7
        }
        response = requests.get(self.BASE_URI, params=query_params)
        response_data = response.json()
        print(response_data)
        print(response_data[0]['title'])
        print(type(response_data))
