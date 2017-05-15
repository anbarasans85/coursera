# python3

import sys


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def isbalanced(input_string):
    bracket_stack = Stack()
    count = 0
    for character in input_string:
        count += 1
        if character in ['(', '[', '{']:
            bracket_stack.push((character, count))
        else:
            if character not in [')', ']', '}']:
                continue
            if bracket_stack.isEmpty():
                return False, (character, count)
            top = bracket_stack.pop()
            if (top[0] == '[' and character != ']') or \
                    (top[0] == '(' and character != ')') or \
                    (top[0] == '{' and character != '}'):
                return False, (top[0], count)
    if bracket_stack.isEmpty():
        return True, 0
    else:
        return False, bracket_stack.peek()


if __name__ == "__main__":
    test_string = sys.stdin.read()
    result = isbalanced(test_string)
    if not result[0]:
        print(result[1][1])
    else:
        print('Success')
