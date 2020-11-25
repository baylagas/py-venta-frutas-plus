from dx_logic import Logic
from user_obj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "user"

    def getAllUsers(self):
        userList = super().getAllRows(self.tableName)
        userObjList = []
        for element in userList:
            newUser = self.createUserObj(element)
            userObjList.append(newUser)
        return userObjList

    # polimorfismo
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

    def insertUser(self, user, password, email):
        database = self.database
        sql = (
            f"INSERT INTO `ventafrutasplusdb`.`user`(`id`,`user`,`password`,`email`) "
            + f"VALUES(0,'{user}','{password}','{email}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateUserById(self, id, user, password, email):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`user` "
            + f"SET `user` = '{user}', `password` = '{password}', `email` = '{email}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUserById(self, id):
        super().deleteRowById(id, self.tableName)
