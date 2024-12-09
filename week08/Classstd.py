class Student:
    def __init__(self,student_name,student_id,
                 student_age,student_grades):
        self.name = student_name
        self.id = student_id
        self.age = student_age
        self.grades = student_grades

    def update_grades(self, subject, new_grade):
            self.grades[subject] = new_grade
            print(f"อัปเดตเกรด {subject} ของ {self.name} เป็น {new_grade}")
    
    def add_grades(self, new_subject, new_grade):
            self.grades[new_subject] = new_grade
            print(f"เพิ่มวิชา {new_subject} เกรดที่ได้ {new_grade} สำหรับ {self.name}")

    def average(self):
        gradesall = sum(self.grades.values()) / len(self.grades)
        print(f"{self.name} | ได้เกรดเฉลี่ย : {gradesall:.2f}")

    def allresults(self):
        gradesall = sum(self.grades.values()) / len(self.grades)
        print(f"ชื่อ : {self.name} หมายเลขประจำตัว : {self.id} อายุ : {self.age} เกรดเฉลี่ย : {gradesall:.2f} ")

grades1 = {'Math': 2,'Thai': 4,'English': 3,'Science': 1,'Social': 4}
grades2 = {'Math': 3,'Thai': 1,'English': 3,'Science': 4,'Social': 4}

mystudent1 = Student("นายสมชาย",1001,15,grades1)
mystudent2 = Student("นางสาวสมหญิง",1002,16,grades2)

mystudent1.average()
mystudent2.average()
print('---------------------------')

mystudent1.allresults()
mystudent2.allresults()
print('-----------------------------------------------------------')
print("รายละเอียดการอัปเดตเกรด")
mystudent1.update_grades('Math', 3)
mystudent1.average()
mystudent1.allresults()
print('---------------------------')
mystudent2.update_grades('English', 4)
mystudent2.average()
mystudent2.allresults()
print('-----------------------------------------------------------')
print("ระละเอียดการเพิ่มวิชาและเกรด")
mystudent1.add_grades('Math', 3)
mystudent1.allresults()
print('---------------------------')
mystudent2.add_grades('Art', 2)
mystudent2.allresults()