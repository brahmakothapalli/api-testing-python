import requests

BASE_URI = "https://reqres.in"
header = {'Content-Type': 'application/json'}

payload = {
    "name": "morpheus 2",
    "job": "leader 2"
}


def test_create_resource():
    """ creating a resource with payload """
    END_POINT = "/api/users"
    res = requests.post(BASE_URI + END_POINT, headers=header, json=payload)
    print(f"status code is {res.status_code}")
    response_data = res.json()
    print(response_data)
    print(f"name of the resource is {response_data['name']} and the id is {response_data['id']}")
