from get_access_token import user_credentials
from fyers_apiv3 import fyersModel


class place_order:

    def __init__(self):
        self.fyers = fyersModel.FyersModel(token=user_credentials().get_token(), is_async=False, client_id=user_credentials().get_client_id(), log_path="")

    def place_single_order(self, symbol='NSE:ONGC-EQ', quantity=1, type=1, side=1, product_type='INTRADAY', limit_price=0, sl_price=0, validity='DAY', disclose_quantity=1, offline_order=False, stoploss=0, take_profit=0):
        try:
            ## SINGLE ORDER

            data = {
                "symbol": symbol,
                "qty": quantity,
                "type": type,
                "side": side,
                "productType": product_type,
                "limitPrice": limit_price,
                "stopPrice": sl_price,
                "validity": validity,
                "disclosedQty": disclose_quantity,
                "offlineOrder": offline_order,
                "stopLoss": stoploss,
                "takeProfit": take_profit
            }  ## This is a sample example to place a limit order you can make the further changes based on your requriements

            print(self.fyers.place_order(data))
        except Exception as ex:
            print(ex.args)

    def place_multi_order(self):
        try:
            ## MULTI ORDER

            data = [{"symbol": "NSE:SBIN-EQ",
                     "qty": 1,
                     "type": 1,
                     "side": 1,
                     "productType": "INTRADAY",
                     "limitPrice": 61050,
                     "stopPrice": 0,
                     "disclosedQty": 0,
                     "validity": "DAY",
                     "offlineOrder": False,
                     "stopLoss": 0,
                     "takeProfit": 0
                     },
                    {
                        "symbol": "NSE:HDFC-EQ",
                        "qty": 1,
                        "type": 2,
                        "side": 1,
                        "productType": "INTRADAY",
                        "limitPrice": 0,
                        "stopPrice": 0,
                        "disclosedQty": 0,
                        "validity": "DAY",
                        "offlineOrder": False,
                        "stopLoss": 0,
                        "takeProfit": 0
                    }]  ### This takes input as a list containing multiple single order data into it and the execution of the orders goes in the same format as mentioned.

            print(self.fyers.place_basket_orders(data))
        except Exception as ex:
            print(ex.args)

    def place_multi_leg_order(self):
        try:
            ## MULTILEG ORDER

            data = {
                "orderTag": "tag1",
                "productType": "MARGIN",
                "offlineOrder": False,
                "orderType": "3L",
                "validity": "IOC",
                "legs": {
                    "leg1": {
                        "symbol": "NSE:SBIN24JUNFUT",
                        "qty": 750,
                        "side": 1,
                        "type": 1,
                        "limitPrice": 800
                    },
                    "leg2": {
                        "symbol": "NSE:SBIN24JULFUT",
                        "qty": 750,
                        "side": 1,
                        "type": 1,
                        "limitPrice": 800
                    },
                    "leg3": {
                        "symbol": "NSE:SBIN24JUN900CE",
                        "qty": 750,
                        "side": 1,
                        "type": 1,
                        "limitPrice": 3
                    }
                }
            }  ### This is a sample data structure used to place an 3 leg order using multileg order api .you can make the further changes based on your requriements

            print(self.fyers.place_multileg_order(data))
        except Exception as ex:
            print(ex.args)

    def modify_order(self, id='1234567', type=1, limit_price=500, quantity=1):
        try:
            ## Modify_order request
            data = {
                "id": id,
                "type": type,
                "limitPrice": limit_price,
                "qty": quantity
            }
            print(self.fyers.modify_order(data))
        except Exception as ex:
            print(ex.args)

    def modify_multi_order(self, *args):
        try:
            ## Modify Multi Order

            data = [
                {"id": "8102710298291",
                 "type": 1,
                 "limitPrice": 61049,
                 "qty": 0
                 },
                {
                    "id": "8102710298292",
                    "type": 1,
                    "limitPrice": 61049,
                    "qty": 1
                }]

            print(self.fyers.modify_basket_orders(data))
        except Exception as ex:
            print(ex.args)


    def cancle_order(self, order_id):
        try:
            ### Cancel_order
            data = {"id": order_id}
            print(self.fyers.cancel_order(data))


        except Exception as ex:
            print(ex.args)

    def cancle_multi_order(self, *args):
        try:
            ### cancel_multi_order
            data = [
                {
                    "id": '808058117761'
                },
                {
                    "id": '808058117762'
                }]
            print(self.fyers.cancel_basket_orders(data))
        except Exception as ex:
            print(ex.args)

    def exit_position(self, order_id):
        try:
            ### Exit Position
            data = {
                "id": order_id
            }
            print(self.fyers.exit_positions(data))
        except Exception as ex:
            print(ex.args)


    def convert_position(self, symbol="MCX:SILVERMIC20NOVFUT", position_side=1, convert_quantity=1, convert_from='INTRADAY', convert_to='CNC'):
        try:
            ### Convert Position

            data = {
                "symbol": symbol,
                "positionSide": position_side,
                "convertQty": convert_quantity,
                "convertFrom": convert_from,
                "convertTo": convert_to
            }

            print(self.fyers.convert_position(data))
        except Exception as ex:
            print(ex.args)

    # place_order().single_order()



