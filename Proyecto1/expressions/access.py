from interfaces.expression import Expression

class Access(Expression):
    def __init__(self, line, col, id):
        self.line = line
        self.col = col
        self.id = id

    def ejecutar(self, ast, env):
        # Realizar busqueda en entorno
        sym = env.getVariable(ast, self.id)
        return sym


