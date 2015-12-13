"""
P := xi := xj +c
    | xi := xj - c
    | P; P
    | LOOP xi DO P END
"""
from collections import namedtuple

Variable = namedtuple('Variable', ['name'])
Constant = namedtuple('Constant', ['value'])
LoopSetup = namedtuple('LoopSetup', [])
LoopStart = namedtuple('LoopStart', [])
LoopEnd = namedtuple('LoopEnd', [])
AssignmentSymbol = namedtuple('AssignmentSymbol', [])
StatementEnd = namedtuple('StatementEnd', [])
Plus = namedtuple('Plus', [])
Minus = namedtuple('Minus', [])

Statement = namedtuple('Statement')
Assignment = namedtuple('Assignment')
Output = namedtuple('Output')
Loop = namedtuple('Loop')


class Tokenizer:
    TOKEN_END = '\n ;'
    stream = None

    def __init__(self, stream):
        self.stream = list(stream)

    def tokenize(self):
        while self.stream:
            token = None
            next_byte = self.next()
            print("Parsing next token, ", next_byte)
            if next_byte == 'x':
                number = None
                while self.peek() not in self.TOKEN_END:
                    number = number or 0
                    number = number * 10 + int(self.next())
                token = Variable(number)
            elif next_byte.isdigit():
                number = None
                while self.peek() not in self.TOKEN_END:
                    number = number or 0
                    number = number * 10 + int(self.next())
                token = Constant(number)
            elif next_byte == ':':
                assert self.next() == '='
                token = AssignmentSymbol()
            elif next_byte in [' ', '\n']:
                continue
            elif next_byte == ';':
                token = StatementEnd()
            elif next_byte == '+':
                token = Plus()
            elif next_byte == '-':
                token = Minus()
            elif next_byte == 'L':
                self.match('O')
                self.match('O')
                self.match('P')
                token = LoopSetup()
            elif next_byte == 'D':
                self.match('O')
                token = LoopStart()
            elif next_byte == 'E':
                self.match('N')
                self.match('D')
                token = LoopEnd()
            else:
                raise SyntaxError()
            yield token

    def peek(self):
        return self.stream[0]

    def next(self):
        return self.stream.pop(0)

    def match(self, byte):
        assert self.next() == byte


class Parser:
    tokens = None
    current = None

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        pass

    def match(self, token):
        pass
