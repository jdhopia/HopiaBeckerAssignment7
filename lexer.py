import re
from token import Token, TokenType

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
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
        return self.tokens

    def _extract_word(self):
        start_pos = self.current_pos
        while (self.current_pos < len(self.input_text) and 
               self.input_text[self.current_pos].isalpha()):
            self.current_pos += 1
        word = self.input_text[start_pos:self.current_pos]
        token_type = TokenType.KEYWORD if word.upper() in ["CREATE", "ACCOUNT", "DEPOSIT", "WITHDRAW", "BALANCE", "EXIT"] else TokenType.NAME
        return Token(token_type, word)

    def _extract_number(self):
        start_pos = self.current_pos
        while (self.current_pos < len(self.input_text) and 
               self.input_text[self.current_pos].isdigit()):
            self.current_pos += 1
        return Token(TokenType.NUMBER, self.input_text[start_pos:self.current_pos])
