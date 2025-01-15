class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
    #animal1 = Animal("wawa",5,"สีดำ")
    #print(f"สัตว์ตัวนึงมี {animal1.showinfo()}")

class Dog(Animal):
    def speak(self):
        return "โฮ่ง"   
dog1 = Dog("wawa",5,"สีขาว")
print(f"หมาชื่อ {dog1.name} ร้อง {dog1.speak()}")
print(f"ข้อมูลหมาตัวที่1 คือ {dog1.showinfo()}")