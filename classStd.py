class Student:
    def __init__(self,student_name,student_id,student_age,student_grades):
        self.name = student_name
        self.id = student_id
        self.age = student_age
        self.grades = student_grades
    def modify(self):
        self.grades["match"] = float(input("ใส่คะเเนนวิชาคณิต"))
        self.grades["thai"] = float(input("ใส่คะเเนนวิชาภาษาไทย"))
        self.grades["English"] = float(input("ใส่คะเเนนวิชาอังกฤษ"))
        self.grades["Science"] = float(input("ใส่คะเเนนวิชาวิทย์"))
        self.grades["Social"] = float(input("ใส่คะเเนนวิชาสังคม"))
    def avg_grades(self):
        return sum(self.grades.value()) / len(self.grades)
    
student1 = Student("รังสิมา","67319010015","15",{})
student1.modify()
average = student1.avg_grades()
print(f"ชื่อ {student1.name} รหัสนักเรียน {student1.id} อายุ {student1.age} เกรด {student1.grades} ได้เกรดเฉลี่ย {average:.2f}")