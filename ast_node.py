from token import Token

class ASTNode:
    def __init__(self, token: Token):
        self.token = token
        self.children = []

    def add_child(self, node):
        self.children.append(node)
