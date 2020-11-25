from user_logic import UserLogic

print("insert a new user")
user = input("user:")
password = input("password:")
email = input("email:")

logic = UserLogic()
rows = logic.insertUser(user, password, email)
print(f"{rows} affected")
