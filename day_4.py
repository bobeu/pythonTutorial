# from algosdk import account, encoding, algod, mnemonic, kmd, wallet
# from algosdk.future import transaction


# # Setup HTTP client w/guest key provided by PureStake
# algod_address = "https://testnet-algorand.api.purestake.io/ps1"
# algod_token = "eVXi2wPlDE8uF15mkil5................" #shortened - my personal API token
# myProject_token = {"X-API-Key": algod_token}

# algod_client = algod.AlgodClient(algod_token, algod_address, myProject_token)


# private_key, address = account.generate_account()
# print("Private key:", private_key)
# print("Address:", address)


user_profile = {
    "name": "Fred",
    "lastname": "Blonde",
    "age": "39",
    "hobbies": ['traveling', 'cycling', 'skating'],
    "session_login_avg": {"daily": "twice", "weekly": "6 times", "monthly": 22,}
}
user_profile["age"] = 37
print(user_profile)

# print out all the values in a dictionary
for x, y in user_profile.items():
    print(x,":", y)

# check if a key exist
if "hobbies" in user_profile:
    print("True")

# prints all values in the user_profile
for x in user_profile.values():
    print(x)

# prints the length of user_profile
print(len(user_profile))




