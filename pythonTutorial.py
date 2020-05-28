from connect import Connect
from sendtransaction import private_key_alc, defaultAddr, sendTransaction
from generateaccount import accounts, generateAccounts
import time
import json

toConnect = Connect()
getConnected = toConnect.connectToNetwork()

# generate the two accounts from generateAccount Module
creatAlcs = generateAccounts()
print("Accounts generate: ", creatAlcs)
print('\n')
# visit https://bank.testnet.algorand.network/ with account 1 to get testnet Algo Token
# prints the information of the first account that send Token
print(getConnected.account_info(defaultAddr))
print('\n')

alc_1_addr = (accounts['account_1']['alc_address'])
alc_2_addr = (accounts['account_2']['alc_address'])
alc_1_pk = (accounts['account_1']['pkey'])

# Call the he function from sendtransaction.py file
# Default account sends token to account 1
trxn_1 = sendTransaction(private_key_alc, defaultAddr, alc_1_addr, 303000)
print(trxn_1)
print('\n')
time.sleep(60)
# Account 1 sends token to account 2
trxn_2 = sendTransaction(alc_1_pk, alc_1_addr, alc_2_addr, 100000)
print(trxn_2)

print("Default Address: ", json.dumps(getConnected.account_info(defaultAddr)))
print("Address 1: ", json.dumps(getConnected.account_info(alc_1_addr)))
print("Address 2: ", json.dumps(getConnected.account_info(alc_2_addr)))














# Day 5 Tutorial

# def convertToMnemonicKey():
#     return mnemonic.from_private_key(private_key)

# mnemonic_phrase = convertToMnemonicKey()
# print("My Mnemonic Phrase: ", mnemonic_phrase)
# print('\n')

# def convertToPrivateKey():
#     result = "My Private Key:", mnemonic.to_private_key(mnemonic_phrase)
#     return result

# private_key = convertToPrivateKey()
# print(private_key)

# def convertToPublicKey():
#     result = "My public Key: " + str(mnemonic.to_public_key(mnemonic_phrase))
#     print(result)
# convertToPublicKey()
















# user_profile = {
#     "name": "Fred",
#     "lastname": "Blonde",
#     "age": 39,
#     "hobbies": ['traveling', 'cycling', 'skating'],
#     "session_login_avg": {"daily": "twice", "weekly": "6 times", "monthly": 22,}
# }
# # user_profile["age"] = 37
# # print(user_profile)

# # print out all the values in a dictionary
# for x, y in user_profile.items():
#     print(x,":", y)

# # check if a key exist
# if "hobbies" in user_profile:
#     print("True")

# # prints all values in the user_profile
# for x in user_profile.values():
#     print(x)

# # prints the length of user_profile
# print(len(user_profile))




