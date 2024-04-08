from interfaces.instruction import Instruction

class Interface(Instruction):
    def __init__(self, line, col, id, attr):
        self.line = line
        self.col = col
        self.id = id
        self.attr = attr

    def ejecutar(self, ast, env, gen):
        return None