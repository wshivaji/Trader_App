from pathlib import Path
import json

# JSON_FILE = f"{Path(__file__).parent.parent}\\Application Settings\\login_credentials.json"
# open_json_file = open(JSON_FILE)
# print(JSON_FILE)
# x = json.load(open_json_file)
# print(x['user1']['redirect_uri'])

class user_credentials:

    def __init__(self):
        self.JSON_FILE = f"{Path(__file__).parent.parent}\\Application Settings\\login_credentials.json"
        self.open_json_file = open(self.JSON_FILE)
        self.x = json.load(self.open_json_file)
        self.open_json_file.close()

    def get_user_credentials(self):
        try:
            # print(self.x)
            self.redirect_uri = self.x['user1']['redirect_uri']
            self.client_id = self.x['user1']['client_id']
            self.secret_key = self.x['user1']['secret_key']
            self.grant_type = self.x['user1']['grant_type']
            self.response_type = self.x['user1']['response_type']
            self.state = self.x['user1']['state']
        except Exception as ex:
            print(ex.args)

    def get_redirect_uri(self):
        try:
            return self.x['user1']['redirect_uri']
        except Exception as ex:
            print(ex.args)

    def get_client_id(self):
        try:
            return self.x['user1']['client_id']
        except Exception as ex:
            print(ex.args)

    def get_secret_key(self):
        try:
            return self.x['user1']['secret_key']
        except Exception as ex:
            print(ex.args)

    def get_grant_type(self):
        try:
            return self.x['user1']['grant_type']
        except Exception as ex:
            print(ex.args)

    def get_response_type(self):
        try:
            return self.x['user1']['response_type']
        except Exception as ex:
            print(ex.args)

    def get_state(self):
        try:
            return self.x['user1']['state']
        except Exception as ex:
            print(ex.args)

    def get_token(self):
        try:
            return self.x['user1']['token']
        except Exception as ex:
            print(ex.args)

    def set_redirect_uri(self, redirect_uri):
        try:
            self.x['user1']['redirect_uri'] = redirect_uri
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_client_id(self, client_id):
        try:
            self.x['user1']['client_id'] = client_id
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_secret_key(self, secret_key):
        try:
            self.x['user1']['secret_key'] = secret_key
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_grant_type(self, grant_type):
        try:
            self.x['user1']['grant_type'] = grant_type
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_response_type(self, response_type):
        try:
            self.x['user1']['response_type'] = response_type
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_state(self, state):
        try:
            self.x['user1']['state'] = state
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

    def set_token(self, token):
        try:
            self.x['user1']['token'] = token
            with open(self.JSON_FILE, 'w') as f:
                json.dump(self.x, f)
        except Exception as ex:
            print(ex.args)

#user_credentials().set_redirect_uri("https://www.google.com/")
# print(user_credentials().get_redirect_uri())
# print(user_credentials().get_response_type())
