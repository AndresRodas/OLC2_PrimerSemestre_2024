from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType

class Break(Expression):
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def ejecutar(self, ast, env):
        if env.LoopValidation():
            return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.BREAK)
        ast.setErrors('La sentencia de transferencia no se encuentra dentro de un ciclo')
        return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)
