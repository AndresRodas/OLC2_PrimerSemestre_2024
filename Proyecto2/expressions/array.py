from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.value import Value

class Array(Instruction):
    def __init__(self, line, col, list_exp):
        self.line = line
        self.col = col
        self.list_exp = list_exp

    def ejecutar(self, ast, env, gen):
        newArr = []
        for var in self.list_exp:
            value = var.ejecutar(ast, env, gen)
            newArr.append(value.value)
        return  Value(newArr, False, ExpressionType.ARRAY, [], [], [])