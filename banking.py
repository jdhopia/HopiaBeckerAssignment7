import lexer
import parser
import interpreter
from bank_account import BankAccount

def initialize_accounts():
    accounts = [
        BankAccount("Alice", "Smith", "AlSm000001", 1000),
        BankAccount("Bob", "Brown", "BoBr000002", 1500),
        BankAccount("Charlie", "Davis", "ChDa000003", 2000),
        BankAccount("Diana", "Evans", "DiEv000004", 2500),
        BankAccount("Ethan", "Fisher", "EtFi000005", 3000),
    ]
    return accounts

def main():
    accounts = initialize_accounts()
    account_dict = {acc.account_number: acc for acc in accounts}
    print("Program exited.")

if __name__ == "__main__":
    main()
