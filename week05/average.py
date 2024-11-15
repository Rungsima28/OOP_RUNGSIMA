number = int(input("ต้องการป้อนทั้งกี่ตัว : "))
score = []
for i in range (number):
    num = int(input(f"ใส่ตัวที่ {i+1} : "))
    score .append(num)
result = sum(score) //len(score)
print(f"ค่าเฉลี่ยของ {score} = {result}")