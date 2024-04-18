from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.value import Value

class ArrayAccess(Expression):
    def __init__(self, line, col, array, index):
        self.line = line
        self.col = col
        self.array = array
        self.index = index

    def ejecutar(self, ast, env, gen):
        # Traer el arreglo
        sym = env.getVariable(ast, self.array)
        if(sym.type == ExpressionType.NULL):
            ast.setErrors(f"El arreglo {self.array} no ha sido encontrado")
            return None
        # Validar tipo principal
        indexVal = self.index.ejecutar(ast, env, gen)
        if indexVal.type != ExpressionType.INTEGER:
            ast.setErrors('El indice contiene un valor incorrecto')
            return None
        # Agregar llamada
        gen.add_br()
        gen.comment('Acceso a un arreglo')
        if 't' in str(indexVal.value):
            gen.add_move('t3', str(indexVal.value))
        else:
            gen.add_li('t3', str(indexVal.value))
        gen.add_lw('t1', '0(t3)')
        gen.add_move('t0', 't1')
        gen.add_slli('t0', 't0', '2')
        gen.add_la('t1', str(sym.position))

        gen.add_lw('t1', '0(t1)')

        gen.add_operation('add', 't2', 't1', 't0')
        return Value('t2', True, sym.type, [], [], [])


