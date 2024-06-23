"""
Author: Lucas Becker and Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the main program for the Banking DSL.
Pledge: This is all our own work.
"""

from my_lexer import Lexer
from my_parser import Parser
from interpreter import Interpreter
from bank_account import BankAccount
import specification_tests

def initialize_accounts():
    """
    Creates and returns a list of initial bank accounts with predefined account numbers.
    """
    accounts = [
        BankAccount("Dawn", "Duerre", 100000000.00, "DD123456"),
        BankAccount("Jayce", "Hopia", 500.00, "JH234567"),
        BankAccount("Lucas", "Becker", 1500.00, "LB345678"),
        BankAccount("Susan", "Furtney", 2000.00, "SF456789"),
        BankAccount("Golden", "Bear", 750.00, "GB567890")
    ]
    return accounts

def display_accounts(accounts):
    """
    Displays the list of accounts with their IDs.
    """
    print("\n--- List of Accounts ---")
    for account in accounts:
        print(f"ID: {account.account_number}, Name: {account.first_name} {account.last_name}, Balance: {account.balance}")

def display_menu(accounts):
    """
    Displays the banking menu and handles user interactions.
    """
    account_dict = {account.account_number: account for account in accounts}

    while True:
        display_accounts(accounts)
        print("\n--- Banking Menu ---")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. Check balance")
        print("4. Log out of account")
        print("5. Check another account")
        print("6. Create a new account")
        print("7. Run specification tests")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_id = input("Enter account ID: ")
            if account_id in account_dict:
                amount = float(input("Enter amount to deposit: "))
                account_dict[account_id].deposit(amount)
                print(f"Deposited {amount} to account {account_id}.")
            else:
                print("Account not found.")
        elif choice == '2':
            account_id = input("Enter account ID: ")
            if account_id in account_dict:
                amount = float(input("Enter amount to withdraw: "))
                try:
                    account_dict[account_id].withdraw(amount)
                    print(f"Withdrew {amount} from account {account_id}.")
                except ValueError as e:
                    print(e)
            else:
                print("Account not found.")
        elif choice == '3':
            account_id = input("Enter account ID: ")
            if account_id in account_dict:
                print(f"Balance of account {account_id}: {account_dict[account_id].balance}")
            else:
                print("Account not found.")
        elif choice == '4':
            print("Logged out.")
            continue
        elif choice == '5':
            continue
        elif choice == '6':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            balance = float(input("Enter initial balance: "))
            new_account = BankAccount(first_name, last_name, balance)
            account_dict[new_account.account_number] = new_account
            accounts.append(new_account)
            print(f"Created new account {new_account.account_number} for {first_name} {last_name} with balance {balance}.")
        elif choice == '7':
            specification_tests.specification_tests()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main function to initialize accounts and display the menu.
    """
    accounts = initialize_accounts()
    display_menu(accounts)

if __name__ == "__main__":
    main()
