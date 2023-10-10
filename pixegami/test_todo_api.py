import requests

BASE_URI = "https://todo.pixegami.io/"

response = requests.get(BASE_URI)
status_code = response.status_code
print(response)
print(status_code)

response_body = response.json()
print(response_body['message'])


def test_call_endpoint():
    res = requests.get(BASE_URI)
    assert res.status_code == 200


def test_create_task():
    payload = {
        "content": "qababuworks",
        "user_id": "qababu1",
        "is_done": False
    }
    # creating the task
    create_task_response = requests.put(BASE_URI + "/create-task", json=payload)
    print(create_task_response.status_code)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    print(data)
    # getting task id
    task_id = data['task']['task_id']
    print(task_id)
    # getting task using task id
    get_task_response = requests.get(BASE_URI + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


def test_update_task():
    payload = new_task_payload()
    # create or get the task to be updated
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_data = create_task_response.json()['task']
    task_id = task_data['task_id']
    data_using_task_id = get_task(task_id)

    # update the task
    new_payload = {"content": "updated content",
                   "user_id": payload['user_id'],
                   "task_id": task_id,
                   "is_done": True}
    # validate the update
    updated_task_response = update_task(new_payload)
    assert updated_task_response.status_code == 200

    get_task_response = get_task(task_id)
    get_task_data = get_task_response.json()

    assert get_task_data['content'] == new_payload['content']


def create_task(payload):
    return requests.put(BASE_URI + '/create-task', json=payload)


def update_task(payload):
    return requests.put(BASE_URI + '/update-task', json=payload)


def get_task(task_id):
    return requests.get(BASE_URI + f'/get-task/{task_id}')


def new_task_payload():
    return {
        "content": "actual content",
        "user_id": "qababu1",
        "is_done": True
    }
