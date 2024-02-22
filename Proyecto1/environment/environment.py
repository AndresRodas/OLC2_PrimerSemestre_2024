from environment.symbol import Symbol
from environment.types import ExpressionType

class Environment():
    def __init__(self, previous, id):
        self.previous = previous
        self.id = id
        self.tabla = {}
        self.interfaces = {}
        self.functions = {}

    def saveVariable(self, ast, id, symbol):
        if id in self.tabla:
            ast.setErrors(f"La variable {id} ya existe.")
            return
        self.tabla[id] = symbol

    def getVariable(self, ast, id):
        tmpEnv = self
        while True:
            if id in self.tabla:
                return self.tabla[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La variable {id} no existe.")
        return Symbol(0, 0, None, ExpressionType.NULL)
