import requests
# this test prints the header of the response and how to fetch the different attributes from header
base_uri = "https://reqres.in/api/users?page=2"
response = requests.get(base_uri)
# print(response.headers)
print('Date ---->', response.headers['Date'])
print('Content-Type ----->', response.headers['Content-Type'])