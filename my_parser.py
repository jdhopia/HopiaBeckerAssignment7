"""
Author: Lucas Becker   
Date: 06/24/2024
Class: 330
Description: This file contains the Parser class for the Banking DSL.
Pledge: This is my own work with the help of Jayce.
"""

from ast_node import ASTNode
from my_token import TokenType

###################################
#####      PARSER CLASS       #####
###################################

class Parser:
    # intializes the parser with the list of tokens
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        # parses the tokes into AST nodes list
        statements = []
        while self.current_token().token_type != TokenType.EOF:
            if self.current_token().token_type == TokenType.KEYWORD:
                if self.current_token().value.upper() == "CREATE":
                    statements.append(self._parse_create_account())
                elif self.current_token().value.upper() == "DEPOSIT":
                    statements.append(self._parse_deposit())
                elif self.current_token().value.upper() == "WITHDRAW":
                    statements.append(self._parse_withdraw())
                elif self.current_token().value.upper() == "BALANCE":
                    statements.append(self._parse_balance())
                elif self.current_token().value.upper() == "EXIT":
                    statements.append(self._parse_exit())
            else:
                raise ValueError(f"Unexpected token: {self.current_token()}")
        print("AST:", statements)  # Print AST
        return statements

    def _parse_create_account(self):
        # parses through CREATE ACCOUNT statement
        self._consume(TokenType.KEYWORD)  # CREATE
        self._consume(TokenType.KEYWORD)  # ACCOUNT
        first_name = self._consume(TokenType.NAME).value
        self._consume(TokenType.COMMA)
        last_name = self._consume(TokenType.NAME).value
        self._consume(TokenType.COMMA)
        account_number = self._consume(TokenType.NAME).value
        self._consume(TokenType.COMMA)
        balance = self._consume(TokenType.NUMBER).value
        node = ASTNode("CreateAccount")
        node.add_child(ASTNode("FirstName", first_name))
        node.add_child(ASTNode("LastName", last_name))
        node.add_child(ASTNode("AccountNumber", account_number))
        node.add_child(ASTNode("Balance", balance))
        return node

    def _parse_deposit(self):
        # parses through deposit statement
        self._consume(TokenType.KEYWORD)  # DEPOSIT
        amount = self._consume(TokenType.NUMBER).value
        self._consume(TokenType.KEYWORD)  # TO
        account_number = self._consume(TokenType.NAME).value
        node = ASTNode("Deposit")
        node.add_child(ASTNode("Amount", amount))
        node.add_child(ASTNode("AccountNumber", account_number))
        return node

    def _parse_withdraw(self):
        # parses through withdraw statement
        self._consume(TokenType.KEYWORD)  # WITHDRAW
        amount = self._consume(TokenType.NUMBER).value
        self._consume(TokenType.KEYWORD)  # FROM
        account_number = self._consume(TokenType.NAME).value
        node = ASTNode("Withdraw")
        node.add_child(ASTNode("Amount", amount))
        node.add_child(ASTNode("AccountNumber", account_number))
        return node

    def _parse_balance(self):
        # parses through balance statement
        self._consume(TokenType.KEYWORD)  # BALANCE
        self._consume(TokenType.KEYWORD)  # OF
        account_number = self._consume(TokenType.NAME).value
        node = ASTNode("Balance")
        node.add_child(ASTNode("AccountNumber", account_number))
        return node

    def _parse_exit(self):
        # parses through an exit statement
        self._consume(TokenType.KEYWORD)  # EXIT
        return ASTNode("Exit")

    def _consume(self, token_type):
        # if token matches the expected type, then conume the current token
        token = self.current_token()
        if token.token_type != token_type:
            raise ValueError(f"Expected token type {token_type}, but got {token.token_type}")
        self.current_token_index += 1
        return token

    def current_token(self):
        # returns current token
        return self.tokens[self.current_token_index]