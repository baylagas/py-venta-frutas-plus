from user_logic import UserLogic

logic = UserLogic()
# userList = logic.getAllUsers()
# for userObj in userList:
#     print(userObj.id, userObj.user, userObj.password, userObj.email)

# logic.insertUser("test01", "123", "test01@gmail.com")

logic.updateUserById(2, "test01x", "123", "test01x@gmail.com")
