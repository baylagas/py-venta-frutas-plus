from dx_logic import Logic


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
