import mysql.connector
class manageDb:
    def __init__(self,host,user,password,database):
        self.mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            use_pure = True
        )
        self.mycursor = self.mydb.cursor()

    def selectdb(self,table):
        sql = f"select * from {table}"
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show

    def insert_product(self,product_id,product_name,description,price,stock):
        sql = "insert into products values (%s ,%s ,%s ,%s ,%s)"
        val_sql = (product_id,product_name,description,price,stock)
        self.mycursor.execute(sql,val_sql)
        self.mydb.commit()
        if mycursor.rowcount > 0 :
            return True
        else:
            return False

    def insert_user(self,user_id,username,password,email,user_role):
        sql = "insert into products values (%s ,%s ,%s ,%s ,%s)"
        val_sql = (user_id,username,password,email,user_role)
        self.execute(sql,val_sql)
        self.mydb.commit()
        if self.rowcount > 0 :
            return True
        else:
            return False

    def insert_order(self,order_id,user_id,order_date,total_amount,status,product_id):
        sql = "insert into products values (%s ,%s ,%s ,%s ,%s ,%s)"
        val_sql = (order_id,user_id,order_date,total_amount,status,product_id)
        self.execute(sql,val_sql)
        self.mydb.commit()
        if self.rowcount > 0 :
            return True
        else:
            return False

    def insert_category(self,category_id,category_name):
        sql = "insert into products values (%s ,%s)"
        val_sql = (category_id,category_name)
        self.execute(sql,val_sql)
        self.mydb.commit()
        if self.rowcount > 0 :
            return True
        else:
            return False

    def delete(self,table,where,id):
        sql=f"delete from {table} where {where} = %s "
        val_sql = (id,)
        self.execute(sql,val_sql)
        self.mydb.commit()
        if self.rowcount > 0 :
            return True
        else:
            return False
    def editdb(self,table,column,val,idname,id):
        sql=f"update {table} set {column} = %s where {idname} = %s "
        val_sql = (val,id,)
        self.execute(sql,val_sql)
        self.mydb.commit()
        if self.rowcount > 0 :
            return True
        else:
            return False
        
shop_db = manageDb('localhost','root','1234','market')

print(shop_db.selectdb('users'))