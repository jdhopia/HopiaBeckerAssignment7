from ast_node import ASTNode

class Interpreter:
    def __init__(self, ast: ASTNode):
        self.ast = ast

    def interpret(self):
        for node in self.ast.children:
            self._execute_node(node)

    def _execute_node(self, node: ASTNode):
        print(f"Executing {node.token.value}")
