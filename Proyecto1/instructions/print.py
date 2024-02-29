from interfaces.instruction import Instruction
from environment.types import ExpressionType

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env):
        outText = ""
        for exp in self.Exp:
            sym = exp.ejecutar(ast, env)
            if sym.type == ExpressionType.ARRAY:
                outText += "["
                for arr in sym.value:
                    outText += " " + str(arr.value) + ", "
                outText += "]"
            else:
                outText += " " + str(sym.value)
        ast.setConsole(outText)

    def PrintMatrix(self, array, outvalue):
        for arr in array:
            if arr == ExpressionType.ARRAY:
                return self.PrintMatrix(arr, outvalue)
            else:
                outvalue += str(arr)
        return outvalue