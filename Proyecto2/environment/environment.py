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
            if id in tmpEnv.tabla:
                return tmpEnv.tabla[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La variable {id} no existe.")
        return Symbol(0, 0, '', ExpressionType.NULL, '')

    def setVariable(self, ast, id, symbol):
        tmpEnv = self
        while True:
            if id in tmpEnv.tabla:
                tmpEnv.tabla[id] = symbol
                return symbol
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La variable {id} no existe.")
        return Symbol(0, 0, None, ExpressionType.NULL)

    def saveFunction(self, ast, id, function):
        if id in self.functions:
            ast.setErrors(f"Ya existe una función con el nombre {id}")
            return
        self.functions[id] = function

    def getFunction(self, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.functions:
                return tmpEnv.functions[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La función {id} no existe.")
        return {}

    def saveStruct(self, ast, id, struct):
        if id in self.interfaces:
            ast.setErrors(f"Ya existe una interface con el nombre {id}")
            return
        self.interfaces[id] = struct
    
    def getStruct(self, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.interfaces:
                return tmpEnv.interfaces[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La interfaz {id} no existe.")
        return None

    def LoopValidation(self):
        tmpEnv = self
        while True:
            if tmpEnv.id == 'WHILE' or tmpEnv.id == 'FOR':
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def FunctionValidation(self):
        tmpEnv = self
        while True:
            if 'FUNCTION_' in tmpEnv.id:
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def getGlobalEnvironment(self):
        tmpEnv = self
        while True:
            if tmpEnv.previous == None:
                return tmpEnv
            else:
                tmpEnv = tmpEnv.previous
