from parsimonious.grammar import (
    Grammar,
    NodeVisitor,
)

grammar = Grammar(r"""
program = (assignment / loop / output)*

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

assignment = NAME WHITESPACE ASSIGNMENT WHITESPACE
    (NAME WHITESPACE ( PLUS / MINUS ) WHITESPACE)?
    NUMBER WHITESPACE SEMICOLON WHITESPACE
output = NAME WHITESPACE SEMICOLON WHITESPACE
loop = LOOP_SETUP WHITESPACE NAME WHITESPACE LOOP_START WHITESPACE program
    WHITESPACE LOOP_END WHITESPACE
""")


class Visitor(NodeVisitor):
    def visit_NAME(self, node, visit):
        ...

    def visit_(self, node, visit):
        pass

    def visit_ASSIGNMENT(self, node, visit):
        ...

    def visit_WHITESPACE(self, node, visit):
        pass

    def visit_NUMBER(self, node, visit):
        ...

    def visit_SEMICOLON(self, node, visit):
        pass

    def visit_assignment(self, node, visit):
        ...

    def visit_PLUS(self, node, visit):
        ...

    def visit_MINUS(self, node, visit):
        ...

    def visit_LOOP_SETUP(self, node, visit):
        ...

    def visit_LOOP_START(self, node, visit):
        ...

    def visit_program(self, node, visit):
        ...

    def visit_LOOP_END(self, node, visit):
        ...

    def visit_loop(self, node, visit):
        ...

    def visit_output(self, node, visit):
        ...
