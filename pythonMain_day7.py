from connect import Connect
from sendtransaction import defaultAddr, private_key_alc, sendTransaction
from generateaccount import generateAccounts, accounts
import time
import json


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


send_1 = sendTransaction(private_key_alc, defaultAddr, alc_1_addr, alc_2_addr, alc_3_addr, 200000)
print("Tranaction 1 was sent to pool")
print("Waiting comfirmation...")
time.sleep(35)

def printAccountsInfo():
    # Get accounts information in json format
    print("Default Address information: {} {}".format(json.dumps(getConnected.account_info(defaultAddr)), "\n"))
    print("Address 1 info: {} {}".format(json.dumps(getConnected.account_info(alc_1_addr)), "\n"))
    print("Address 2 info: {} {}".format(json.dumps(getConnected.account_info(alc_2_addr)), "\n"))
    print("Address 3 info: {}".format(json.dumps(getConnected.account_info(alc_3_addr))))

printAccountsInfo()
filename = 'textfile.txt'
with open(filename, 'w', 'endrun') as file_write:
    file_write.write(printAccountsInfo())