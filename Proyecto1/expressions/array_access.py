from interfaces.expression import Expression
from environment.types import ExpressionType

class ArrayAccess(Expression):
    def __init__(self, line, col, array, index):
        self.line = line
        self.col = col
        self.array = array
        self.index = index

    def ejecutar(self, ast, env):
        # Traer el arreglo
        sym = self.array.ejecutar(ast, env)
        # Validar tipo principal
        if sym.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es un arreglo')
            return
        # Validar indice
        indexVal = self.index.ejecutar(ast, env)
        if indexVal.type != ExpressionType.INTEGER:
            ast.setErrors('El indice contiene un valor incorrecto')
            return
        # Retornar valor
        return sym.value[indexVal.value]


