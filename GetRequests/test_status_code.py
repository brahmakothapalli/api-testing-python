import requests

base_uri = "https://reqres.in/api/users?page=2"
response = requests.get(base_uri)
# printing the status code 
print(response.status_code)
# asserting the status code
assert response.status_code is 200
