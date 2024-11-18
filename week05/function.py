def sumall(num1,num2):
    a = []
    for i in range (num1,num2+1):
        if i % 3 != 0:
            a.append(i)
    return a