from connect import Connect
from sendtransaction import sendTransaction
from generateaccount import generateAccounts, accounts
import time
import json

defaultAddr = "N6SJLDQXCXZ7IJMLM5VVEAWJ36JUJSDQVNQFA2I3BKFOWE3QLKKJGATPJ4"
private_key_alc = "QZkBrhS8lENmn30GyKMPufFPdjG88Knz0Fj279+jxVdvpJWOFxXz9CWLZ2tSAsnfk0TIcKtgUGkbCorrE3BalA=="
toConnect = Connect()
getConnected = toConnect.connectToNetwork()

# generate the two accounts from generateAccount Module
creatAlc = generateAccounts()
print("Accounts generated: {} {}".format(creatAlc, '\n'))
# visit https://bank.testnet.algorand.network/ with account 1 to get testnet Algo Token
# prints the information of the first account that send Token
print("default Account info: {} {}".format(getConnected.account_info(defaultAddr), '\n'))
#Get addresses and private key of account_2
alc_1_addr = (accounts['account_1']['alc_address'])
alc_2_addr = (accounts['account_2']['alc_address'])
alc_3_addr = (accounts['account_3']['alc_address'])
alc_1_pk = (accounts['account_1']['pkey'])
alc_2_pk = (accounts['account_2']['pkey'])

# Call the he function from sendtransaction.py file and default account sends token to account 1
send_1 = sendTransaction(private_key_alc, defaultAddr, alc_1_addr, 304000)
print("Tranaction 1 was sent to pool: {} {}".format(send_1, '\n'))
# print a line
print('\n')
# handles confirmation time
time.sleep(60)
# Account 1 sends token to account 2
send_2 = sendTransaction(alc_1_pk, alc_1_addr, alc_2_addr, 203000)
print("Tranaction 2 was successful with ID: {} {}".format(send_2, '\n'))
time.sleep(60)
# Account 2 sends Algo to Account 3
send_3 = sendTransaction(alc_2_pk, alc_2_addr, alc_3_addr, 100000)
print("Tranaction 3 was successful with ID: {} {}".format(send_3, '\n'))

print("Default Address information: {} {}".format(json.dumps(getConnected.account_info(defaultAddr)), "\n"))
print("Address 1 info: {} {}".format(json.dumps(getConnected.account_info(alc_1_addr)), "\n"))
print("Address 2 info: {} {}".format(json.dumps(getConnected.account_info(alc_2_addr)), "\n"))
print("Address 3 info: {}".format(json.dumps(getConnected.account_info(alc_3_addr))))















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


# Uncomment
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




