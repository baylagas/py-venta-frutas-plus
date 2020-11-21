from dx_logic import Logic
from product_obj import ProductObj


class PepitoLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllProducts(self):
        database = self.database
        sql = "select * from ventafrutasplusdb.product;"
        productList = database.executeQueryRows(sql)
        productObjList = []
        for productDict in productList:
            name = productDict["name"]
            cost = productDict["cost"]
            id = productDict["id"]
            currentObj = ProductObj(name, cost, id)
            productObjList.append(currentObj)
        return productObjList
