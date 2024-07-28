from fyers_apiv3.FyersWebsocket import data_ws
from user_credentials import user_credentials


class data_web_socket:

    def __init__(self):
        # Replace the sample access token with your actual access token obtained from Fyers
        self.access_token = user_credentials().get_token()
        # Create a FyersDataSocket instance with the provided parameters
        self.fyers = data_ws.FyersDataSocket(
            access_token=self.access_token,  # Access token in the format "appid:accesstoken"
            log_path="",  # Path to save logs. Leave empty to auto-create logs in the current directory.
            litemode=False,  # Lite mode disabled. Set to True if you want a lite response.
            write_to_file=False,  # Save response in a log file instead of printing it.
            reconnect=True,  # Enable auto-reconnection to WebSocket on disconnection.
            on_connect=self.onopen,  # Callback function to subscribe to data upon connection.
            on_close=self.onclose,  # Callback function to handle WebSocket connection close events.
            on_error=self.onerror,  # Callback function to handle WebSocket errors.
            on_message=self.onmessage  # Callback function to handle incoming messages from the WebSocket.
        )

    def fetch_live_data_with_websocket(self):
        try:
            # Establish a connection to the Fyers WebSocket
            self.fyers.connect()
        except Exception as ex:
            print(ex.args)

    def onmessage(self, message):
        """
        Callback function to handle incoming messages from the FyersDataSocket WebSocket.

        Parameters:
            message (dict): The received message from the WebSocket.

        """
        print("Response:", message)

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
        # self.fyers.unsubscribe()
        print("Connection closed:", message)

    def onopen(self, symbols=['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ'], data_type="symbolData"):
        """
        Callback function to subscribe to data type and symbols upon WebSocket connection.

        """
        # Specify the data type and symbols you want to subscribe to
        data_type = data_type
        # data_type = "DepthUpdate"/"symbolData"

        # Subscribe to the specified symbols and data type
        symbols = symbols
        self.fyers.subscribe(symbols=symbols, data_type=data_type)

        # Keep the socket running to receive real-time data
        self.fyers.keep_running()

# data_web_socket().fetch_live_data_with_websocket()

