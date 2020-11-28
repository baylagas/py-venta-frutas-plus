from core.dx_logic import Logic
from persist_objects.cart_obj import CartObj


class CartLogic(Logic):
    def __init__(self):
        super().__init__("cart")

    def getAllCarts(self):
        cartList = super().getAllRows(self.tableName)
        cartObjList = []
        for element in cartList:
            newCart = self.createCartObj(element)
            cartObjList.append(newCart)
        return cartObjList

    def getCartById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newCart = self.createCartObj(rowDict)
        return newCart

    # polimorfismo
    def createCartObj(self, id, idUser, total):
        cartObj = CartObj(id, idUser, total)
        return cartObj

    def createCartObj(self, cartDict):
        cartObj = CartObj(
            cartDict["iduser"],
            cartDict["total"],
            cartDict["id"],
        )
        return cartObj

    def insertCart(self, idUser, total=0):
        database = self.database
        sql = (
            "INSERT INTO `ventafrutasplusdb`.`cart`(`id`,`iduser`,`total`) "
            + f"VALUES (0,{idUser},{total});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCartById(self, id, idUser, total=0):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`cart` "
            + f"SET `iduser` = {idUser}, `total` = {total} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCartById(self, id):
        rows = super().deleteRowById(id, self.tableName)
        return rows
