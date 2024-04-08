from interfaces.expression import Expression

class InterfaceAccess(Expression):
    def __init__(self, line, col, exp, id):
        self.line = line
        self.col = col
        self.exp = exp
        self.id = id

    def ejecutar(self, ast, env, gen):
        return None

