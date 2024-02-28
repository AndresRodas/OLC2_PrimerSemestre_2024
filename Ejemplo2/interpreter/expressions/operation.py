from ..interfaces.expression import Expression

class Operation(Expression):
    def __init__(self, line, col, operador, opLeft, opRight):
        self.line = line
        self.col = col
        self.operador = operador
        self.opLeft = opLeft
        self.opRight = opRight

    def ejecutar(self, ast, env):
        if(self.operador == "+"):
            return self.opLeft + self.opRight
        if(self.operador == "-"):
            return self.opLeft - self.opRight
        if(self.operador == "*"):
            return self.opLeft * self.opRight

