from user_logic import UserLogic

logic = UserLogic()
userList = logic.getAllUsers()
for userObj in userList:
    print(userObj.id, userObj.user, userObj.password, userObj.email)
