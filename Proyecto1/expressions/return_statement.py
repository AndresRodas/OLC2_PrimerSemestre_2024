from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType

class Return(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env):
        if env.FunctionValidation():
            if self.exp == None:
                return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.RETURN)
            sym = self.exp.ejecutar(ast, env)
            return Symbol(line=self.line, col=self.col, value=sym, type=ExpressionType.RETURN)
        ast.setErrors('La sentencia de transferencia no se encuentra dentro de una función')
        return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)