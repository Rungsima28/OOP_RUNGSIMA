import random
print("โปรเเกรมเป่ายิงฉุบ")
w = 0
f = 0
while True:
    b = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(b)
    print("เลือก ค้อน กรรไกร กระดาษ ")
    a = str(input("คุณเลือก :"))
    if a == b :
        print("เสมอ") 
    elif a == "ค้อน" and b == "กรรไกร" :
        print("ชนะ")
    elif a == "กรรไกร" and b == "กระดาษ" :
        print("ชนะ")
    elif a == "กระดาษ" and b == "ค้อน" :
        print("ชนะ")
    else:
        print("เเพ้")
        f += 1
print(f"")
