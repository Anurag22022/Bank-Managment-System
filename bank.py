#Bank Services
from database import *
class Bank:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number
    #Balance Enquiry
    def show_balance(self):
        result = db_query(f"SELECT balance FROM customers WHERE username = '{self.username}'")
        if result:
            print(f"Your current balance is: {result[0][0]}")
        else:
            print("Error: Unable to fetch balance.")
    

    #Cash Deposit
    def deposit(self, amount):
        if amount > 0:
            db_execute(f"UPDATE customers SET balance = balance + {amount} WHERE username = '{self.username}'")
            print(f"Successfully deposited {amount}.")
            self.create_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive.")
    

    # Cash Withdraw
    def withdraw(self, amount):
        result = db_query(f"SELECT balance FROM customers WHERE username = '{self.username}'")
        if result and result[0][0] >= amount:
            db_execute(f"UPDATE customers SET balance = balance - {amount} WHERE username = '{self.username}'")
            print(f"Successfully withdrew {amount}.")
            self.create_transaction("Withdraw", amount)
        else:
            print("Insufficient funds or invalid amount.")


    #Fund Transfer
    def transfer_funds(self, to_account, amount):
        result = db_query(f"SELECT balance FROM customers WHERE username = '{self.username}'")
        if result and result[0][0] >= amount:
            # Check if the recipient account exists
            recipient = db_query(f"SELECT account_number FROM customers WHERE account_number = {to_account}")
            if recipient:
                # Proceed with the transfer
                db_execute(f"UPDATE customers SET balance = balance - {amount} WHERE username = '{self.username}'")
                db_execute(f"UPDATE customers SET balance = balance + {amount} WHERE account_number = {to_account}")
                print(f"Successfully transferred {amount} to account {to_account}.")
                self.create_transaction(f"Transfer to {to_account}", amount)
            else:
                print("Recipient account does not exist.")
        else:
            print("Insufficient funds or invalid amount.")


    #Transaction Table
    def create_transaction(self, txn_type, amount):
        query = f"""
        INSERT INTO transactions (username, type, amount)
         VALUES (%s, %s, %s)
    """
        db_execute(query, (self.username, txn_type, amount))

   #Transaction history
    def show_transaction_history(self):
        query = "SELECT * FROM transactions WHERE username = %s ORDER BY timestamp DESC"
        result = db_fetch(query, (self.username,))
        for row in result:
            print(row)
