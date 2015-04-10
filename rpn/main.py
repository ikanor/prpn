import string
import operator

import parser

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '**': operator.pow,
    '%': operator.mod,
}

eval = parser.generate(
    operators,
    lambda operator, *args: operators[operator](*args),
    float)

parse = parser.generate(
    operators,
    lambda operator, *args: {operator: args},
    lambda operand: operand)

export = parser.generate(
    operators,
    lambda operator, *args: "(%s %s %s)" % (args[0], operator, args[1]),
    lambda operand: operand)
