from typing import NamedTuple


class Token(NamedTuple):
    Type: str
    Literal: str

# --- Contants for the tokens ---

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers
IDENT = "IDENT" # add, foobar, x, y
INT = "INT" # 1234567890

# Operators
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"

LT = "<"
GT = ">"

EQ = "=="
NOT_EQ = "!="

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"

keywords = {
    "floof": FUNCTION,
    "boop": LET,
    "good": TRUE,
    "bad": FALSE,
    "mlem": IF,
    "blep": ELSE,
    "bork": RETURN,
}


def lookup_ident(ident):
    return keywords[ident] if ident in keywords else IDENT