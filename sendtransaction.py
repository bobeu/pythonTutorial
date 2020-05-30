from algosdk import algod, transaction
from connect import Connect
from createTransaction import create_transaction

forAlgoClient = Connect()
algodClient = forAlgoClient.connectToNetwork()
defaultAddr = "N6SJLDQXCXZ7IJMLM5VVEAWJ36JUJSDQVNQFA2I3BKFOWE3QLKKJGATPJ4"
private_key_alc = "QZkBrhS8lENmn30GyKMPufFPdjG88Knz0Fj279+jxVdvpJWOFxXz9CWLZ2tSAsnfk0TIcKtgUGkbCorrE3BalA=="

def sendTransaction(privateKey_def, addr_def, addr_acl_1, addr_acl_2, addr_acl_3, amount):
    # Create two seperate transactions
    trxn_1 = create_transaction(privateKey_def, addr_def, addr_acl_1, amount)
    trxn_2 = create_transaction(privateKey_def, addr_def, addr_acl_2, amount)
    trxn_3 = create_transaction(privateKey_def, addr_def, addr_acl_3, amount)
    # Make transactions into group
    gid = transaction.calculate_group_id([trxn_1, trxn_2, trxn_3])
    trxn_1.group = gid
    trxn_2.group = gid
    trxn_3.group = gid
    # sign the transaction
    signTrxn_1 = trxn_1.sign(privateKey_def)
    signTrxn_2 = trxn_2.sign(privateKey_def)
    signTrxn_3 = trxn_3.sign(privateKey_def)
    # trxn_id = signTrxn.transaction.get_txid()
    
    try:
        return ("Transactions were signed with: ", algodClient.send_transactions([signTrxn_1, signTrxn_2, signTrxn_3], headers={'content-type': 'application/x-binary'}))
    except Exception as e:
        print(e)























# gn="testnet-v1.0"
# genhash="SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI="