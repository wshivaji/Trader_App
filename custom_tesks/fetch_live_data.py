from fyers_apiv3 import fyersModel
import webbrowser
from get_access_token import user_credentials
class fetch_live_data:

    def __init__(self):
        self.fyers = fyersModel.FyersModel(token=user_credentials().get_token(), is_async=False, client_id=user_credentials().get_client_id(), log_path="")


    def get_live_data(self):
        try:
            pass
        except Exception as ex:
            print(ex.args)

    def get_historical_data(self, symbol="NSE:SBIN-EQ", resolution="D", date_format="0", range_from="1622097600", range_to="1622097685", cont_flag="1"):
        try:
            """
            DATA APIS : This includes following Apis(History,Quotes,MarketDepth)
            """

            ## Historical Data

            data = {"symbol": symbol, "resolution": resolution, "date_format": date_format, "range_from": range_from,
                    "range_to": range_to, "cont_flag": cont_flag}

            print(self.fyers.history(data))

            ## Quotes

            data = {"symbols": "NSE:SBIN-EQ"}
            print(self.fyers.quotes(data))

            ## Market Depth

            data = {"symbol": "NSE:SBIN-EQ", "ohlcv_flag": "1"}
            print(self.fyers.depth(data))
        except Exception as ex:
            print(ex.args)

fetch_live_data().get_historical_data()
