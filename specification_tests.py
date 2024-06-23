"""
Author: Lucas Becker
Date: 06/23/2024
Class: 330
Description: This file contains unittests for the Banking DSL.
Pledge: This work is all my own with the help of Jayce.
"""

import unittest
from bank_account import BankAccount
from my_lexer import Lexer
from my_parser import Parser
from my_token import Token, TokenType
from interpreter import Interpreter
import re

class TestBankingDSL(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Dawn", "Duerre", 100000000.00)

    def test_initial_balance(self):
        expected = 100000000.00
        result = self.account.balance
        self.assertEqual(result, expected, f"FAIL: Initial balance should be {expected}, but got {result}.")
        print(f"PASS: Initial balance test. Expected: {expected}, Got: {result}")

    def test_deposit(self):
        self.account.deposit(500000)
        expected = 100500000.00
        result = self.account.balance
        self.assertEqual(result, expected, f"FAIL: Balance after depositing 500000 should be {expected}, but got {result}.")
        print(f"PASS: Deposit test. Expected: {expected}, Got: {result}")

    def test_withdraw(self):
        self.account.withdraw(500000)
        expected = 99500000.00
        result = self.account.balance
        self.assertEqual(result, expected, f"FAIL: Balance after withdrawing 500000 should be {expected}, but got {result}.")
        print(f"PASS: Withdraw test. Expected: {expected}, Got: {result}")

    def test_account_number(self):
        account_number_pattern = re.compile(r"^[A-Z]{2}\d{6}$")
        result = self.account.account_number
        self.assertTrue(account_number_pattern.match(result), f"FAIL: Account number '{result}' is not in the correct format 'XX123456'.")
        print(f"PASS: Account number test. Got: {result}")

def specification_tests():
    print("Running specification tests...")
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBankingDSL))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")
        for failure in result.failures:
            print(failure[1])
        for error in result.errors:
            print(error[1])

if __name__ == '__main__':
    specification_tests()
