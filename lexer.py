import re
from token import Token

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []

    def tokenize(self):
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('ID',       r'[A-Za-z][A-Za-z0-9]*'),
            ('WS',       r'\s+'),
        ]
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        get_token = re.compile(tok_regex).match

        mo = get_token(self.input_text)
        while mo is not None:
            typ = mo.lastgroup
            if typ != 'WS':
                val = mo.group(typ)
                self.tokens.append(Token(typ, val))
            self.position = mo.end()
            mo = get_token(self.input_text[self.position:])
        return self.tokens
