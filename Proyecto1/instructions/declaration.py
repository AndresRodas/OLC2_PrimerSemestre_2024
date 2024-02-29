from interfaces.instruction import Instruction

class Declaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env):
        # Obtener simbolo
        result = self.exp.ejecutar(ast, env)
        # Validar tipo
        if result.type != self.type:
            ast.setErrors("Los tipos de dato son incorrectos")
            return
        # Agregar al entorno
        env.saveVariable(ast, self.id, result)