score = {}
number = int(input("จำนวนคนที่จะป้อน : "))
for i in range (1,number+1):
    print(f"กรุณากรอกคนที่ {i} : ")
    score['nickname'] = str(input(f"กรุณากรอกชื่อเล่น : "))
    score['stdid'] = int(input(f"กรุณากรอกเลขที่ : "))
    score['hobby'] = str(input(f"กรุณากรอกงานอดิเรก : "))
    score['color'] = str(input(f"กรุณากรอกสีที่ชอบ : "))
    print(f"ข้อมูลคนที่ {str(i)}\n{score}")