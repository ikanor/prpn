import unittest

import rpn.parsers


class TestCase(unittest.TestCase):
    def test_parsers(self):
        result = rpn.parsers.math.eval("5 3 *")
        self.assertEquals(15.0, result)

        result = rpn.parsers.math.parse("5 3 *")
        self.assertEquals({'*': ('5', '3')}, result)

        result = rpn.parsers.math.export("5 3 *")
        self.assertEquals("(5 * 3)", result)
