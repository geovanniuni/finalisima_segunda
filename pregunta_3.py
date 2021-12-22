
class User:
    userid = None
    password = None
    loginStatus = None
    registerDate = None

    def __init__(self, userId, password, loginStatus, registerDate):
        self.userid = userId
        self.password = password
        self.loginStatus = loginStatus
        self.registerDate = registerDate

    def veryLogin(self):
        print("login verificado")



class Adminsistrator(User):
    adminName = None
    email = None

    def __init__(self, adminName, email, userId, password, loginStatus, registerDate):
        super().__init__(userId, password, loginStatus, registerDate)
        self.adminName =adminName
        self.email = email

    def updateCatalog(self):
        print("El catalogo esta actualziado")


class Customer(User):
    customerName = None
    address = None
 #   email = None
 #   creditCardinfo = None
 #   shipping_info = None
 #   account_balance = None

#    def __init__(self, customerName, address, email, creditCardinfo, shipping_info, account_balance, cartid):
    def __init__(self,userId, password, loginStatus, registerDate, address ,cartid,customerName, orderid, productid, productName,
                 quantity, unitCost, shippingid, shippingType, shippingCost, shippingRegionid ):

        super().__init__(userId, password, loginStatus, registerDate)
        self.customerName=customerName
        self.address=address
 #       self.email=email
 #       self.creditCardinfo=creditCardinfo
 #       self.shipping_info=shipping_info
 #       self.account_balance=account_balance
        self.shoppingCartx = Shopping_Cart(cartid)
        self.orderx = Order(customerName, orderid, productid, productName,
                 quantity, unitCost, shippingid, shippingType, shippingCost, shippingRegionid)





class Shopping_Cart:
    cartid = None
#    productID =None
#    quantity = None
#    dateAddress =None

    def __init__(self, cartid):
#   def __init__(self, cartid,productID,quantity,dateAddress):
        self.cartid=cartid
#        self.productID=productID
#        self.quantity=quantity
#        self.dateAddress=dateAddress

    def addCartitem(self):
        print("agregando Item")

    def updateQuantity(self):
        print("Actualizando la cantidad")

    def viewCartDetails(self):
        print("vizualizando detalles del carrito")
        print("id del carrito: ")
        print(self.cartid)

    def checkOut(self):
        print("Realizando el checkout")





class Order:
    orderid = None  #
  #  dateCreated = None
  #  dateShipped = None
    customerName = None
  #  customerid = None
  #  status = None
    shippingid = None #

    def __init__(self, customerName, orderid, productid, productName,
                 quantity, unitCost, shippingid, shippingType, shippingCost, shippingRegionid):
    #def __init__(self, dateCreated,dateShipped,customerName,customerid,status , orderid,productid,productName,quantity,unitCost,  shippingid,shippingType,shippingCost,shippingRegionid):
        self.orderid = orderid
     #   self.dateCreated = dateCreated
     #   self.dateShipped = dateShipped
        self.customerName = customerName
     #   self.customerid = customerid
     #   self.status = status
     #   self.shippingid = shippingid
        self.order_info = Order_Details(orderid,productid,productName,quantity,unitCost)
        self.shi_info = shipping_info(shippingid,shippingType,shippingCost,shippingRegionid)

    def placeOrder(self):
        print(" Orden procesada")



class Order_Details:
    orderid = None
    productid = None
    productName = None
    quantity = None
    unitCost = None
    subtotal = None



    def __init__(self, orderid,productid,productName,quantity,unitCost ):
        self.orderid = orderid
        self.productid = productid
        self.productName = productName
        self.quantity = quantity
        self.unitCost = unitCost


    def calcPrice(self):
        print("obteniendo precio...")
        self.subtotal = self.unitCost * self.quantity
        print(self.subtotal)


class shipping_info:
    shippingid= None
    shippingType=None
    shippingCost = None
    shippingRegionid = None

    def __init__(self, shippingid, shippingType, shippingCost, shippingRegionid):
        self.shippingid=shippingid
        self.shippingType=shippingType
        self.shippingCost=shippingCost
        self.shippingRegionid=shippingRegionid

    def updateShippinginfo(self):
        print("updating info ....")
        print(" Informacion actual: ")
        print(" id de embarcacion: ")
        print(self.shippingid)
        print("tipo de embarcacion ")
        print(self.shippingType)
        print("Costo de la embarcacion")
        print(self.shippingCost)
        print("Region: ")
        print(self.shippingRegionid)



# -----------------------------------------------------------

custo_1 = Customer(12, '122', 'Activado', '08/10/21', 'Lima' ,213, 'Juan', '121332', '43443', 'trofeo',
                 4, 3, '12233', 'lento', 12, 3)

print("")
custo_1.veryLogin()

print("")
custo_1.shoppingCartx.viewCartDetails()

print("")
custo_1.orderx.placeOrder()

print("")
custo_1.orderx.order_info.calcPrice()

print("")
custo_1.orderx.shi_info.updateShippinginfo()