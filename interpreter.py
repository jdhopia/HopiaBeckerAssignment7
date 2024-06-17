class Interpreter:
    def __init__(self, ast, account_dict):
        self.ast = ast
        self.account_dict = account_dict

    def interpret(self):
        print("AST:", self.ast)
        print("Accounts:", self.account_dict)
