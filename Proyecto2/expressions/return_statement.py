from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType

class Return(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        return None