from interfaces.instruction import Instruction

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env):
        outText = ""
        for exp in self.Exp:
            sym = exp.ejecutar(ast, env)
            print(exp)
            outText += " " + str(sym.value)
        print(outText)
