from core.dx_logic import Logic
from persist_objects.sale_obj import SaleObj


class SaleLogic(Logic):
    def __init__(self):
        super().__init__("sale")

    def getAllSales(self):
        saleList = super().getAllRows(self.tableName)
        saleObjList = []
        for element in saleList:
            newSale = self.createSaleObj(element)
            saleObjList.append(newSale)
        return saleObjList

    def getSaleById(self, id):
        rowDict = super().getRowById(id, self.tableName)
        newSale = self.createSaleObj(rowDict)
        return newSale

    # polimorfismo
    def createSaleObj(self, id, idUser, total, cardNumber):
        saleObj = SaleObj(idUser, total, cardNumber, id)
        return saleObj

    def createSaleObj(self, saleDict):
        saleObj = SaleObj(
            saleDict["iduser"],
            saleDict["total"],
            saleDict["cardnumber"],
            saleDict["id"],
        )
        return saleObj

    def insertSale(self, idUser, total, cardNumber):
        database = self.database
        sql = (
            f"INSERT INTO `ventafrutasplusdb`.`sale`"
            + f"(`id`,`iduser`,`total`,`cardnumber`) "
            + f"VALUES(0,{idUser},{total},'{cardNumber}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSaleById(self, id, idUser, total, cardNumber):
        database = self.database
        sql = (
            "UPDATE `ventafrutasplusdb`.`sale` "
            + f"SET `iduser` = {idUser}, `total` = {total}, "
            + f"`cardnumber` = '{cardNumber}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteSaleById(self, id):
        super().deleteRowById(id, self.tableName)
