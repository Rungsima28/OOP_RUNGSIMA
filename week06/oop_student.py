import random as wawa
class Student:
    def __init__(self, ชื่อ , ชื่อเล่น , คะเเนนสอบ):
        self.name = ชื่อ
        self.nickname = ชื่อเล่น
        self.scoretest = คะเเนนสอบ
    def random(self):
        r = wawa.randint(1,10)
        self.scoretest += r
    def grade(self):
        if  self.scoretest>= 5:
            print('คุณสอบผ่าน')
        else:
            print('คุณสอบไม่ผ่าน')

student1 = Student(ชื่อ="นางสาวรังสิมา พิเดช",ชื่อเล่น="วา",คะเเนนสอบ=0)
student2 = Student(ชื่อ="นางสาววิลัยภรณ์ กัญจนกาญจน์",ชื่อเล่น="เป้",คะเเนนสอบ=0)
student3 = Student(ชื่อ="นางสาวไลลา รัตติกาล",ชื่อเล่น="ไลลา",คะเเนนสอบ=0)
student4 = Student(ชื่อ="นางสาวปิ่นทิพย์ รุ่งศรี",ชื่อเล่น="ปิ่น",คะเเนนสอบ=0)
student5 = Student(ชื่อ="นายมฤคินทร์ ปัญญาวัชระ",ชื่อเล่น="มิก",คะเเนนสอบ=0)

allstd = [student1,student2,student3,student4,student5]
for i in allstd:
    i.random()
    print(i.name,i.nickname,i.scoretest)
    i.grade()
    