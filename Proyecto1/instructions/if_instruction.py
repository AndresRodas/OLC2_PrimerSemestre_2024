from interfaces.instruction import Instruction
from environment.execute import BlockExecuter
from environment.environment import Environment
class If(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env):
        # Obtener simbolo
        validate = self.exp.ejecutar(ast, env)
        # Crear entorno del If
        if_env = Environment(env, "IF")
        # Evaluar
        if validate.value:
            return BlockExecuter(self.block, ast, if_env)
        return None
