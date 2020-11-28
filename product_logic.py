from dx_logic import Logic
from product_obj import ProductObj


class ProductLogic(Logic):
    def __init__(self):
        super().__init__("product")

    # code new methods
    def getAllProducts(self):
        productList = super().getAllRows(self.tableName)
        productObjList = []
        for element in productList:
            newProduct = self.createProductObj(element)
            productObjList.append(newProduct)
        return productObjList

    def getProductById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newProduct = self.createProductObj(rowDict)
        return newProduct

    # polimorfismo
    def createProductObj(self, id, name, cost):
        productObj = ProductObj(id, name, cost)
        return productObj

    def createProductObj(self, productDict):
        productObj = ProductObj(
            productDict["name"],
            productDict["cost"],
            productDict["id"],
        )
        return productObj

    def insertProduct(self, name, cost):
        database = self.database
        sql = (
            f"INSERT INTO `ventafrutasplusdb`.`product`(`id`,`name`,`cost`) "
            + f"VALUES(0,'{name}',{cost});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateProductById(self, id, name, cost):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`product` "
            + f"SET `name` = '{name}', `cost` = {cost} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProductById(self, id):
        super().deleteRowById(id, self.tableName)
