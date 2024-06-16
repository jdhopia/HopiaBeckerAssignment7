import lexer
import parser
import interpreter
from bank_account import BankAccount

def initialize_accounts():
    accounts = [
        BankAccount("Dawn", "Duerre", "DD000001", 1000000),
        BankAccount("Jayce", "Hopia", "JH000002", 1500),
        BankAccount("Lucas", "Becker", "LB000003", 2000),
        BankAccount("Susan", "Furtney", "SF000004", 1750),
        BankAccount("Golden", "Bear", "GB000005", 10000),
    ]
    return accounts

def main():
    accounts = initialize_accounts()
    account_dict = {acc.account_number: acc for acc in accounts}
    print("Program exited.")

if __name__ == "__main__":
    main()
