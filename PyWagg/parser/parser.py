from enum import Enum, auto

from PyWagg import ast
from PyWagg import lexer
from PyWagg import tokens


class Precedence(Enum):
    LOWEST = auto()
    EQUALS = auto()  # ==
    LESSGREATER = auto()  # > or <
    SUM = auto()  # +
    PRODUCT = auto()  # *
    PREFIX = auto()  # -X or !X
    CALL = auto()  # myFunction(x)


class Parser:
    l = None
    errors = []
    curToken = None
    peekToken = None
    prefix_parse_fns = {}
    infix_parse_fns = {}

    def __init__(self, l, errors=None):
        self.l = l
        if errors is None:
            errors = []
        self.errors = errors

    def next_token(self):
        self.curToken = self.peekToken
        self.peekToken = self.l.next_token()

    def parse_program(self):
        program = ast.Program()
        while self.curToken.Type != tokens.EOF:
            stmt = self.parse_statement()
            if stmt is not None:
                program.statements.append(stmt)
            self.next_token()
        return program

    def parse_statement(self):
        if self.curToken.Type == tokens.LET:
            return self.parse_let_statement()
        elif self.curToken.Type == tokens.RETURN:
            return self.parse_return_statement()
        else:
            return self.parse_expression_statement()

    def parse_let_statement(self):
        stmt = ast.LetStatement(self.curToken)
        if not self.expect_peek(tokens.IDENT):
            return None
        stmt.name = ast.Identifier(self.curToken, self.curToken.Literal)
        if not self.expect_peek(tokens.ASSIGN):
            return None
        # TODO: Skipping expressions until we encounter a semicolon

        while not self.cur_token_is(tokens.SEMICOLON):
            self.next_token()

        return stmt

    def parse_return_statement(self):
        stmt = ast.ReturnStatement(self.curToken)
        self.next_token()

        # TODO: Skipping the expression until we encounter a semicolon
        while not self.cur_token_is(tokens.SEMICOLON):
            self.next_token()

        return stmt

    def cur_token_is(self, t):
        return self.curToken.Type == t

    def peek_token_is(self, t):
        return self.peekToken.Type == t

    def expect_peek(self, t):
        if self.peek_token_is(t):
            self.next_token()
            return True
        else:
            self.peek_error(t)
            return False

    def peek_error(self, t):
        msg = "expected next token to be " + t + ", got " + self.peekToken.Type + " instead"
        self.errors.append(msg)

    def register_prefix(self, token_type, fn):
        self.prefix_parse_fns[token_type] = fn

    def register_infix(self, token_type, fn):
        self.infix_parse_fns[token_type] = fn

    def parse_expression_statement(self):
        stmt = ast.ExpressionStatement(self.curToken)
        stmt.expression = self.parse_expression(Precedence.LOWEST)

        if self.peek_token_is(tokens.SEMICOLON):
            self.next_token()

        return stmt

    def parse_expression(self, precedence):
        prefix = self.prefix_parse_fns[self.curToken.Type]
        if prefix is None:
            return None

        left_exp = prefix()
        return left_exp

    def parse_identifier(self):
        return ast.Identifier(self.curToken, self.curToken.Literal)

    def parse_integer_literal(self):
        lit = ast.IntegerLiteral(self.curToken)
        try:
            value = int(self.curToken.Literal)
            lit.value = value
            return lit
        except ValueError:
            msg = 'could not parse {} as integer'.format(self.curToken)
            self.errors.append(msg)
            return None

def new(lexer):
    p = Parser(lexer)

    p.prefix_parse_fns = {}
    p.register_prefix(tokens.IDENT, p.parse_identifier)
    p.register_prefix(tokens.INT, p.parse_integer_literal)

    p.next_token()
    p.next_token()

    return p
