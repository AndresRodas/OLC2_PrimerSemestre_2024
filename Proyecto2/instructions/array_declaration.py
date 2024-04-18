from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol

class ArrayDeclaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        temp = gen.new_temp()
        arrValue = self.exp.ejecutar(ast, env, gen)
        # Validar tipo
        if arrValue.type != ExpressionType.ARRAY:
            ast.setErrors("La expresion no es un arreglo")
            return None
        nameId = 'arr_'+str(temp)
        gen.variable_data(nameId, 'word', ', '.join(arrValue.value) )
        # Generar simbolo
        sym = Symbol(self.line, self.col, self.id, self.type, nameId)
        # Agregar al entorno
        env.saveVariable(ast, self.id, sym)
        return None