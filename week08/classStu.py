class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grader = {}
    def score(self):
        choice = input('กรุณาเลือกิชาที่จะกรอกคะเเนน')
        score = int(input('ใส่คะเเนน'))
        grade = self.grade(score)
        if choice == "M" :
            self.grader["Math"] = grade
        elif choice == "T" :
            self.grader["Thai"] = grade
        elif choice == "E" :
            self.grader["English"] = grade
        elif choice == "S" :
            self.grader["Science"] = grade
        elif choice == "SS" :
            self.grader["Social Studies"] = grade
    def grade (self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
stu1 = Student("pae",10011,20)
stu2 = Student("wawa",10012,18)
stu1.score()
print(stu1.grader)