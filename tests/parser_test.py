import unittest

import rpn.parser


class TestCase(unittest.TestCase):
    def test_Parser(self):
        parser = rpn.parser.Parser(["*"])

        result = parser.parse("5 3 *")
        self.assertIs(type(result), dict)

        result = parser.export("5 3 *")
        self.assertIs(type(result), str)

        failed = False
        try:
            parser.eval("5 3 *")
        except NotImplementedError:
            failed = True
        self.assertTrue(failed, "eval method should not be implemented")
