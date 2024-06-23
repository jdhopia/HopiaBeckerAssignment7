"""
Author: Jayce Hopia
Date: 06/23/2024
Class: 330
Description: This file contains the ASTNode class for the Banking DSL.
Pledge: This work is all my own with the help of Lucas.
"""

class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"ASTNode({self.node_type}, {self.value}, {self.children})"
