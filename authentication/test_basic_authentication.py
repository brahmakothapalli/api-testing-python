import requests

BASE_URI = "https://postman-echo.com/basic-auth"
header ={
    'Content-Type': 'application/json',
    'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='
}
credentials = ('postman', 'password') # username and password as a tuple

def test_basic_auth_using_token():
    '''testing basic auth using '''
    response = requests.get(BASE_URI, headers=header)
    print(response.text)
    status = response.status_code
    print(f"\nStatus Code is {status}")
    if status == 200:
        print("Authentication successful")
    else:   
        print("Authentication failed")

def test_basic_auth():
    '''testing basic auth using '''
    response = requests.get(BASE_URI, auth=credentials)
    print(response.text)
    status = response.status_code
    print(f"\nStatus Code is {status}")
    if status == 200:
        print("Authentication successful")
    else:
        print("Authentication failed")