print("คำนวณหาพื้นที่ 4 เหลี่ยมจตุรัส")
side = float(input('ใส่ความยาวด้าน: '))
result = side*side
print("พื้นที่ 4 เหลี่ยมจตุรัสนี้ คือ "+str(result))

print("คำนวณหาพื้นที่ 4 เหลี่ยมผืนผ้า")
wide = float(input('ใส่ความกว้าง: '))
long = float(input('ใส่ความยาว: '))
result1 = wide*long
print("พื้นที่ 4 เหลี่ยมผืนผ้านี้ คือ "+str(result1))

print("คำนวณหาพื้นที่วงกลม")
radius = float(input('ใส่ความยาวของรัศมี: '))
result3 = 3.14*radius**2
print("พื้นที่ 4 เหลี่ยมวงกลม คือ "+str(result3))