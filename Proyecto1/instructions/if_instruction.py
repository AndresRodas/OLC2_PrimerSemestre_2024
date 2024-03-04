from interfaces.instruction import Instruction

class If(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env):
        # Obtener simbolo
        validate = self.exp.ejecutar(ast, env)
        # Evaluar
        if validate.value:
            for inst in self.block:
                inst.ejecutar(ast, env)