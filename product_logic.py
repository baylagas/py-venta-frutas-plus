from dx_logic import Logic
from product_obj import ProductObj


class ProductLogic(Logic):
    def __init__(self):
        super().__init__()

    # code new methods
    def getAllProducts(self):
        database = self.database
        data = database.executeQueryRows("select * from product;")
        productList = []
        for element in data:
            newProduct = self.createProductObj(element)
            productList.append(newProduct)
        return productList

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
        database = self.database
        sql = f"DELETE FROM `ventafrutasplusdb`.`product` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
