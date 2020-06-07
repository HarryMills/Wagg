import unittest
from PyWagg import lexer
from PyWagg import ast
from PyWagg import parser


class ParserTest(unittest.TestCase):

    def test_let_statements(self):
        tests = [
            ("boop x = 5;", "x", 5),
            ("boop y = 10;", "y", 10),
            ("boop foobar = 838383;", "foobar", 838383),
        ]
        for t in tests:
            with self.subTest(test_case=t):
                l = lexer.new(t[0])
                p = parser.new(l)
                program = p.parse_program()
                self.check_parse_errors(p)
                stmt = program.statements[0]
                if not self.check_let_statement(stmt, t[1]):
                    return

    def test_return_statements(self):
        tests = [
            ("bork 5;", 5),
            ("bork 10;", 10),
            ("bork 993322;", 993322),
        ]
        for t in tests:
            with self.subTest(test_case=t):
                l = lexer.new(t[0])
                p = parser.new(l)
                program = p.parse_program()
                self.check_parse_errors(p)
                stmt = program.statements[0]
                if not self.check_return_statement(stmt, t[1]):
                    return

    def check_parse_errors(self, p):
        errors = p.errors
        if len(errors) == 0:
            return
        print('parser has {} errors'.format(len(errors)))
        for e in errors:
            print('parser error: {}'.format(e))
        self.fail()

    def check_let_statement(self, s, name):
        if s.token_literal() != 'boop':
            print("s.token_literal not 'boop'. got={}".format(s.token_literal()))
            return False
        if not isinstance(s, ast.LetStatement):
            print("s is not a ast.LetStatement. got={}".format(type(s)))
            return False
        if s.name.value != name:
            print("statement s value is not {}. got={}".format(name, s.name.value))
            return False
        if s.name.token_literal() != name:
            print("statement s token is not {}. got={}".format(name, s.name.token_literal()))
            return False
        return True

    def check_return_statement(self, s, name):
        if s.token_literal() != 'bork':
            print("s.token_literal not 'bork'. got={}".format(s.token_literal()))
            return False
        if not isinstance(s, ast.ReturnStatement):
            print("s is not a ast.ReturntStatement. got={}".format(type(s)))
            return False
