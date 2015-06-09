__author__ = 'elena'
import requests
import json


def create_folder(folder_name, path=None, domain=None, method=None, content_type=None, accept=None,
                  username=None, password=None):
    if domain is None:
        domain = 'https://istepanko27.qa-egnyte.com'
    if method is None:
        method = 'POST'
    if content_type is None:
        content_type = 'application/json'
    if accept is None:
        accept = 'application/json'
    if username is None:
        username = 'admin'
    if password is None:
        password = '12345678'
    if path is None:
        path = '/Shared/elena_test1'

    endpoint = '/public-api/v1/fs'
    url = '%s%s%s%s' % (domain, endpoint, path, folder_name)
    headers = dict()
    headers['Content-Type'] = content_type
    headers['Accept'] = accept
    data = dict()
    data['action'] = 'add_folder'
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

    r.json = json_resp
    return r