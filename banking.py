"""
Author: Lucas Becker and Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the main program for the Banking DSL.
Pledge: This is all our own work.
"""

from my_lexer import Lexer
from my_parser import Parser
from interpreter import Interpreter

def main():
    input_text = """
    CREATE ACCOUNT Dawn,Duerre,DD330330,100000000.00
    DEPOSIT 500000 TO DD330330
    WITHDRAW 200 FROM DD330330
    BALANCE OF DD330330
    EXIT
    """
    lexer = Lexer(input_text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter(ast)
    interpreter.interpret()

if __name__ == "__main__":
    main()
