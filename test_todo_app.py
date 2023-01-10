import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    # check here (only pass this test, if the status code is 200)
    assert response.status_code == 200