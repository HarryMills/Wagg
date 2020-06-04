from PyWagg.tokens import tokens


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
                tok = new_token(tokens.EQ, literal)
            else:
                tok = new_token(tokens.ASSIGN, self.ch)
        elif self.ch == ';':
            tok = new_token(tokens.SEMICOLON, self.ch)
        elif self.ch == '(':
            tok = new_token(tokens.LPAREN, self.ch)
        elif self.ch == ')':
            tok = new_token(tokens.RPAREN, self.ch)
        elif self.ch == ',':
            tok = new_token(tokens.COMMA, self.ch)
        elif self.ch == '+':
            tok = new_token(tokens.PLUS, self.ch)
        elif self.ch == '-':
            tok = new_token(tokens.MINUS, self.ch)
        elif self.ch == '!':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = new_token(tokens.NOT_EQ, literal)
            else:
                tok = new_token(tokens.BANG, self.ch)
        elif self.ch == '/':
            tok = new_token(tokens.SLASH, self.ch)
        elif self.ch == '*':
            tok = new_token(tokens.ASTERISK, self.ch)
        elif self.ch == '<':
            tok = new_token(tokens.LT, self.ch)
        elif self.ch == '>':
            tok = new_token(tokens.GT, self.ch)
        elif self.ch == '{':
            tok = new_token(tokens.LBRACE, self.ch)
        elif self.ch == '}':
            tok = new_token(tokens.RBRACE, self.ch)
        elif self.ch == 0:
            tok = new_token(tokens.EOF, "")
        else:
            if is_letter(self.ch):
                literal = self.read_identifier()
                type = tokens.lookup_ident(literal)
                return new_token(type, literal)
            elif is_digit(self.ch):
                return new_token(tokens.INT, self.read_number())
            else:
                tok = new_token(tokens.ILLEGAL, self.ch)

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
        while self.position != 0 and is_digit(self.ch):
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
    return '0' <= ch and ch <= '9'


def new_token(token_type, ch):
    return tokens.Token(token_type, ch)


def new(source):
    lex = Lexer(source)
    lex.read_char()
    return lex
