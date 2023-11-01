# ATM-Simulator-Python

<h3>Expalination of the Code</h3>

1. Imports:
We import the necessary modules from the 'tkinter' library. 'tkinter' is used to create graphical user interfaces (GUIs) in Python.
'messagebox' is used to display pop-up messages to the user, and 'simpledialog' is used for user input dialogs.

2. Class Definitions:
<b>ATMApp</b>: This class represents the main application. It's responsible for creating the GUI and handling user interactions. It contains methods for logging in, creating accounts, depositing, withdrawing, displaying balances, and managing the GUI components.

<b>Account</b>: This class represents a bank account. It has attributes such as the account number, PIN (Personal Identification Number), and balance. Account objects are created to store account information.

<b>ATM</b>: This class represents an ATM machine. It manages a collection of bank accounts, allowing for login, account creation, deposits, and withdrawals. It also enforces security checks such as verifying account numbers and PINs.

3. Initialize the Main Window: We create the main application window using tk.Tk(). This window serves as the primary user interface for the ATM simulator.
   
4. ATMApp: The ATMApp class is instantiated as app, and it becomes the core of the GUI.

5. Create GUI Components: Inside ATMApp, we create various GUI components such as labels, entry fields, buttons, and a frame. These elements make up the ATM interface that the user interacts with.

6. Login and Account Creation:Two buttons are provided for the user to either log in with their account number and PIN or create a new account. These buttons trigger actions defined in the login and create_account methods when clicked.

7. Deposit and Withdrawal: Additional buttons are created for depositing and withdrawing money. These buttons initiate deposit and withdrawal operations when clicked. User input is requested for the transaction amounts.

8. Display Balance Button: A "Display Balance" button is added to allow the user to check their account balance. When clicked, this button shows a pop-up message with the account balance.

9. Exit Button: An "Exit" button is provided to close the ATM application.

10. ATM Operations: The ATM class manages ATM operations. It handles account creation, login, custom deposits, and custom withdrawals. Security checks are performed during login, including verification of account numbers and PINs. Custom deposits and withdrawals are processed, with validations for valid account numbers, sufficient funds, and positive transaction amounts.

11. Application Execution: Finally, the main application is executed with root.mainloop(), which starts the GUI interface, allowing the user to interact with the ATM simulator.


The code essentially creates a GUI-based ATM simulator that allows users to log in, create accounts, deposit or withdraw money, check their account balances, and exit the application. It uses the tkinter library for creating the graphical interface, and user interactions are handled through various methods in the ATMApp class, while account management is handled by the ATM class.
