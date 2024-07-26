from fyers_apiv3 import fyersModel

from user_credentials import user_credentials


class fetch_data:

    def __init__(self):
        print(user_credentials().get_redirect_uri())

        ## Once you have generated accessToken now we can call multiple trading related or data related apis after that in order to do so we need to first initialize the fyerModel object with all the requried params.
        """
        fyerModel object takes following values as arguments
        1. accessToken : this is the one which you received from above 
        2. client_id : this is basically the app_id for the particular app you logged into
        """
        fyers = fyersModel.FyersModel(token=user_credentials().get_token(), is_async=False, client_id=user_credentials().get_client_id(), log_path="")

        ## After this point you can call the relevant apis and get started with

        #######################################################################################################

        ####################################################################################################################
        """
        1. User Apis : This includes (Profile,Funds,Holdings)
        """

        print(fyers.get_profile())  ## This will provide us with the user related data

        print(fyers.funds())  ## This will provide us with the funds the user has

        print(fyers.holdings())  ## This will provide the available holdings the user has

        ########################################################################################################################

        """
        2. Transaction Apis : This includes (Tradebook,Orderbook,Positions)
        """

        print(fyers.tradebook())  ## This will provide all the trade related information

        print(fyers.orderbook())  ## This will provide the user with all the order realted information

        print(fyers.positions())  ## This will provide the user with all the positions the user has on his end

        ######################################################################################################################


fetch_data()

