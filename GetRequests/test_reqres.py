import requests


class TestGetRequests:

    base_uri = "https://reqres.in/api/users"

    def test_get_all_users(self):
        response = requests.get(self.base_uri)
        print(response)

    def test_validate_status_code(self):
        response = requests.get(self.base_uri)
        print(response.status_code)
        assert response.status_code == 200

    def test_print_response_different_forms(self):
        response = requests.get(self.base_uri)
        print("Text data Format: \n")
        print(response.text)
        print("JSON data Format: \n")
        print(response.json())
        print("Raw data Format: \n")
        print(response.json())

    def test_print_header_history(self):
        res = requests.get(self.base_uri)
        print('\nHistory ----', res.history)
        print('\nHeaders', res.headers)
        print('\nDate -- ', res.headers['Date'])
        print('\nContent Type -- ', res.headers['Content-Type'])
