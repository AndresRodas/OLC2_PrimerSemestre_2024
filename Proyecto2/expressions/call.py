from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.environment import Environment
from environment.execute import StatementExecuter
from expressions.continue_statement import Continue

class Call(Expression):
    def __init__(self, line, col, id, params):
        self.line = line
        self.col = col
        self.id = id
        self.params = params

    def ejecutar(self, ast, env, gen):
        return None
