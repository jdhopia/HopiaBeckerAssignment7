"""
Author: Lucas Becker
Date: 06/23/2024
Class: 330
Description: This file contains the Interpreter class for the Banking DSL.
Pledge: This work is all my own with the help of Jayce.
"""

from ast_node import ASTNode
from bank_account import BankAccount

###################################
#####    INTERPRETER CLASS    #####
###################################

class Interpreter:
    def __init__(self, ast: ASTNode):
        # Initializes the interpreter with the given AST.
        self.ast = ast
        self.accounts = {}

    def interpret(self):
        # Interprets the AST.
        for node in self.ast:
            self._execute_node(node)

    def _execute_node(self, node: ASTNode):
        # Executes the given AST node based on its type.
        if node.node_type == "CreateAccount":
            self._create_account(node)
        elif node.node_type == "Deposit":
            self._deposit(node)
        elif node.node_type == "Withdraw":
            self._withdraw(node)
        elif node.node_type == "Balance":
            self._balance(node)
        elif node.node_type == "Exit":
            print("Exit command received")
            return "Exit"

    def _create_account(self, node):
        # Creates a new bank account.
        first_name = node.children[0].value
        last_name = node.children[1].value
        account_number = node.children[2].value
        balance = float(node.children[3].value)
        if account_number in self.accounts:
            raise ValueError("Account number already exists")
        self.accounts[account_number] = BankAccount(first_name, last_name, balance)

    def _deposit(self, node):
        # Deposits the given amount into the specified account.
        amount = float(node.children[0].value)
        account_number = node.children[1].value
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        self.accounts[account_number].deposit(amount)

    def _withdraw(self, node):
        # Withdraws the given amount from the specified account.
        amount = float(node.children[0].value)
        account_number = node.children[1].value
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        self.accounts[account_number].withdraw(amount)

    def _balance(self, node):
        # Prints the balance of the specified account.
        account_number = node.children[0].value
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        print(f"Balance of {account_number}: {self.accounts[account_number].balance}")
