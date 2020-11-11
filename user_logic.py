from dx_logic import Logic
from user_obj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllUsers(self):
        database = self.database
        data = database.executeQueryRows("select * from user;")
        userList = []
        for element in data:
            newUser = self.createUserObj(element)
            userList.append(newUser)
        return userList

    def createUserObj(self, id, user, password, email):
        userObj = UserObj(id, user, password, email)
        return userObj

    def createUserObj(self, userDict):
        userObj = UserObj(
            userDict["user"],
            userDict["password"],
            userDict["email"],
            userDict["id"],
        )
        return userObj
