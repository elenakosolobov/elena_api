import pubapiutils
import httplib


def test_create_100_folders_positive():
    no_json = 'NoJSON'
    for i in range(5):
        folder_name = 'test_folder123%s' % i
        resp = pubapiutils.create_folder(folder_name)
        assert resp.status_code == httplib.CREATED
        assert resp.json == no_json


def test_create_folders_positive():
    no_json = 'NoJSON'
    for i in range(3):
        folder_name = 'test_folder123gtg%s' % i
        resp = pubapiutils.create_folder(folder_name)
        print resp.status_code
        assert resp.status_code == httplib.CREATED
        assert resp.json == no_json


test_create_folders_positive()
