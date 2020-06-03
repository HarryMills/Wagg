from PyWagg.token import token


class Lexer:
    input = ""
    position = 0
    readPosition = 0
    ch = ''

    def __init__(self, input, position=0, read_position=0, ch=''):
        self.input = input
        self.position = position
        self.read_position = read_position
        self.ch = ch

    def next_token(self):
        tok = None
        self.skip_whitespace()

        if self.ch == '=':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = new_token(token.EQ, literal)
            else:
                tok = new_token(token.ASSIGN, self.ch)
        elif self.ch == ';':
            tok = new_token(token.SEMICOLON, self.ch)
        elif self.ch == '(':
            tok = new_token(token.LPAREN, self.ch)
        elif self.ch == ')':
            tok = new_token(token.RPAREN, self.ch)
        elif self.ch == ',':
            tok = new_token(token.COMMA, self.ch)
        elif self.ch == '+':
            tok = new_token(token.PLUS, self.ch)
        elif self.ch == '-':
            tok = new_token(token.MINUS, self.ch)
        elif self.ch == '!':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = new_token(token.NOT_EQ, literal)
            else:
                tok = new_token(token.BANG, self.ch)
        elif self.ch == '/':
            tok = new_token(token.SLASH, self.ch)
        elif self.ch == '*':
            tok = new_token(token.ASTERISK, self.ch)
        elif self.ch == '<':
            tok = new_token(token.LT, self.ch)
        elif self.ch == '>':
            tok = new_token(token.GT, self.ch)
        elif self.ch == '{':
            tok = new_token(token.LBRACE, self.ch)
        elif self.ch == '}':
            tok = new_token(token.RBRACE, self.ch)
        elif self.ch == 0:
            tok = new_token(token.EOF, "")
        else:
            if is_letter(self.ch):
                literal = self.read_identifier()
                type = token.lookup_ident(literal)
                return new_token(type, literal)
            elif is_digit(self.ch):
                return new_token(token.INT, self.read_number())
            else:
                tok = new_token(token.ILLEGAL, self.ch)

        self.read_char()
        return tok

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position = self.read_position + 1

    def read_identifier(self):
        position = self.position
        while self.ch != 0 and is_letter(self.ch):
            self.read_char()
        return self.input[position:self.position]

    def read_number(self):
        position = self.position
        while self.position != 0 and is_digit(self.position):
            self.read_char()
        return self.input[position:self.position]

    def skip_whitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()

    def peek_char(self):
        if self.read_position >= len(self.input):
            return 0
        else:
            return self.input[self.read_position]


def is_letter(ch):
    return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'


def is_digit(ch):
    return '0' <= ch <= '9'


def new_token(token_type, ch):
    return token.Token(token_type, ch)


def new(source):
    lex = Lexer(source)
    lex.read_char()
    return lex
