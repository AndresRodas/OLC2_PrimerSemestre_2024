from interfaces.instruction import Instruction

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env):
        print('entra a print')
        outText = ""
        for exp in self.Exp:
            print(exp)
            sym = exp.ejecutar(ast, env)
            outText += " " + str(sym.value)
        ast.setConsole(outText)