sum = 0
while True:
        try :
            num = (input('ราคาสินค้า :'))
            if num == 'exit':
                print(f'ยอดขายรวมทั้งหมด = {sum}')
                break
            num = int(num)
            if num  == 0 :
                raise (ZeroDivisionError)
            elif num < 0 :
                raise (Exception) 
            else:
                sum += num
                print(sum)
        except ValueError:
            print('กรุณาใส่ตัวเลขเท่านั้น')
        except ZeroDivisionError:
            print('ราคาสินค้าต้องมากกว่า 0')
        except :
             print('ราคาสินค้าต้องไม่ติดลบ')
            
