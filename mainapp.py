# from dx_logic import Logic

from user_logic import UserLogic
from product_logic import ProductLogic

# logic = UserLogic()
# userList = logic.getAllUsers()
# for userObj in userList:
#     print(userObj.id, userObj.user, userObj.password, userObj.email)

# logic.insertUser("test02", "123", "test02@gmail.com")

# logic.updateUserById(2, "test01x", "123", "test01x@gmail.com")

# cc game fest
# Python Invaders: Creando videojuegos con Python
# miercoles 18 nov
# 1:15pm - 1 hora


# database = DatabaseX()
# sql = "select * from ventafrutasplusdb.user;"
# userList = database.executeQueryRows(sql)
# for userDict in userList:
#     print(userDict["user"], userDict["email"])

# sql = "select * from ventafrutasplusdb.user where id=1;"
# userDict = database.executeQueryOneRow(sql)
# if userDict is not None:
#     print(userDict["password"], userDict["user"])
# else:
#     print("el usuario no existe")

# logic = UserLogic()

logic = ProductLogic()

# logic.insertProduct("kiwi", 2.50)

# productList = logic.getAllProducts()
# for productObj in productList:
#     print(productObj.id, productObj.name, productObj.cost)

# import os

# print(os.getcwd())
# wd = os.getcwd()
# musicfiles = "\\music"
# print(wd + musicfiles)
