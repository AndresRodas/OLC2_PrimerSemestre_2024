from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType

class Continue(Expression):
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def ejecutar(self, ast, env, gen):
        return None
