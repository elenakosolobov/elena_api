import requests
import json

method = 'DELETE'
url = 'https://istepanko27.qa-egnyte.com/public-api/v1/fs/Shared/elena_test1'
headers = dict()
headers['Content-Type'] = 'application/json'
data = dict()
data['action'] = 'add_folder'
username = 'admin'
password = '12345678'

data = json.dumps(data)

r = requests.request(
    method=method,
    url=url,
    headers=headers,
    data=data,
    auth=(username, password)
)

try:
    json_resp = json.loads(r.content)
except ValueError:
    json_resp = 'NoJSON'

print(json_resp)
print()
print(r.status_code)
print()
print(r.headers)