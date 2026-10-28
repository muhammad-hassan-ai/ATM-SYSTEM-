# Simple Python ATM System

This is a simple command-line ATM system I built to practice Python.

## Features
- Login with Account Number & PIN
- Create New Account with auto-generated Account Number
- Check Balance
- Deposit Money
- Withdraw Money with limit check (50,000) and balance check
- Data Persistence using JSON file (`account.json`)

## How to Run

```bash
python ATM1.py
```

## Example Output

```text
--- ATM SYSTEM ---
1. Login
2. Create New Account

> Choose: 1
Enter Account Number: 501
Enter PIN: 1011
Login Successful
Welcome Hassan

1. Check Balance
2. Deposit
3. Withdrawal
4. Logout

> Choose: 1
Your balance is: 1900
```

## Default Test Accounts
- 501 | Hassan | PIN: 1011 | Balance: 1900
- 502 | shayan | PIN: 1234 | Balance: 800
- 503 | yousaf | PIN: 3344 | Balance: 200

## What I Learned
- Using `json` module to store and load data
- Using `os` module to check if file exists
- Using `random` module to generate account numbers
- Creating and using functions in Python
- Taking user input and type casting
- Using if/elif/else conditions
- Error handling with try/except
- Using loops and dictionaries
- Clean code structure

## Files
- `ATM1.py` - Main ATM logic
- `account.json` - Auto-created file to save accounts data (after first run)

---
Part of my Python learning journey on GitHub.
