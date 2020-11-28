from core.dx_logic import Logic
from persist_objects.cart_detail_obj import CartDetailObj
from logic.product_logic import ProductLogic


class CartDetailLogic(Logic):
    def __init__(self):
        super().__init__("cart_detail")

    def getAllCartDetails(self):
        cartDetailList = super().getAllRows(self.tableName)
        cartDetailObjList = []
        for element in cartDetailList:
            newCartDetail = self.createCartDetailObj(element)
            cartDetailObjList.append(newCartDetail)
        return cartDetailObjList

    def getCartDetailsById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newCartDetail = self.createCartDetailObj(rowDict)
        return newCartDetail

    # un metodo que nos de los cart details por idCart
    def getCartDetailsByIdCart(self, idCart):
        pass

    # polimorfismo
    # id,idcart,idproduct,cost,quantity,subtotal
    def createCartDetailObj(self, id, idCart, idProduct, cost, quantity, subtotal):
        cartDetailObj = CartDetailObj(id, idCart, idProduct, cost, quantity, subtotal)
        return cartDetailObj

    def createCartDetailObj(self, cartDetailDict):
        cartDetailObj = CartDetailObj(
            cartDetailDict["idcart"],
            cartDetailDict["idproduct"],
            cartDetailDict["cost"],
            cartDetailDict["quantity"],
            cartDetailDict["subtotal"],
            cartDetailDict["id"],
        )
        return cartDetailObj

    def insertCartDetail(self, idCart, idProduct, cost, quantity, subtotal):
        database = self.database
        sql = (
            f"INSERT INTO `ventafrutasplusdb`.`cart_detail`"
            + f"(`id`,`idcart`,`idproduct`,`cost`,`quantity`,`subtotal`) "
            + f"VALUES (0,{idCart},{idProduct},{cost},{quantity},{subtotal});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCartDetailById(self, id, idCart, idProduct, cost, quantity, subtotal):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`cart_detail` "
            + f"SET `idcart` = {idCart}, `idproduct` = {idProduct}, `cost` = {cost}, "
            + f"`quantity` = {quantity}, `subtotal` = {subtotal} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCartDetailByIdProduct(self, id, idProduct):
        CDObj = self.getCartDetailsById(id)
        prodLogic = ProductLogic()
        prodObj = prodLogic.getProductById(idProduct)
        idCart = CDObj.idCart
        quantity = CDObj.quantity
        subtotal = prodObj.cost * quantity
        rows = self.updateCartDetailById(
            id, idCart, prodObj.id, prodObj.cost, quantity, subtotal
        )
        return rows

    def updateCartDetailByCost(self, id, cost):
        pass

    def updateCartDetailByQuantity(self, id, quantity):
        pass

    def deleteCartDetailById(self, id):
        super().deleteRowById(id, self.tableName)

    def deleteCartDetailByIdCart(self, idCart):
        pass
