#!/usr/bin/env python
from sys import stdin

from loop_lang import (
    grammar,
    Visitor,
)


if __name__ == "__main__":
    inp = stdin.read().strip()
    ast = grammar.parse(inp)
    visitor = Visitor()
    visitor.visit(ast)
