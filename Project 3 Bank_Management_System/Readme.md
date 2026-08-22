# 🏦 Bank Account Management System

A simple **command-line Bank Account Management System** built in Python using **Object-Oriented Programming (OOP)**. This project simulates real-world banking operations like account creation, deposits, withdrawals, PIN verification, and transaction history — all managed in memory during runtime.

## 📌 Features

- **Create Account** — Register a new account with name, account number, PIN, and initial balance
- **Deposit** — Add funds to an account (with input validation)
- **Withdraw** — Withdraw funds with insufficient balance protection
- **Display Account Details** — View name, account number, and current balance
- **Transaction History** — View a full log of all deposits and withdrawals
- **PIN Authentication** — Every sensitive operation requires PIN verification
- **Multiple Accounts** — Manage multiple accounts simultaneously using a dictionary
- **Menu-Driven Interface** — Simple, loop-based CLI menu for easy navigation

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts Used:** Object-Oriented Programming (Classes, Constructors, Encapsulation), Dictionaries, Loops, Conditional Statements, Input Validation, f-strings

## 📂 Project Structure

```
bank-account-management-system/
│
├── main_bank.py     # Main program file (Account & Bank classes + program entry point)
└── README.md        # Project documentation
```

## 🧠 How It Works

The project is built using two main classes:

### `Account` Class
Represents a single bank account and handles all account-level operations:
- `__init__()` — Initializes account details (name, account number, PIN, balance, transaction history)
- `verify_pin()` — Checks if the entered PIN matches the account's PIN
- `deposit()` — Adds money to the account with amount validation
- `withdraw()` — Deducts money with balance and amount validation
- `display()` — Prints account details
- `show_transactions()` — Prints the full transaction history

### `Bank` Class
Manages all accounts and drives the program:
- `__init__()` — Initializes an empty dictionary to store all accounts
- `create_account()` — Creates a new `Account` object and stores it
- `authenticate()` — Finds an account by number and verifies the PIN (reused across deposit, withdraw, display, and transaction operations)
- `run()` — Runs the main menu loop until the user exits

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/shanzailarif012-jpg/<repo-name>.git
   ```
2. Navigate into the project folder:
   ```bash
   cd <repo-name>
   ```
3. Run the program:
   ```bash
   python main_bank.py
   ```

## 🎮 Menu Options

```
1. Create Account
2. Deposit
3. Withdraw
4. Display
5. Transactions
6. Exit
```

## 💡 Example Usage

```
Banking Management System
Menu Options
1. Create Account
2. Deposit
3. Withdraw
4. Display
5. Transactions
6. Exit
Enter Choice Number: 1
Enter Your Name: Shanzail
Enter Your Account_Number: 1001
Enter Pin Number: 1234
Enter Initial Balance: 500
Account Created Successfully
```

## ⚠️ Known Limitations

- Data is stored **only in memory** — all accounts and transactions are lost when the program is closed (no file/database persistence yet)
- No handling for non-numeric input (e.g., entering letters where a number is expected will crash the program)
- No minimum balance requirement enforced

## 🚀 Future Improvements

- [ ] Add persistent storage using **JSON** or **SQLite**
- [ ] Add `try/except` error handling for invalid inputs
- [ ] Add minimum balance and daily withdrawal limits
- [ ] Add interest calculation for savings accounts
- [ ] Build a GUI or web interface (Tkinter / Flask)

## 👤 Author

**Shanzail Arif**
Part of ongoing Python learning journey — 100 Days of Code challenge & DecodeLabs Python Internship (Batch 2026)

GitHub: [@shanzailarif012-jpg](https://github.com/shanzailarif012-jpg)

## 📄 License

This project is open source and available for learning purposes.