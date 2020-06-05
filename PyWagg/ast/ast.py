from PyWagg.tokens import Token


class Node:
    def token_literal(self): pass
    def string(self): pass


class Statement(Node):
    node = None
    def statement_node(self): pass


class Expression(Node):
    node = None
    def expression_node(self): pass


class Program:
    statements = []

    def __init__(self, statements=None):
        if statements is None:
            statements = []
        self.statements = statements

    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""

    def string(self):
        out = ""
        for s in self.statements:
            out = out + s.string()
        return out


class Identifier(Expression):
    token = None
    value = ""

    def __init__(self, token, value):
        self.token = token
        self.value = value

    def token_literal(self):
        return self.token.Literal

    def string(self):
        return self.value


class LetStatement(Statement):
    token = None
    name = None
    value = None

    def __init__(self, token=None, name=None, value=None):
        self.token = token
        self.name = name
        self.value = value

    def token_literal(self):
        return self.token.Literal

    def string(self):
        out = self.token_literal() + " "
        out = out + self.name.string()
        out = out + " = "

        if self.value is not None:
            out = out + self.value.string()

        out = out + ";"
        return out


class ReturnStatement(Statement):
    token = None
    return_value = None

    def __init__(self, token=None, return_value=None):
        self.token = token
        self.return_value = return_value

    def token_literal(self):
        return self.token.Literal

    def string(self):
        out = self.token.Literal + " "

        if self.return_value is not None:
            out = out + self.return_value.string()

        out = out + ";"
        return out


class ExpressionStatement(Statement):
    token = None
    expression = None

    def __init__(self, token=None, expression=None):
        self.token = token
        self.expression = expression

    def token_literal(self):
        return self.token.Literal

    def string(self):
        if self.expression is not None:
            return self.expression.string()
        return ""
