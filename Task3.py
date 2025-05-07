import hashlib

# def hash_password(password):
#     pass = password.encode('utf-8') 
#     hash_obj = haslib.sha256(pass)
#     hash_pass = hash_obj.hexdigest() #hexadecimal
#     return hash_pass

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
# {'username': 'raml', 'password': '8a10191e65ccf722bf59e70ddda155525c5f2ab80c5fed2ed67ee9f855171f7d'}

userList = [
    {"username": "John", "password": "123456"},
]
def login(username,password):
    for user in userList:
        if user["username"] == username:
            if hash(user["password"]) == hash(password):
                print("Login successful")
                return True
            else:
                print("Incorrect password")
                return False
        else:
            print("User not found")
            return False
        
# Welcome to the login system
# 1. Login
# 2. Register
# Please select an option: 1
# Please enter your username: John
# Please enter your password: 123456
# Login successful

def register(username,password):
    for user in userList:
        if user["username"] == username:
            while True:
                username = input("Username already exists. Please enter a new username: ")
                if user["username"] != username:
                    break
    userList.append({"username": username, "password": hash(password)})
    print("Registration successful")

# Welcome to the login system
# 1. Login
# 2. Register
# Please select an option: 2
# Please enter your username: John
# Please enter your password: 123456
# Username already exists. Please enter a new username: John2
# Registration successful

print("Welcome to the login system")
print("1. Login")
print("2. Register")
i = int(input("Please select an option: "))
if i == 1:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    login(username,password)
else:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    register(username,password)

print("Display \n", userList)


# Welcome to the login system
# 1. Login
# 2. Register
# Please select an option: 2
# Please enter your username: raml
# Please enter your password: 3453
# Registration successful
# Display
# [
#     {'username': 'John', 'password': '123456'}, 
#     {'username': 'raml', 'password': '8a10191e65ccf722bf59e70ddda155525c5f2ab80c5fed2ed67ee9f855171f7d'}
# ]