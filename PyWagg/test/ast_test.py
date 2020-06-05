import unittest
from PyWagg import tokens
from PyWagg import ast


class ASTTest(unittest.TestCase):

    def test_string(self):
        program = ast.Program([
            ast.LetStatement(
                tokens.Token(tokens.LET, "boop"),
                ast.Identifier(
                    tokens.Token(tokens.IDENT, "myVar"),
                    "myVar"
                ),
                ast.Identifier(
                    tokens.Token(tokens.IDENT, "anotherVar"),
                        "anotherVar"
                )
            )
        ])
        self.assertEqual(program.string(), "boop myVar = anotherVar;",
             msg="program.string() wrong. Got={}".format(program.string()))