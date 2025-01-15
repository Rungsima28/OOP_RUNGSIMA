class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.__balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')

    def withdraw(self,amount):
        if amount >= 100:
            if amount <= self.balance:
                self.__balance -= amount
            else:
                print('ยอดเงินไม่เพียงพอ')
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')
    
    def check(self):
        return self.__balance

id1 = Bank(1,"Mix",5000)
print(f'เงินของ {id1.name} มีอยู่ {id1.check} บาท')
print('---------------------------------------------')
id1.__balance += 300
print('ฝากเงินไป 300 บาท')
print(f'เงินของ {id1.name} มีอยู่ {id1.check} บาท')
print('---------------------------------------------')
id1.withdraw(1000)
print('ถอนเงินไป 1000 บาท')
print(f'เงินของ {id1.name} มีอยู่ {id1.check} บาท')