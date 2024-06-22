from bank_account import BankAccount
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    accounts = [
        BankAccount("Alice", "Smith", 1000),
        BankAccount("Bob", "Brown", 1500),
        BankAccount("Charlie", "Davis", 2000)
    ]

    lexer = Lexer("create deposit withdraw balance")
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter(ast)
    interpreter.interpret()

    for account in accounts:
        print(account)

if __name__ == "__main__":
    main()
