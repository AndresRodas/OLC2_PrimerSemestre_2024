from interfaces.instruction import Instruction
from environment.symbol import Symbol

class Assignment(Instruction):
    def __init__(self, line, col, id, exp):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        # Obtener valor
        result = self.exp.ejecutar(ast, env, gen)
        sym = Symbol(self.line, self.col, self.id, result.type, result.value)
        # Editar simbolo
        env.setVariable(ast, self.id, sym)
        return None