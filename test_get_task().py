import requests

API = "https://todo.pixegami.io/"

def test_get_task():
    payload = {
        "content": "string",
        "user_id": "string",
        "task_id": "string",
        "is_done": False
        }

    create_response = requests.put(API+"/create-task", json=payload)

    assert create_response.status_code == 200

    create_data = create_response.json()
    print(create_data)

    task_id = create_data["task"]["task_id"]
    # task = dictionary
    # task_id = from task object

    get_response = requests.get(API+f"get-task/{task_id}")

    assert get_response.status_code == 200

    get_data = get_response.json()
    print(get_data)

    assert get_data["content"] == payload["content"]
    assert get_data["user_id"] == payload["user_id"]