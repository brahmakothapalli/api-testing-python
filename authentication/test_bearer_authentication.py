import requests

BASE_URI = "https://gorest.co.in"    # base url

END_POINT = "/public/v2/users"  # end point url

Token = "Bearer 4fb7dc4bdf2753074cb24479061d15da39ce2ff4701a9d831d41e470f27a1fb4"   # bearer token generated

header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 4fb7dc4bdf2753074cb24479061d15da39ce2ff4701a9d831d41e470f27a1fb4'
} # added authorization in the header with the given bearer token

response = requests.get(BASE_URI+END_POINT, headers=header)  # passing the token to the get request method

print(f'\nThe status code is - {response.status_code}')
print(f'The response {response.json()}')