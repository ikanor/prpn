import string
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '**': operator.pow,
    '%': operator.mod,
}

def eval(expression):
    stack = []

    for token in string.split(expression):
        if token in operators:
            if len(stack) < 2:
                raise ValueError(
                    "Invalid RPN expression: not enough operands "
                    "for operator %s" % token)
            right, left = stack.pop(), stack.pop()
            result = operators[token](left, right)
        else:
            result = float(token)
        stack.append(result)

    if len(stack) > 1:
        raise ValueError(
            "Invalid RPN expression: not enough operators %s" % stack)

    return stack.pop()
