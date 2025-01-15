class Product:
    def __init__(self,name,product):
        self.name = name
        self.__price = []
        self.__product = product

    def addstock(self):
            self.__product += stock_in_company
        
    def removestock(self):
            self.__product -= stock_in_company

    def editprice(self):
        money_in_company = int(input('ใส่ราคาสินค้า '))
        self.__price.append(money_in_company)
    
    def Product_details(self):
        return (f'(มีสินค้าชื่อ {self.name} มีราคา {self.__price} บาท จำนวน {self.__product} ชิ้น)')

    
    
fan = Product("พัดลม",0)

while True:
    choiec = input('โปรดกรอกตามขั้นตามนี้ 1.addstock 2.removestock 3.editprice 4.check หรือ exit : ')
    if choiec == 'addstock':
        stock_in_company = int(input('โปรดกรอกจำนวนที่ต้องการจะเพิ่ม: '))
        fan.addstock()
    elif choiec == 'removestock':
        stock_in_company = int(input('โปรดกรอกจำนวนที่ต้องการจะลด: '))
        fan.removestock()
    elif choiec == 'editprice':
        fan.editprice()
    elif choiec == 'check':
        print(f'รายสินค้า{fan.name}มีรายละเอียดดังนี้{fan.Product_details()}')
    elif choiec == 'exit':
        break
    else:
        print('ลองใหม่อีกครั้ง')