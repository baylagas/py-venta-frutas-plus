from pepito_logic import PepitoLogic

pepitoObj = PepitoLogic()
pepitoObjList = pepitoObj.getAllProducts()

for pepito in pepitoObjList:
    print(pepito.id, pepito.name, pepito.cost)

# import os

# print(os.getcwd())
# wd = os.getcwd()
# musicfiles = "\\music"
# print(wd + musicfiles)

# print(os.listdir(os.getcwd()))
# itemList = os.listdir(os.getcwd())
# for item in itemList:
#     if ".py" in item:
#         print(item.replace(".py", ""))
