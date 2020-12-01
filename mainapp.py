from views.user_view import SaleView

print("venta frutas plus...")

run = True
option = 0

saleView = SaleView()

while run:
    print("0 - exit")
    print("1 - user")
    print("2 - product")
    option = input("option: ")

    if option == 0:
        print("exit venta frutas...")
        break
    if option == 1:
        saleView.showMenu()
