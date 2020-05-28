from algosdk import account
from connect import Connect

accounts = {}
# To get acount information
getConnect = Connect()
forAlcInfo = getConnect.connectToNetwork() 

# define a function to generate 2 accounts
def generateAccounts():
    # generate accounts 1 and 2
    private_key_1, address_1 = account.generate_account()
    private_key_2, address_2 = account.generate_account()
    account_1 =  {
            "pkey": private_key_1,
            "alc_address":address_1,
            "alc_information": forAlcInfo.account_info(address_1)
        }
    account_2 = {
            "pkey": private_key_2,
            "alc_address":address_2,
            "alc_information": forAlcInfo.account_info(address_2)
        }
    # store accounts 1 and 2
    accounts["account_1"] = account_1
    accounts["account_2"] = account_2
    return (accounts)

