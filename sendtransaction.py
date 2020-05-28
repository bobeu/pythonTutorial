from algosdk import algod, transaction, encoding
from connect import Connect
from generateaccount import accounts

defaultAddr = "N6SJLDQXCXZ7IJMLM5VVEAWJ36JUJSDQVNQFA2I3BKFOWE3QLKKJGATPJ4"
private_key_alc = "QZkBrhS8lENmn30GyKMPufFPdjG88Knz0Fj279+jxVdvpJWOFxXz9CWLZ2tSAsnfk0TIcKtgUGkbCorrE3BalA=="

forAlgoClient = Connect()
algAddr = forAlgoClient.algod_address
algTok = forAlgoClient.algod_token
head = forAlgoClient.headers
forParam = algod.AlgodClient(algTok, algAddr, head)

algodClient = forAlgoClient.connectToNetwork()
params = forParam.suggested_params()
note = "Hi, sent you some Algo".encode()

def sendTransaction(privateKey, my_address, receiver, amount):
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

    trxn = transaction.PaymentTxn(**txn)
    signTrxn = trxn.sign(privateKey)
    trxn_id = signTrxn.transaction.get_txid()
    try:
        return ("Transaction was signed with: ", algodClient.send_transaction(signTrxn,  headers={'content-type': 'application/x-binary'}))
    except Exception as e:
        print(e)






# gn="testnet-v1.0"
# genhash="SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI="