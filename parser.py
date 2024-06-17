class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def statement(self):
        # Implement according to your language's grammar
        pass

    def program(self):
        nodes = self.statement_list()
        if self.current_token.type != 'EOF':
            self.error()
        return nodes

    def parse(self):
        return self.program()
