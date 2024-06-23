"""
Author: Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the Lexer class for the Banking DSL.
Pledge: This work is all my own with the help of Lucas.
"""

from my_token import Token, TokenType

###################################
#####      LEXER CLASS        #####
###################################

class Lexer:
    def __init__(self, input_text):
        # initializes lexer with input text
        self.input_text = input_text
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        # tokenizes the input into a list of the tokens
        while self.current_pos < len(self.input_text):
            if self.input_text[self.current_pos].isspace():
                self.current_pos += 1
            elif self.input_text[self.current_pos].isalpha():
                self.tokens.append(self._extract_word())
            elif self.input_text[self.current_pos].isdigit():
                self.tokens.append(self._extract_number())
            elif self.input_text[self.current_pos] == ',':
                self.tokens.append(Token(TokenType.COMMA, ','))
                self.current_pos += 1
            elif self.input_text[self.current_pos] == '.':
                self.tokens.append(Token(TokenType.DOT, '.'))
                self.current_pos += 1
            else:
                raise ValueError(f"Unknown character: {self.input_text[self.current_pos]}")
        self.tokens.append(Token(TokenType.EOF, ''))
        print("Tokens:", self.tokens)  # Print tokens
        return self.tokens

    def _extract_word(self):
        # extracts a word from the input text from the position of the tokenizer
        start_pos = self.current_pos
        while (self.current_pos < len(self.input_text) and 
               (self.input_text[self.current_pos].isalpha() or self.input_text[self.current_pos].isdigit())):
            self.current_pos += 1
        word = self.input_text[start_pos:self.current_pos]
        token_type = TokenType.KEYWORD if word.upper() in ["CREATE", "ACCOUNT", "DEPOSIT", "WITHDRAW", "BALANCE", "EXIT"] else TokenType.NAME
        return Token(token_type, word)

    def _extract_number(self):
        # extracts a number from the input text from the position of the tokenizer
        start_pos = self.current_pos
        while (self.current_pos < len(self.input_text) and 
               self.input_text[self.current_pos].isdigit()):
            self.current_pos += 1
        if self.current_pos < len(self.input_text) and self.input_text[self.current_pos] == '.':
            self.current_pos += 1
            while (self.current_pos < len(self.input_text) and 
                   self.input_text[self.current_pos].isdigit()):
                self.current_pos += 1
        return Token(TokenType.NUMBER, self.input_text[start_pos:self.current_pos])