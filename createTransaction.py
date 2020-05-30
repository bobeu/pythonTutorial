from connect import Connect
from algosdk import algod, transaction

forAlgo = Connect()
algAddr = forAlgo.algod_address
algTok = forAlgo.algod_token
head = forAlgo.headers
forParam = algod.AlgodClient(algTok, algAddr, head)
params = forParam.suggested_params()
note = "Hi, sent you some Algo".encode()

def create_transaction(privateKey, my_address, receiver, amount):
    txn = {
        "sender": my_address,
        "receiver": receiver,
        "fee": params.get('minFee'),
        "flat_fee": True,
        "amt": amount,
        "first": params.get('lastRound'),
        "last": params.get('lastRound') + 1000,
        "note": note,
        "gen": params.get('genesisID'),
        "gh": params.get('genesishashb64')
    }
    
    return transaction.PaymentTxn(**txn)
