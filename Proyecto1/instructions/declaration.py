from interfaces.instruction import Instruction
from environment.types import ExpressionType

class Declaration(Instruction):
    def __init__(self, line, col, id, exp):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env):
        # Obtener simbolo
        result = self.exp.ejecutar(ast, env)
        # Agregar al entorno
        if result.type != ExpressionType.STRUCT:
            env.saveVariable(ast, self.id, result)
        

