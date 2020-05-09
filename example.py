from algosdk import algod
# Setup HTTP client w/guest key provided by PureStake
algod_address = "https://testnet-algorand.api.purestake."
algod_token = "eVXi2wPlDE8uF15mkil5Z2"
myProject_token = {"X-API-Key": algod_token}

algod_client = algod.AlgodClient(algod_token, algod_address, myProject_token)

#To test the code, simply uncomment them by highlighting and do ctrl + / (back slash)

 
# userName = input("Please enter your name.")
# print("Welcome " + userName)

# user_name = "Carnegie"
# print(user_name)

# if 10 > 3: #This is an example of a comment.
#     print("True") # Pythob ignores comment and will never run

# x = 100
# y = "What did you notice?"
# z = True
# a = False
# b  = frozenset({"apple", "banana", "cherry"})
# c = bytearray(8)
# d  = memoryview(bytes(6))
# veges = {"cucumber", "pumpkin", "garden egg"}
# f  = {"name" : "James", "age" : 30}
# g = range(10)
# vowel_list = ['a', 'e', 'i', 'o', 'u']
# vowel_tup = ('a', 'e', 'i', 'o', 'u')
# one_decimal = 12.1
# h = 12j

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(veges))
# print(type(f))
# print(type(g))
# print(type(vowel_list))
# print(type(vowel_tup))
# print(type(one_decimal))
# print(type(h))








# x = int(input("Enter the first number"))
# y = int(input("Enter the second number"))
# add_number = x + y

# print("The addition of the two numbers is: " + str(add_number))




# This is how to comment in python using VSCode
# This prints a line of text using both single and double quotes
# print("Good Morning User, today's topic is all about data type")



# x = 23
# y = 55
# z = bool(0)
# a = bool(1)
# print(x == y)
# print(x > y)
# print(z)
# print(a)

arbitrary_li = ["sausage", 10, "fish pie", True, "meat  pie", {"name": 'James', "age": 49,}]
arbitrary_list = (["sausage", 10, "fish pie", True, "meat  pie", {"name": 'James', "age": 49,}], 10, {"email": "bob@gmail.com"}, ["country", "towm"])
print(arbitrary_li)
print(arbitrary_list)














