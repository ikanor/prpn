"""
RPN Parser

Generates RPN parsers using a given set of operators.
"""

import string


def generate(operators, resolve, convert):

    def eval(expression):
        stack = []

        for token in string.split(expression):
            if token in operators:
                if len(stack) < 2:
                    raise ValueError(
                        "Invalid RPN expression: not enough operands "
                        "for operator %s" % token)
                right, left = stack.pop(), stack.pop()
                result = resolve(token, left, right)
            else:
                result = convert(token)
            stack.append(result)

        if len(stack) > 1:
            raise ValueError(
                "Invalid RPN expression: not enough operators %s" % stack)

        return stack.pop()

    return eval

