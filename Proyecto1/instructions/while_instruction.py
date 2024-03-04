from interfaces.instruction import Instruction
from environment.environment import Environment

class While(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env):
        # Variables de iteración
        safe_cont = 0
        result = None
        # Ciclo
        while True:
            safe_cont += 1
            # Obtencion de la expresión
            result = self.exp.ejecutar(ast, env)
            # Validación
            if result.value:
                while_env = Environment(env, "WHILE")
                for s in self.block:
                    s.ejecutar(ast, while_env)
            else:
                break
            # Validar limite de seguridad
            if safe_cont >= 1000:
                ast.setErrors('Se ha excedido el máximo de ciclos permitidos')
                break


