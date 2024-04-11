from interfaces.instruction import Instruction
from environment.types import ExpressionType

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env, gen):
        for exp in self.Exp:
            val = exp.ejecutar(ast, env, gen)
            # Imprimiendo expresion
            gen.add_br()
            gen.add_li('t3', str(val.value))
            gen.add_lw('a0', '0(t3)')
            gen.add_li('a7', '1')
            gen.add_system_call()
            # Imprimiendo salto de linea
            gen.add_br()
            gen.add_li('a0', '10')
            gen.add_li('a7', '11')
            gen.add_system_call()

        return None