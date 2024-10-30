print("โปรเเกรมคำนวณเกรดเฉลี่ย")
score = int(input("กรอกคะเเนน :"))
if score >= 100:
    print("error")
elif score > 80 :
    print("คุณได้เกรด 4")
elif score > 70 :
    print("คุณได้เกรด 3")
elif score > 60 :
    print("คุณได้เกรด 2")
elif score > 50 :
    print("คุณได้เกรด 1")
elif score < 50 :
    print("คุณสอบตก")
    print("คุณต้องการเเก้ 0 ไหม")
    take2 = int(input("ถ้าใช่ ตอบ1 ถ้าไม่ใช่ ตอบ2 \n คำตอบคือ : "))
    if take2 == 1 :
        print("คุณขาดคะเเนนอีก"+str(50-score)+"ถึงจะสอบผ่าน")
    elif take2 == 2 :
        print("คุณสอบไม่ผ่าน")
else :
    print("กรอกตัวเลขใหม่อีกครั้ง")