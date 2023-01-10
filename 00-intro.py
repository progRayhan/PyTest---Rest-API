import requests

ENDPOINT = "https://todo.pixegami.io/"

response = requests.get(ENDPOINT)
print(response)
# <Response [200]>

data = response.json()
print(data)
# {'message': 'Hello World from Todo API'}

status_code = response.status_code
print(status_code)
# 200