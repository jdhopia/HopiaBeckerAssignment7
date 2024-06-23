"""
Author: Lucas Becker
Date: 06/23/2024
Class: 330
Description: This file contains the Token and TokenType classes for the Banking DSL.
Pledge: This work is all my own with the help of Jayce.
"""

from enum import Enum, auto

###################################
#####     TOKEN TYPE ENUM     #####
###################################

class TokenType(Enum):
    KEYWORD = auto()
    NAME = auto()
    NUMBER = auto()
    COMMA = auto()
    DOT = auto()
    EOF = auto()

###################################
#####      TOKEN CLASS        #####
###################################

class Token:
    def __init__(self, token_type, value):
        # Initializes a new token with the given type and value.
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        # Returns a string representation of the token.
        return f"Token({self.token_type}, {self.value})"