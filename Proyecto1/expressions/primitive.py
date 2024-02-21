from interfaces.expression import Expression
from environment.symbol import Symbol

class Primitive(Expression):
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.type = type

    def ejecutar(self, ast, env):
        return Symbol(line=self.line, col=self.col, value=self.value, type=self.type)


