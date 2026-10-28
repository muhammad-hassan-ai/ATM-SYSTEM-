# using json module to store data in json file
import json
# using os moudle to check file 
import os 
# using random module to generate random account number
import random


File = "account.json"

if os.path.exists(File):
    with open(File,"r") as f:
        data=json.load(f)
        accounts = {int(k):v for k,v in data.items()}
else:
    accounts={ 
                501:{"name":"Hassan", "pin" : 1011 , "balance":1900},
                502:{"name":"shayan", "pin" : 1234 , "balance": 800},
                503:{"name":"yousaf", "pin" : 3344 , "balance":200},
    }

# Save Function
def save():
    with open(File,"w")as f:
        json.dump(accounts,f,indent=2)


# Login Function
def login():
    try:
        account_number = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))
        if account_number in accounts and pin == accounts[account_number]["pin"]:
            print("Login Successful")
            print("Welcome", accounts[account_number]["name"])
            return account_number
        else:
            print("Account Not Found.Please check your account number , pin and try again.")
        return None
    except ValueError:
        print("Invalid input.")


# Create New Account Function 
def create_account():
     try:
        name = (input("Enter Your Full Name: "))
        while True:
            account_number = random.randint(500,9990)
            if account_number not in accounts:
                 break
            
        pin = int(input("Enter Your PIN:"))
        first_deposit = float(input("Deposit Amount if not enter 0: "))
     except ValueError:
          print("Enter a valid PIN CODE. ")
          return None
     accounts[account_number]={"name":name,"pin":pin,"balance":first_deposit}  
     save()
     print("Account Created Successfully")
     print(f"Your Account Number: {account_number}")


# Check Balance Funtion 
def check_balance(account_number):
    print(f"Your balance is: {accounts[account_number]['balance']}")


# Deposit Function
def deposit(account_number):
    try:
        deposit_amount = float(input("Enter Amount to Deposit: "))
        if deposit_amount <= 0:
            print("Deposit Amount must be greater than zero")
        else:

            accounts[account_number]["balance"] += deposit_amount
            save()
            print(f"Deposit Successful your new balance is: {accounts[account_number]['balance']}")
    except ValueError:
        print("Invalid Amount.")


# Withdrawal Function
def Withdrawl(account_number):
    try:
        withdraw = float(input("Enter Amount to Withdraw: "))
        if(withdraw<=0):
            print("Withdrawl amount must be greater than zero")

        elif(withdraw>50000):
            print("your withdrawl limit is 50000")

        elif(withdraw>accounts[account_number]["balance"]):
            print("Insufficient Balance")

        else:
            accounts[account_number]["balance"] -= withdraw
            save()
            print(f"Withdrawl Successful your remainig balance is: {accounts[account_number]['balance']}")
    except ValueError:
        print("Invalid Amount. Please Enter valid amount to withdraw")


# First menu for user to login or create new account
while True:
    print('\n--- ATM SYSTEM ---')
    print("1. Login  ")
    print("2. Create New Account")

    try:
        ch = int(input("\n> Choose: "))

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # IF ELSE FOR FIRST MENU 
    if ch == 1:
        account_number = login()
        if account_number:
            # SECOND MENU WITH LOOP AFTER SUCCESSFUL LOGIN
            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdrawal")
                print("4. Logout")

                try:
                        user_choice = int(input("\n> Choose:"))

                except ValueError:
                    print("Invalid input." )
                    continue

                if(user_choice == 1):
                        check_balance(account_number)
                elif(user_choice == 2):
                        deposit(account_number)
                elif(user_choice == 3):
                        Withdrawl(account_number)
                elif(user_choice == 4):
                    break
                else:
                        print("Invalid option. Please choose a valid option.")
    
    elif ch == 2:
         create_account()

    
    else:
        print("Invalid option. Please choose a valid option.")




