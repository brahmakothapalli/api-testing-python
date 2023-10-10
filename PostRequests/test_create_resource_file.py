import requests
import json

BASE_URI = "https://reqres.in"
header = {'Content-Type': 'application/json'}
json_file = open("./my_payload.json", mode="r")
payload = json.load(json_file)
# print("content--------> ", payload)


def test_create_resource():
    """ creating a resource with payload from file"""
    END_POINT = "/api/users"
    # res = requests.post(BASE_URI + END_POINT, headers=header, json=payload)
    res = requests.post(BASE_URI + END_POINT, headers=header, data=json.dumps(payload))
    print(f"status code is {res.status_code}")
    response_data = res.json()
    print(response_data)
    print(f"name of the resource is {response_data['name']} and the id is {response_data['id']}")
