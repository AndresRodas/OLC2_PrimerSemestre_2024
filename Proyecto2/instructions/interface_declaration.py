from interfaces.instruction import Instruction
from environment.environment import Environment

class InterfaceDeclaration(Instruction):
    def __init__(self, line, col, id1, id2, content):
        self.line = line
        self.col = col
        self.id1 = id1
        self.id2 = id2
        self.content = content

    def ejecutar(self, ast, env, gen):
        return None