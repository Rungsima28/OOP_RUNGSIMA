class Library:
    def __init__(self):
        self.namebook = []
    def add_book(self):
        while True:
            choice = input("พิมพ์ add เพื่อมเพิ่ม พิมพ์ exit เพื่อออก : ")
            if choice == 'add' :
                bookname = str(input('ใส่ชื่อหนังสือ : '))
                self.namebook.append(bookname)
            elif choice == 'exit':
                break
    def show_books(self):
        print("รายชื่อหนังสื่อในห้องสมุด : ")
        for show_book in self.namebook:
            print(show_book)
    def find_book(self):
        bookname = str(input('ค้นหาชื่อ : '))
        for i in self.namebook:
            if bookname == i :
                print(i)
Lib = Library()
Lib.add_book()
Lib.show_books()
Lib.find_book()
print(Lib.namebook)
    