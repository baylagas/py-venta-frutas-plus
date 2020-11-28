from logic.sale_logic import SaleLogic

logic = SaleLogic()
# logic.insertSale(3, 35.0, "3333444455556666")

# logic.updateSaleById(3, 1, 25.00, "1111222233334444")

# logic.deleteSaleById(4)

saleObjList = logic.getAllSales()
for saleObj in saleObjList:
    print(saleObj.idUser, saleObj.total, saleObj.cardNumber)

saleObj = logic.getSaleById(2)
print(saleObj.idUser, saleObj.total, saleObj.cardNumber)
