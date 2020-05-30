from algosdk import algod, transaction
from connect import Connect
from createTransaction import create_transaction

forAlgoClient = Connect()
algodClient = forAlgoClient.connectToNetwork()

def sendTransaction(privateKey, sending_addr, receiving_addr, amount):
    # Create two seperate transactions
    trxn_1 = create_transaction(privateKey, sending_addr, receiving_addr, amount)
    trxn_2 = create_transaction(privateKey, sending_addr, receiving_addr, amount)
    # Make transactions into group
    gid = transaction.calculate_group_id([trxn_1, trxn_2])
    trxn_1.group = gid
    trxn_2.group = gid
    # sign the transaction
    signTrxn_1 = trxn_1.sign(privateKey)
    signTrxn_2 = trxn_2.sign(privateKey)
    # trxn_id = signTrxn.transaction.get_txid()
    
    try:
        return ("Transactions were signed with: ", algodClient.send_transactions([signTrxn_1, signTrxn_2], headers={'content-type': 'application/x-binary'}))
    except Exception as e:
        print(e)























# gn="testnet-v1.0"
# genhash="SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI="