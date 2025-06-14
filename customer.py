#Customer Details
from database import *
class Customer:
    def __int__(self,username,password,name,age,city,account_number,balance=0):
        self.username=username
        self.password=password
        self.name=name
        self.age=age
        self.city=city
        self.account_number=account_number
        self.balance = balance
        
    def createuser(self):
        db_query(f"INSERT INTO customers VALUES ('{self.username}','{self.password}','{self.name}','{self.age}','{self.city}','{self.account_number}''{self.balance}','True');")
        mydb.commit()