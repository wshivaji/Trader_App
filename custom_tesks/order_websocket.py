from fyers_apiv3.FyersWebsocket import order_ws
from get_access_token import user_credentials


class order_websocket:

    def __init__(self):
        # Replace the sample access token with your actual access token obtained from Fyers
        self.access_token = user_credentials().get_token()

        # Create a FyersDataSocket instance with the provided parameters
        self.fyers = order_ws.FyersOrderSocket(
            access_token=self.access_token,  # Your access token for authenticating with the Fyers API.
            write_to_file=False,  # A boolean flag indicating whether to write data to a log file or not.
            log_path="",  # The path to the log file if write_to_file is set to True (empty string means current directory).
            on_connect=self.onopen,  # Callback function to be executed upon successful WebSocket connection.
            on_close=self.onclose,  # Callback function to be executed when the WebSocket connection is closed.
            on_error=self.onerror,  # Callback function to handle any WebSocket errors that may occur.
            on_general=self.onGeneral,  # Callback function to handle general events from the WebSocket.
            on_orders=self.onOrder,  # Callback function to handle order-related events from the WebSocket.
            on_positions=self.onPosition,  # Callback function to handle position-related events from the WebSocket.
            on_trades=self.onTrade  # Callback function to handle trade-related events from the WebSocket.
        )

    def onTrade(self, message):
        """
        Callback function to handle incoming messages from the FyersDataSocket WebSocket.

        Parameters:
            message (dict): The received message from the WebSocket.

        """
        print("Trade Response:", message)

    def onOrder(self, message):
        """
        Callback function to handle incoming messages from the FyersDataSocket WebSocket.

        Parameters:
            message (dict): The received message from the WebSocket.

        """
        print("Order Response:", message)

    def onPosition(self, message):
        """
        Callback function to handle incoming messages from the FyersDataSocket WebSocket.

        Parameters:
            message (dict): The received message from the WebSocket.

        """
        print("Position Response:", message)

    def onGeneral(self, message):
        """
        Callback function to handle incoming messages from the FyersDataSocket WebSocket.

        Parameters:
            message (dict): The received message from the WebSocket.

        """
        print("General Response:", message)

    def onerror(self, message):
        """
        Callback function to handle WebSocket errors.

        Parameters:
            message (dict): The error message received from the WebSocket.


        """
        print("Error:", message)

    def onclose(self, message):
        """
        Callback function to handle WebSocket connection close events.
        """
        print("Connection closed:", message)

    def onopen(self):
        """
        Callback function to subscribe to data type and symbols upon WebSocket connection.

        """
        # Specify the data type and symbols you want to subscribe to
        # data_type = "OnOrders"
        # data_type = "OnTrades"
        # data_type = "OnPositions"
        # data_type = "OnGeneral"
        data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

        self.fyers.subscribe(data_type=data_type)

        # Keep the socket running to receive real-time data
        self.fyers.keep_running()



# Establish a connection to the Fyers WebSocket
# order_websocket().fyers.connect()

