a = int(input("โปรดใส่ค่าที่ต้องการ: "))
for i in range(1,24+1,1):
    c = a * i
    d = c / 2
    if d % 2 != 0:
        print(f"{a} x {i} = {c}")