from algosdk import account, algod, encoding
from algosdk.future import transaction
from connect import Connect
from generateaccount import generateAccounts, accounts
from createTransaction import create_transaction

wifeAddress = "N6SJLDQXCXZ7IJMLM5VVEAWJ36JUJSDQVNQFA2I3BKFOWE3QLKKJGATPJ4"
wifePrivateKey = "QZkBrhS8lENmn30GyKMPufFPdjG88Knz0Fj279+jxVdvpJWOFxXz9CWLZ2tSAsnfk0TIcKtgUGkbCorrE3BalA=="

toConnect = Connect()
getConnected = toConnect.connectToNetwork()
params = getConnected.suggested_params()
note = "We just spent 400 Algo for this month".encode()

def txnfield(my_address, receiver, amount):
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


# generate three accounts
gen_alc = generateAccounts()
print(gen_alc)

# Generate a multisignature account
req = 2  # number of Signature(s) required
vers = 1  # version of Signature
hisAddress = (accounts['account_1']['alc_address'])
hisPrivateKey = (accounts['account_1']['pkey'])
spendAccount = (accounts['account_2']['alc_address'])

# create the rule
multsig = transaction.Multisig(vers, req, [hisAddress, wifeAddress])
i = multsig.get_multisig_account()
print(i)


# # create a transaction
savingAlcAddr = multsig.address()
# trx = create_transaction(savingAlcAddr, spendAccount, 401000)
trxn = txnfield(savingAlcAddr, spendAccount, 401000)
# trxn = transaction.PaymentTxn(**trxn)
multisigtxn = transaction.MultisigTransaction(trxn, multsig) # create a SignedTransaction object
multisigtxn.sign(wifePrivateKey) # signer1 signs the transaction
multisigtxn.sign(hisPrivateKey) # signer2 signs the transaction
getConnected.send_transaction(multisigtxn, headers={'content-type': 'application/x-binary'})

# # print encoded transaction
print(encoding.msgpack_encode(multisigtxn))


# savingAlcAddr, params, spendAccount, 401000


# transaction.write_to_file([txn], "pathtofile.tx")



# def i():
#     k = (0, 1, 2)
#     for i in k:
#         return k[i]

# h = i()
# print(i)
# filename = 'textfile.txt'
# with open(filename, 'w') as file_write:
#     h = i()
#     file_write.write(str(h))
    # file_write.write().__dict__

    # transaction.PaymentTxn(sender, sp, account_3, amount)


    
# txn = {
#     "fee": params.get('minFee'),
#     "flat_fee": True,
#     "first": params.get('lastRound'),
#     "last": params.get('lastRound') + 1000,
#     "note": note,
#     "gen": params.get('genesisID'),
#     "gh": params.get('genesishashb64')
# }