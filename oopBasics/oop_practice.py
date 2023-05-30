class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity
 
class Store:
    def __init__(self) -> None:
        self.__products_price = {}
        self.__products_quantity = {}
        self.__profit = 0
 
    def add_product(self, name, price, quantity):
 
        product = Product(name, price, quantity)
 
        self.__products_price[product.product_name] = product.product_price
        self.__products_quantity[product.product_name] = product.product_quantity
 
    def buy_product(self, name, quantity):
        if name in self.__products_price:
            if self.__products_quantity[name] >= quantity:
                # profit calculate
                self.__profit = self.__profit + ((5*self.__products_price[name])/100)*quantity
                # deduct product quantity
                self.__products_quantity[name] = self.__products_quantity[name] - quantity
                print("thank you")
            else:
                print("Unavailable")
        else:
            print("Not Found")
 
    def show_products(self):
        print("all products price: ",self.__products_price)
        print("all products quantity: ",self.__products_quantity)
 
    def show_profit(self):
        print("profit: ",self.__profit)
 
class Shop(Store):
    def __init__(self, name) -> None:
        self.shop_name = name
        super().__init__()
 
 
shop1 = Shop("aapel bd")
 
shop1.add_product("iphoneX", 400, 12)
shop1.add_product("samsungS9", 350, 20)
 
shop1.show_products()
 
shop1.buy_product("iphoneX", 2)
 
shop1.show_products()
 
shop1.show_profit()
 
shop2 = Shop("gadget 420")
 
shop2.add_product("mackbook", 800, 7)
 
shop2.show_products()