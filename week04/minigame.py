import random
print('เกมเป่ายิงฉุบ')
win = 0
lose = 0
always = 0
for รอบ in range(1,5+1):
    bot = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print('-----------------------------')
    print(bot)
    print("เลือก ค้อน กรรไกร กระดาษ")
    player = str(input("คุณเลือก :"))
    if player == bot :
        always += 1
        print("เสมอ")
    elif (player == "ค้อน" and bot == "กรรไกร"):
        win += 1
        print("ชนะ")
    elif (player == "กระดาษ" and bot == "ค้อน"):
        win += 1
        print("ชนะ")
    elif (player == "กรรไกร" and bot == "กระดาษ"):
        win += 1
        print("ชนะ")
    else :
        lose += 1
        print("แพ้")
print(f"เล่นเสร็จสิ้น!! ชนะทั้งหมด: {win} แพ้ทั้งหมด: {lose} เสมอทั้งหมด: {always}")