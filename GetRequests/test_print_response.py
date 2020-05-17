import requests

base_uri = "https://reqres.in/api/users?page=2"
response = requests.get(base_uri)
# printing response body
print(response.content)
# printing response body using json() method
print(response.json())