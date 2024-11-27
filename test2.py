try:
    a = int(input('ใส่คะเเนน :'))
    if a < 0 :
        raise Exception()
    elif a == 0 :
        raise ZeroDivisionError()
    elif a >= 80 :
        print('คุณได้เกรด 4')
    elif a >= 70 :
        print('คุณได้เกรด 3')
    elif a >= 60 :
        print('คุณได้เกรด 2')
    elif a >= 50 :
        print('คุณได้เกรด 1')
    elif a <= 49 :
        print('คุณสอบตก')
except ValueError:
    print('กรุณาใส่ตัวเลขเท่านั้น')
except ZeroDivisionError:
    print('ค่าคะเเนนต้องไม่เป็น 0')
except :
    print('ค่าคะเเนนต้องไม่ติดลบ')