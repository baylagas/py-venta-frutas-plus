class CartDetailObj:
    def __init__(self, idcart, idproduct, cost, quantity, subtotal=0, id=0):
        self.id = id
        self.idcart = idcart
        self.idproduct = idproduct
        self.cost = cost
        self.quantity = quantity
        self.subtotal = subtotal
