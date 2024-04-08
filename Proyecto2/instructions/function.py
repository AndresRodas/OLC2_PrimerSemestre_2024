from interfaces.instruction import Instruction

class Function(Instruction):
    def __init__(self, line, col, id, params, type, block):
        self.line = line
        self.col = col
        self.id = id
        self.params = params
        self.type = type
        self.block = block

    def ejecutar(self, ast, env, gen):
        return None