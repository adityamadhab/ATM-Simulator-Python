import tkinter as tk
from tkinter import messagebox, simpledialog


class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")

        # Increase the size of the main window
        self.root.geometry("500x400")

        # Create a frame for the ATM interface with a light gray background
        self.frame = tk.Frame(root, bg="light gray")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create labels for account number and PIN with a larger font
        tk.Label(self.frame, text="Account Number:", bg="light gray", font=("Helvetica", 14)).grid(row=0, column=0)
        tk.Label(self.frame, text="PIN:", bg="light gray", font=("Helvetica", 14)).grid(row=1, column=0)

        # Create account number and PIN input fields with a larger font
        self.account_entry = tk.Entry(self.frame, font=("Helvetica", 14))
        self.account_entry.grid(row=0, column=1)
        self.pin_entry = tk.Entry(self.frame, show="*", font=("Helvetica", 14))
        self.pin_entry.grid(row=1, column=1)

        # Create buttons for login, create account, deposit, withdraw, display balance, and exit with a larger font
        self.login_button = tk.Button(self.frame, text="Login", command=self.login, bg="green", fg="white", font=("Helvetica", 14))
        self.login_button.grid(row=2, column=0, pady=10)

        self.create_account_button = tk.Button(self.frame, text="Create Account", command=self.create_account, bg="blue", fg="white", font=("Helvetica", 14))
        self.create_account_button.grid(row=2, column=1, pady=10)

        self.deposit_button = tk.Button(self.frame, text="Deposit", command=self.deposit, bg="green", fg="white", font=("Helvetica", 14))
        self.deposit_button.grid(row=3, column=0, pady=10)

        self.withdraw_button = tk.Button(self.frame, text="Withdraw", command=self.withdraw, bg="red", fg="white", font=("Helvetica", 14))
        self.withdraw_button.grid(row=3, column=1, pady=10)

        self.balance_button = tk.Button(self.frame, text="Display Balance", command=self.display_balance, bg="purple", fg="white", font=("Helvetica", 14))
        self.balance_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=root.quit, bg="red", fg="white", font=("Helvetica", 14))
        self.exit_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Create an ATM instance
        self.atm = ATM()
        self.balance = None

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()
        result, balance = self.atm.login(account_number, pin)
        messagebox.showinfo("Login Result", result)
        if balance is not None:
            self.balance = balance

    def create_account(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()
        result = self.atm.create_account(account_number, pin)
        messagebox.showinfo("Account Creation", result)

    def deposit(self):
        deposit_amount = float(simpledialog.askstring("Deposit", "Enter the deposit amount in Rs:"))
        account_number = self.account_entry.get()
        result, balance = self.atm.custom_deposit(account_number, deposit_amount)
        messagebox.showinfo("Deposit Result", result)
        if balance is not None:
            self.balance = balance

    def withdraw(self):
        withdraw_amount = float(simpledialog.askstring("Withdraw", "Enter the withdrawal amount in Rs:"))
        account_number = self.account_entry.get()
        result, balance = self.atm.custom_withdraw(account_number, withdraw_amount)
        messagebox.showinfo("Withdrawal Result", result)
        if balance is not None:
            self.balance = balance

    def display_balance(self):
        if self.balance is not None:
            messagebox.showinfo("Balance", f"Balance (Rs): {self.balance:.2f}")
        else:
            messagebox.showinfo("Balance", "Please log in to check your balance.")


class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number not in self.accounts:
            account = Account(account_number, pin, 0)
            self.accounts[account_number] = account
            return "Account created successfully."
        else:
            return "Account already exists."

    def login(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return "Login successful.", self.accounts[account_number].balance
        else:
            return "Invalid account number or PIN.", None

    def custom_deposit(self, account_number, custom_amount):
        if account_number in self.accounts and custom_amount > 0:
            self.accounts[account_number].balance += custom_amount
            return f"Deposit of Rs {custom_amount:.2f} successful.", self.accounts[account_number].balance
        else:
            return "Invalid account number or amount.", None

    def custom_withdraw(self, account_number, custom_amount):
        if account_number in self.accounts and 0 < custom_amount <= self.accounts[account_number].balance:
            self.accounts[account_number].balance -= custom_amount
            return f"Withdrawal of Rs {custom_amount:.2f} successful.", self.accounts[account_number].balance
        else:
            return "Invalid account number, insufficient funds, or invalid amount.", None


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
