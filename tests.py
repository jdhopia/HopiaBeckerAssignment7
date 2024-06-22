import unittest
from bank_account import BankAccount
from lexer import Lexer
from parser import Parser
from token import Token
from ast_node import ASTNode
from interpreter import Interpreter

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John", "Doe", 500)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 500)

    def test_deposit(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 200)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(600)

    def test_account_number(self):
        self.assertEqual(self.account.account_number[:2], "JD")
        self.assertEqual(len(self.account.account_number), 8)

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        lexer = Lexer("create deposit withdraw balance")
        tokens = lexer.tokenize()
        expected_tokens = [
            Token("IDENTIFIER", "create"),
            Token("IDENTIFIER", "deposit"),
            Token("IDENTIFIER", "withdraw"),
            Token("IDENTIFIER", "balance")
        ]
        self.assertEqual(tokens, expected_tokens)

class TestParser(unittest.TestCase):
    def test_parse(self):
        lexer = Lexer("create deposit")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(len(ast.children), 2)
        self.assertEqual(ast.children[0].token.value, "create")
        self.assertEqual(ast.children[1].token.value, "deposit")

class TestInterpreter(unittest.TestCase):
    def test_interpret(self):
        lexer = Lexer("create deposit withdraw")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        with self.assertLogs() as log:
            interpreter.interpret()
            self.assertIn("Executing create", log.output[0])
            self.assertIn("Executing deposit", log.output[1])
            self.assertIn("Executing withdraw", log.output[2])

if __name__ == '__main__':
    unittest.main()
