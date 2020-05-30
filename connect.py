from algosdk import algod

# Setup HTTP client w/guest key provided by PureStake
class Connect():
    def __init__(self):
        self.algod_address = "https://testnet-algorand.api.purestake.io/ps1"# declaring the third party API
        self.algod_token = "eVXi2wPlDE8u" # <-----shortened - my personal API token
        self.headers = {"X-API-Key": self.algod_token}

    def connectToNetwork(self):       
        # establish connection
        connecting = algod.AlgodClient(self.algod_token, self.algod_address, self.headers)
        return connecting


# curl -X GET "https://testnet-algorand.api.purestake.io/ps1/versions" -H "x-api-key:eVXi2wPlDE8uF15mkil5Z2FzRm20GTJg8r3R7ldv"