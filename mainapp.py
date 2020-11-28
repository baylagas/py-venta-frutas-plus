from cart_detail_logic import CartDetailLogic
from product_logic import ProductLogic
import random

prodLogic = ProductLogic()


def getRandomProduct(prodLogic):
    randomProd = random.choice([1, 2, 3, 4, 5])
    return prodLogic.getProductById(randomProd)


def getRandomeQuantity():
    return random.choice([2, 3, 4, 5, 6])


logic = CartDetailLogic()

# # inserts
# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(2, product.id, product.cost, quantity, product.cost * quantity)
# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(2, product.id, product.cost, quantity, product.cost * quantity)
# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(2, product.id, product.cost, quantity, product.cost * quantity)

# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(5, product.id, product.cost, quantity, product.cost * quantity)
# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(5, product.id, product.cost, quantity, product.cost * quantity)

# cdObjList = logic.getAllCartDetails()
# for cdObj in cdObjList:
#     print(cdObj.idProduct, cdObj.cost, cdObj.subtotal)

# cdObj = logic.getCartDetailsById(3)
# print(cdObj.idProduct, cdObj.cost, cdObj.subtotal)

# logic.updateCartDetailById(3, 2, 5, 1.0, 5, 5.0)

# product = getRandomProduct(prodLogic)
# quantity = getRandomeQuantity()
# logic.insertCartDetail(5, product.id, product.cost, quantity, product.cost * quantity)

# logic.deleteCartDetailById(6)

rows = logic.updateCartDetailByIdProduct(3, 4)
print(f"{rows} affected")
