class Cat:
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        return self.name , "เมี๊ยวๆ"
    def cry2(self):
        print (f"แมว{self.color} ชื่อ {self.cry()}")
mycat1 = Cat("ศรีทอง","สีส้ม")
mycat2 = Cat("ศรีเงิน","สีขาว")
print(mycat1.cry2())
