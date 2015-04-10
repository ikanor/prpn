"""
RPN Parser

Provides the parser interface, with helpers to traverse RPN expressions and
create RPN parsers.
"""

import string


def traverse(expression, operators, solve, convert):
    """
    Analyses an RPN string using a stack. Creates the tree as the expression is
    traversed.

    Args:
        expression: A string representing an RPN expression.
        operators: The set of operators. Can be any structure that implements
            the `in` operator to test membership.
        solve: The solver function. This function will receive three
            paramenters: `operator`, `left_operand` and `right_operand`. The
            operand will not be converted, but sent as found in the expression
            string. Must return the result of the operation, which will be
            pushed to the stack.
        convert: The converter function. It will receive any non-operand tokens
            found in the expression string for them to be converted before being
            pushed to the stack.

    Returns:
        The last result returned by the `solve` function.

    Throws:
        ValueError: if not enough operands were found in the expression string.
        ValueError: if not enough operators were found in the expression string.
    """
    stack = []

    for token in string.split(expression):
        if token in operators:
            if len(stack) < 2:
                raise ValueError(
                    "Invalid RPN expression: not enough operands "
                    "for operator %s" % token)
            right, left = stack.pop(), stack.pop()
            result = solve(token, left, right)
        else:
            result = convert(token)
        stack.append(result)

    if len(stack) > 1:
        raise ValueError(
            "Invalid RPN expression: not enough operators %s" % stack)

    return stack.pop()


def generate(operators, solve, convert):
    """
    Generates a simple parser function with an associated inmutable set of
    operators.

    See the documentation of `traverse` for a description of the args.

    Returns:
        A `traverse` function where the parameters `operators`, `solve` and
        `convert` are fixed.
    """
    def parser(expression):
        return traverse(expression, operators, solve, convert)
    return parser
