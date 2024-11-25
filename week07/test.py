try:
    a = 5
    b = 0
    c = a/b
    print(c)
except:
    print("ห้ามใส่ 0")
finally:
    print("จบโปรแกรม")

print('-------------------------------')

try:
    a = 5
    b = 0
    if b == 0:
        raise Exception() #ใส่เพื่อให้เจาะจง Error
    else:
        c = a/b
        print(c)
except:
    print("ห้ามใส่ 0")
finally:
    print("จบโปรแกรม")

print('-------------------------------')

try:
    a = 5
    b = int(input("ใส่ตัวเลข : "))
    if b == 10:
        raise Exception()
    else:
        c = a-b
        print(c)
except ValueError:
    print("ใส่เฉพาะตัวเลข")
finally:
    print("จบโปรแกรม")

print('-------------------------------')

try:
    a = 5
    b = int(input("ใส่ตัวเลข : "))
    if b == 0:
        raise ZeroDivisionError()
    else:
        c = a*b
        print(c)
except ZeroDivisionError:
    print("ใส่เฉพาะตัวเลข")
finally:
    print("จบโปรแกรม")