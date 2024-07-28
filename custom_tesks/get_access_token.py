from fyers_apiv3 import fyersModel
import webbrowser
from user_credentials import user_credentials
"""
In order to get started with Fyers API we would like you to do the following things first.
1. Checkout our API docs :   https://myapi.fyers.in/docsv3
2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/

Once you have created an APP you can start using the below SDK 
"""

#### Generate an authcode and then make a request to generate an accessToken (Login Flow)

"""
1. Input parameters
"""
class generate_auth_code_and_access_token:

    def __init__(self):

        self.redirect_uri= user_credentials().get_redirect_uri()  ## redircet_uri you entered while creating APP.
        self.client_id = user_credentials().get_client_id()                      ## Client_id here refers to APP_ID of the created app
        self.secret_key = user_credentials().get_secret_key()                         ## app_secret key which you got after creating the app
        self.grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
        self.response_type = "code"                             ## The response_type always has to be "code"
        self.state = "sample"                                   ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code

        self.appSession = fyersModel.SessionModel(client_id=self.client_id, redirect_uri=self.redirect_uri,
                                             response_type=self.response_type, state=self.state, secret_key=self.secret_key,
                                             grant_type=self.grant_type)

    def generate_auth_code(self):
        ### Connect to the sessionModel object here with the required input parameters
        # ## Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code
        generateTokenUrl = self.appSession.generate_authcode()

        """There are two method to get the Login url if  you are not automating the login flow
        1. Just by printing the variable name 
        2. There is a library named as webbrowser which will then open the url for you without the hasel of copy pasting
        both the methods are mentioned below"""
        print((generateTokenUrl))
        webbrowser.open(generateTokenUrl, new=1)

        """
        run the code firstly upto this after you generate the auth_code comment the above code and start executing the below code """
        ##########################################################################################################################

    def get_access_token(self):
        try:
            auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MjIxODczOTQsImV4cCI6MTcyMjIxNzM5NCwibmJmIjoxNzIyMTg2Nzk0LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzYwMDcyIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDk1ZWU2YWNhYjJlZjQ1NjdmMzc1NWU4MjBlNmZmOGFiMDlkN2Y3YmQwOTRlNzFmYzg0M2NmZGUiLCJub25jZSI6IiIsImFwcF9pZCI6IjRKSU5BT0E0NUUiLCJ1dWlkIjoiMzU0ZDk1ZmUzMmNkNGI3Njg4Y2QxYmZhN2EyYTg1NWYiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.Z98sU3TmAcHxJVtS14Gw35VpdR2NFBjyD0VQzqMZlmw"
            self.appSession.set_token(auth_code)
            response = self.appSession.generate_token()
            print(response['access_token'])
            user_credentials().set_token(response['access_token'])
        except Exception as ex:
            print(ex.args)

# generate_auth_code_and_access_token().generate_auth_code()

# https://www.google.com/?s=ok&code=200&auth_code=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MjIxODczOTQsImV4cCI6MTcyMjIxNzM5NCwibmJmIjoxNzIyMTg2Nzk0LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzYwMDcyIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDk1ZWU2YWNhYjJlZjQ1NjdmMzc1NWU4MjBlNmZmOGFiMDlkN2Y3YmQwOTRlNzFmYzg0M2NmZGUiLCJub25jZSI6IiIsImFwcF9pZCI6IjRKSU5BT0E0NUUiLCJ1dWlkIjoiMzU0ZDk1ZmUzMmNkNGI3Njg4Y2QxYmZhN2EyYTg1NWYiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.Z98sU3TmAcHxJVtS14Gw35VpdR2NFBjyD0VQzqMZlmw&state=sample

# generate_auth_code_and_access_token().get_access_token()
