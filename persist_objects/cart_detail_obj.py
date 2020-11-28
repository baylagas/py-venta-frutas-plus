class CartDetailObj:
    def __init__(self, idCart, idProduct, cost, quantity, subtotal=0, id=0):
        self.id = id
        self.idCart = idCart
        self.idProduct = idProduct
        self.cost = cost
        self.quantity = quantity
        self.subtotal = subtotal
