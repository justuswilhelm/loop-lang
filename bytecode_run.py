#!/usr/bin/env python
from collections import namedtuple
from sys import stdin

Name = namedtuple('Name', ['value'])
Number = namedtuple('Number', ['value'])
JumpAddress = namedtuple('JumpAddress', ['value'])


def read_code(inp):
    for line in inp.readlines():
        instr, *val = line.strip().split(' ')
        yield instr, val


def pop_obj(stack, cls):
    obj = stack.pop()
    try:
        assert isinstance(obj, cls), (
            "{} is not instance of {}".format(obj, cls))
    except AssertionError as e:
        stack.append(obj)
        raise e
    return obj.value


def run_code(code):
    values = {}
    stack = []
    position = -1

    while True:
        position += 1
        if position >= len(code):
            break
        instr, val = code[position]
        if instr == 'PRINT':
            name = pop_obj(stack, Name)
            print(values[name])
        elif instr == 'LOAD_NUMBER':
            stack.append(Number(int(val[0])))
        elif instr == 'LOAD_NAME':
            stack.append(Name(val[0]))
        elif instr == 'STORE':
            number = pop_obj(stack, Number)
            name = pop_obj(stack, Name)
            values[name] = number
        elif instr == 'ADD':
            try:
                number = pop_obj(stack, Number)
            except AssertionError:
                name2 = pop_obj(stack, Name)
                number = values[name2]
            name = pop_obj(stack, Name)
            stack.append(Number(values[name] + number))
        elif instr == 'END':
            break
        elif instr == 'LOOP_PUSH':
            name = pop_obj(stack, Name)
            stack.append(JumpAddress((values[name] - 1, position)))
            if values[name] <= 0:
                while instr != "LOOP_CHECK":
                    position += 1
                    instr, _ = code[position]
        elif instr == 'LOOP_CHECK':
            value, jump_position = pop_obj(stack, JumpAddress)
            if value > 0:
                stack.append(JumpAddress((value - 1, jump_position)))
                position = jump_position
        else:
            raise Exception('Unknown Instruction {}'.format(instr, val))


if __name__ == "__main__":
    code = list(read_code(stdin))
    run_code(code)
