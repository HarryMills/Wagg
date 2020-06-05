from PyWagg import ast
from PyWagg import lexer
from PyWagg import tokens


class Parser:
    l = None
    errors = []
    curToken = None
    peekToken = None

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
        if self.curToken.Type == tokens.RETURN:
            return self.parse_return_statement()
        return None

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


def new(lexer):
    p = Parser(lexer)

    p.next_token()
    p.next_token()

    return p
