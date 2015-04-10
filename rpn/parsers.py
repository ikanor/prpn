import operator

import parser


math = parser.Parser({
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '**': operator.pow,
    '%': operator.mod,
})
math.eval = lambda expression: parser.traverse(
    expression,
    math.operators,
    lambda operator, *args: math.operators[operator](*args),
    float)
