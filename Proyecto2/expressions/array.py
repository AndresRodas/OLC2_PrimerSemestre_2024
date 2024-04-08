from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol

class Array(Instruction):
    def __init__(self, line, col, list_exp):
        self.line = line
        self.col = col
        self.list_exp = list_exp

    def ejecutar(self, ast, env, gen):
        return None