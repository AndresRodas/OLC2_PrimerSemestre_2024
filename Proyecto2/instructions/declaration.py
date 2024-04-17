from interfaces.instruction import Instruction
from environment.symbol import Symbol

class Declaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        # Generar simbolo
        result = self.exp.ejecutar(ast, env, gen)
        sym = Symbol(self.line, self.col, self.id, self.type, result.value)
        # Validar tipo
        if result.type != self.type:
            ast.setErrors("Los tipos de dato son incorrectos")
            return
        # Agregar al entorno
        env.saveVariable(ast, self.id, sym)
        return None