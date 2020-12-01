from logic.sale_detail_logic import SaleDetailLogic

logic = SaleDetailLogic()
# rows = logic.insertSaleDetail(1, 1, 1, 1, 1)
# print(f"{rows} affected")

# rows = logic.updateSaleDetailById(1, 1, 2, 2, 1, 2)
# print(f"{rows} affected")

# rows = logic.deleteSaleDetailById(10)
# print(f"{rows} affected")

saleDetailObjList = logic.getAllSaleDetail()
for saleDetailObj in saleDetailObjList:
    print(saleDetailObj.cost, saleDetailObj.subtotal)

saleDetailObj = logic.getSaleDetailById(5)
print(saleDetailObj.id, saleDetailObj.cost, saleDetailObj.subtotal)
