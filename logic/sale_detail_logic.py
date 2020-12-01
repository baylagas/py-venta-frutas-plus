from core.dx_logic import Logic
from persist_objects.sale_detail_obj import SaleDetailObj


class SaleDetailLogic(Logic):
    def __init__(self):
        super().__init__("sale_detail")

    def getAllSaleDetail(self):
        saleDetailList = super().getAllRows(self.tableName)
        saleDetailObjList = []
        for element in saleDetailList:
            newSaleDetail = self.createSaleDetailObj(element)
            saleDetailObjList.append(newSaleDetail)
        return saleDetailObjList

    def getSaleDetailById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newSaleDetail = self.createSaleDetailObj(rowDict)
        return newSaleDetail

    # polimorfismo
    def createSaleDetailObj(self, id, idSale, idProduct, cost, quantity, subtotal):
        saleDetailObj = SaleDetailObj(id, idSale, idProduct, cost, quantity, subtotal)
        return saleDetailObj

    def createSaleDetailObj(self, saleDetailDict):
        saleDetailObj = SaleDetailObj(
            saleDetailDict["idsale"],
            saleDetailDict["idproduct"],
            saleDetailDict["cost"],
            saleDetailDict["quantity"],
            saleDetailDict["subtotal"],
            saleDetailDict["id"],
        )
        return saleDetailObj

    def insertSaleDetail(self, idSale, idProduct, cost, quantity, subtotal):
        database = self.database
        sql = (
            f"INSERT INTO `ventafrutasplusdb`.`sale_detail`"
            + f"(`id`,`idsale`,`idproduct`,`cost`,`quantity`,`subtotal`) "
            + f"VALUES(0,{idSale},{idProduct},{cost},"
            + f"{quantity},{subtotal});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSaleDetailById(self, id, idSale, idProduct, cost, quantity, subtotal):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`sale_detail` "
            + f"SET `idsale` = {idSale},`idproduct` = {idProduct},"
            + f"`cost` = {cost},`quantity` = {quantity},"
            + f"`subtotal` = {subtotal} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteSaleDetailById(self, id):
        rows = super().deleteRowById(id, self.tableName)
        return rows
