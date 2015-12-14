"""
P := xi := xj +c
    | xi := xj - c
    | P; P
    | LOOP xi DO P END
"""
from sys import stdin

from tdparser import (
    Token,
    Lexer,
)


class Variable(Token):
    regexp = r'x\d+'


class Constant(Token):
    regexp = r'\d+'


class Plus(Token):
    regexp = '\+'


class Assignment(Token):
    regexp = r':='


class StatementEnd(Token):
    regexp = r';'


class NewLine(Token):
    regexp = r'\n'


lexer = Lexer()
lexer.blank_chars = ' \n'
lexer.register_token(Assignment)
lexer.register_token(Constant)
lexer.register_token(Plus)
lexer.register_token(StatementEnd)
lexer.register_token(Variable)
lexer.register_token(NewLine)

if __name__ == "__main__":
    inp = stdin.read()
    print(inp)
