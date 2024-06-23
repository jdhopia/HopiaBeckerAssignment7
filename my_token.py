"""
Author: Lucas Becker
Date: 06/23/2024
Class: 330
Description: This file contains the Token and TokenType classes for the Banking DSL.
Pledge: This work is all my own with the help of Jayce.
"""

from enum import Enum, auto

class TokenType(Enum):
    KEYWORD = auto()
    NAME = auto()
    NUMBER = auto()
    COMMA = auto()
    DOT = auto()
    EOF = auto()

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"

