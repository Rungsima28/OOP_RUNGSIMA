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
    def __init__(self, name, age, color,race):
        super().__init__(name, age, color)
        self.race = race
    def showdog(self):
        return f"หมาพันธุ์ {super().showinfo()}"
dog1 = Dog("wawa",5,"สีขาว","poodle")
print(dog1.showinfo())