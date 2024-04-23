from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from expressions.continue_statement import Continue
class If(Instruction):
    def __init__(self, line, col, exp, block, elseblock):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block
        self.elseblock = elseblock

    def ejecutar(self, ast, env, gen):
        gen.comment('Generando un If')
        # Se imprime el "if" en el código de la expresion
        condition = self.exp.ejecutar(ast, env, gen)
        # Etiqueta de salida
        newLabel = gen.new_label()
        # Se agregan las etiquetas verdaderas
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)
        # Instrucciones If
        if_env = Environment(env, "IF")
        StatementExecuter(self.block, ast, if_env, gen)
        # Salto etiqueta de salida
        gen.add_jump(newLabel)
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            gen.new_body_label(lvl)
        # Validar else
        if self.elseblock != None:
            else_env = Environment(env, "ELSE")
            StatementExecuter(self.elseblock, ast, else_env, gen)
        # Etiqueta de salida
        gen.new_body_label(newLabel)
        return None