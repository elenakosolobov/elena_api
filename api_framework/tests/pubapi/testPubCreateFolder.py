from pubapiutils import Calls
from pubapiutils import Config
from pubapiutils import Utils
import httplib


class TestClass:
    def __init__(self):
        self.no_json = 'NoJSON'
        self.calls = Calls()
        self.config = Config()
        self.utils = Utils()

    def test_create_5_folders_positive(self):
        l = []
        for i in range(5):
            folder_name = self.utils.random_name()
            resp = self.calls.create_folder(folder_name)
            assert resp.status_code == httplib.CREATED
            assert resp.json == self.no_json
            l.append(folder_name)
        for item in l:
            resp = self.calls.delete_folder(folder_path=self.config.testpath + item)
            assert resp.status_code == httplib.OK

    def test_create_folder_enough_perms(self):
        folder1 = self.utils.random_name()
        folder2 = self.utils.random_name()
        perms = ['Editor', 'Full', 'Owner']
        for perm in perms:
            folder_path = '%s/%s' % (self.config.testpath, folder1)
            self.calls.create_folder(folder1)
            resp = self.calls.set_perms(folder_path=folder_path, users=self.config.puser, permission=perm)
            assert resp.status_code == httplib.OK
            resp = self.calls.list_perms(folder_path=folder_path, users=self.config.puser)
            assert resp.status_code == httplib.OK
            assert resp.json['users'][0]['permission'] == perm
            assert resp.json['users'][0]['subject'] == self.config.puser
            assert len(resp.json['groups']) == 0
            resp = self.calls.create_folder(folder2, path=folder_path, username=self.config.puser)
            assert resp.status_code == httplib.CREATED
            assert resp.json == self.no_json
            self.calls.delete_folder(folder_path)