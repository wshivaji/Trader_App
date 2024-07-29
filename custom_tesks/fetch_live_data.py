from fyers_apiv3 import fyersModel
import webbrowser
from get_access_token import user_credentials
from datetime import datetime
import pandas as pd
import json


class fetch_live_data:

    def __init__(self):
        self.fyers = fyersModel.FyersModel(token=user_credentials().get_token(), is_async=False, client_id=user_credentials().get_client_id(), log_path="")


    def get_live_data(self):
        try:
            pass
        except Exception as ex:
            print(ex.args)

    def get_historical_data(self, symbol="NSE:SBIN-EQ", resolution="D", date_format="0", range_from="1704125534", range_to="1722269534", cont_flag="1"):
        try:
            """
            DATA APIS : This includes following Apis(History,Quotes,MarketDepth)
            """

            ## Historical Data

            data = {"symbol": symbol, "resolution": resolution, "date_format": date_format, "range_from": range_from,
                    "range_to": range_to, "cont_flag": cont_flag}
            print(type(self.fyers.history(data)))
            print(self.fyers.history(data))
            historical_data = (self.fyers.history(data))
            f_name = f"{symbol[4:]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            print(f_name)
            df = pd.DataFrame(historical_data['candles'], columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
            print(df)
            df.to_csv(f_name)
            ## Quotes

            data = {"symbols": "NSE:SBIN-EQ"}
            print(self.fyers.quotes(data))

            ## Market Depth

            data = {"symbol": "NSE:SBIN-EQ", "ohlcv_flag": "1"}
            print(self.fyers.depth(data))
        except Exception as ex:
            print(ex.args)

# fetch_live_data().get_historical_data()
