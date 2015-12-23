from parsimonious.grammar import (
    Grammar,
    NodeVisitor,
)

grammar = Grammar(r"""
program = (assignment / plus_assignment / loop / output)*

NAME = ~r"x\d+"
NUMBER = ~r"(?:[1-9]\d*)|0"
MINUS = "-"
PLUS = "+"
ASSIGNMENT = ":="
SEMICOLON = ";"
WHITESPACE = ~r"\s*"
LOOP_SETUP = "LOOP"
LOOP_START = "DO"
LOOP_END = "END"

assignment = NAME WHITESPACE ASSIGNMENT WHITESPACE (expression/arithmetic)
plus_assignment = NAME WHITESPACE PLUS ASSIGNMENT WHITESPACE NAME WHITESPACE
    SEMICOLON WHITESPACE
expression = NUMBER WHITESPACE SEMICOLON WHITESPACE
arithmetic = (NAME WHITESPACE ( PLUS / MINUS ) WHITESPACE)?
    NUMBER WHITESPACE SEMICOLON WHITESPACE
output = NAME WHITESPACE SEMICOLON WHITESPACE
loop = LOOP_SETUP WHITESPACE NAME WHITESPACE LOOP_START WHITESPACE program
    WHITESPACE LOOP_END WHITESPACE
""")


class Visitor(NodeVisitor):
    stack = []

    def visit_NAME(self, node, visit):
        print("LOAD_NAME {}".format(node.match.group(0)))

    def visit_(self, node, visit):
        pass

    def visit_ASSIGNMENT(self, node, visit):
        pass

    def visit_WHITESPACE(self, node, visit):
        pass

    def visit_NUMBER(self, node, visit):
        print("LOAD_NUMBER {}".format(node.match.group(0)))

    def visit_SEMICOLON(self, node, visit):
        pass

    def visit_assignment(self, node, visit):
        print("STORE")

    def visit_plus_assignment(self, node, visit):
        print("LOAD_NAME {}".format(node.children[0].match.group(0)))
        print("ADD")
        print("STORE")

    def visit_PLUS(self, node, visit):
        self.stack.append("ADD")

    def visit_MINUS(self, node, visit):
        self.stack.append("MINUS")

    def visit_LOOP_SETUP(self, node, visit):
        pass

    def visit_LOOP_START(self, node, visit):
        print("LOOP_PUSH")

    def visit_program(self, node, visit):
        pass

    def visit_LOOP_END(self, node, visit):
        print("LOOP_CHECK")

    def visit_loop(self, node, visit):
        pass

    def visit_output(self, node, visit):
        print("PRINT")

    def visit_arithmetic(self, node, visit):
        print(self.stack.pop(0))

    def visit_expression(self, node, visit):
        pass
