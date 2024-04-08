from interfaces.instruction import Instruction
from environment.types import ExpressionType

class ArrayDeclaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        return None