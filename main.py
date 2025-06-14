from register import *
from database import create_transactions_table

print("Welcome to Trusted Express Bank")

# Ask user to sign in first
signed_in = False

while not signed_in:
    try:
        choice = int(input("1. SignUp\n2. SignIn\n3. Exit\nChoose an option: "))
        
        if choice == 1:
            SignUp()
        elif choice == 2:
            username, account_number = SignIn()
            if username and account_number:
                bobj = Bank(username, account_number)  # Create bobj after successful sign-in
                signed_in = True
            else:
                print("Sign-in failed. Please try again.")
        elif choice == 3:
            print("Thank you for using Trusted Express Bank!")
            exit()
        else:
            print("Please enter a valid option (1, 2, or 3).")
    except ValueError:
        print("Invalid input. Please enter a number.")

# After SignIn, show the main menu:
while True:
    print("\nMain Menu: ")
    print("1. Balance Enquiry")
    print("2. Cash Deposit")
    print("3. Cash Withdraw")
    print("4. Fund Transfer")
    print("5. Logout")
    
    try:
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            # Call Balance Enquiry
            bobj.show_balance()
        elif choice == 2:
            # Call Cash Deposit
            amount = int(input("Enter amount to deposit: "))
            bobj.deposit(amount)
        elif choice == 3:
            # Call Cash Withdraw
            amount = int(input("Enter amount to withdraw: "))
            bobj.withdraw(amount)
        elif choice == 4:
            # Call Fund Transfer
            to_account = int(input("Enter the account number to transfer to: "))
            amount = int(input("Enter amount to transfer: "))
            bobj.transfer_funds(to_account, amount)
        elif choice == 5:
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


create_transactions_table()