from interfaces.expression import Expression

class Ternario(Expression):
    def __init__(self, line, col, exp1, exp2, exp3):
        self.line = line
        self.col = col
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

    def ejecutar(self, ast, env, gen):
        return None
