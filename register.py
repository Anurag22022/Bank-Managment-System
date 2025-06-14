#User sign IN/UP page
from database import *
from customer import *
from bank import Bank
import random
def SignUp():
    username=input("Create username: ")
    temp=db_query(f"SELECT username FROM customers where username ='{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        name=input("Enter your name again: ")
        password=input("Enter your password: ")
        age=int(input("Enter your age: "))
        city=input("Enter your city: ")
        while True:
            account_number=random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(f"Your Account Number is: {account_number}")
                break
        db_execute(f"""
            INSERT INTO customers (account_number, username, password, name, age, city, balance ,status)
            VALUES ({account_number}, '{username}', '{password}', '{name}', {age}, '{city}', 0 ,True)
        """)
        print("Account created successfully!")

    bobj = Bank(username,account_number)
    bobj.create_transaction()  

def SignIn():
    while True:
        username = input("Enter username: ")
        temp = db_query(f"SELECT password, account_number FROM customers WHERE username = '{username}';")
        if not temp:
            print("Invalid username. Try again.")
            continue

        # Password check
        for _ in range(3):  # Allow 3 tries
            password = input(f"Welcome {username}, enter password: ")
            if temp[0][0] == password:
                print("Sign-in successful!")
                account_number = temp[0][1]  # Fetch the account number after successful login
                return username, account_number  # Return both username and account number
            else:
                print("Wrong Password. Try again.")
        print("Too many failed attempts. Exiting login.")
        return None, None  # If login fails

