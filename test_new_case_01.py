import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_create_task():
    payload = {
      "content": "string",
      "user_id": "string",
      "task_id": "string",
      "is_done": False
    }

    create_response = requests.put(ENDPOINT+"/create-task", json=payload)

    assert create_response.status_code == 200

    create_data = create_response.json()
    print(create_data)
