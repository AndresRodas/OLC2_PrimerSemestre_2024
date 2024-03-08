from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.execute import StatementExecuter
from environment.types import ExpressionType
from expressions.continue_statement import Continue
class While(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env):
        # Variables de iteración
        safe_cont = 0
        Flag = None
        result = None
        # Ciclo
        while True:
            safe_cont += 1
            # Obtencion de la expresión
            result = self.exp.ejecutar(ast, env)
            # Validación
            if result.value:
                while_env = Environment(env, "WHILE")
                Flag = StatementExecuter(self.block, ast, while_env)
                # Validar si es sentencia de transferencia
                if Flag != None:
                    if Flag.type == ExpressionType.BREAK:
                        break
                    if Flag.type == ExpressionType.CONTINUE:
                        continue
                    if Flag.type == ExpressionType.RETURN:
                        return Flag
            else:
                break
            # Validar limite de seguridad
            if safe_cont >= 1000:
                ast.setErrors('Se ha excedido el máximo de ciclos permitidos')
                break
        return None

