from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.execute import StatementExecuter
from environment.types import ExpressionType
from expressions.continue_statement import Continue
class While(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env, gen):
        return None