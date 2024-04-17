from interfaces.expression import Expression
from environment.value import Value
from environment.types import ExpressionType

class Access(Expression):
    def __init__(self, line, col, id):
        self.line = line
        self.col = col
        self.id = id

    def ejecutar(self, ast, env, gen):
        # Realizar busqueda en entorno
        sym = env.getVariable(ast, self.id)
        if(sym.type != ExpressionType.NULL):
            # Reconstrucción de Value
            return Value(sym.position, False, sym.type, [], [], [])
        return Value('', False, ExpressionType.NULL, [], [], [])

