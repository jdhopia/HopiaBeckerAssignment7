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

    while True:
        print("Available accounts:")
        for acc in accounts:
            print(f"{acc.account_number}: {acc.first_name} {acc.last_name}")

        print("Enter your command (or type 'exit' to quit):")
        user_input = input()

        if user_input.lower() in ["exit", "quit", "end"]:
            break

        lex = lexer.Lexer(user_input)
        tokens = lex.tokenize()
        parse = parser.Parser(tokens)
        ast = parse.parse()
        interp = interpreter.Interpreter(ast, account_dict)
        interp.interpret()

        print("Would you like to perform another operation? (yes/no)")
        if input().lower() != 'yes':
            break

    print("Program exited.")

if __name__ == "__main__":
    main()
