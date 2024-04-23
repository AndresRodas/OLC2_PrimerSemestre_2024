from interfaces.instruction import Instruction

class Assignment(Instruction):
    def __init__(self, line, col, id, exp):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        gen.comment('Asignacion de variable')
        # Obtener valor
        result = self.exp.ejecutar(ast, env, gen)
        # Obteniendo la posicion
        sym = env.getVariable(ast, self.id)
        # Sustituyendo valor
        if 't' in str(result.value):
            gen.add_move('t0', str(result.value))
        else:
            gen.add_li('t0', str(result.value))
        gen.add_lw('t1', '0(t0)')
        gen.add_li('t3', str(sym.position))
        gen.add_sw('t1', '0(t3)')
        gen.comment('Fin asignacion')
        return None