from user_credentials import user_credentials


class fetch_data:

    def __init__(self):
        print(user_credentials().get_redirect_uri())

fetch_data()

