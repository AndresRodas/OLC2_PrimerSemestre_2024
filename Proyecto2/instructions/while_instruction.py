from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.execute import StatementExecuter
from environment.types import ExpressionType
from expressions.continue_statement import Continue
class While(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block

    def ejecutar(self, ast, env, gen):
        gen.comment('Generando un ciclo While')
        # Agregando etiqueta de retorno
        newLabel = gen.new_label()
        gen.new_body_label(newLabel)
        # Se imprime el "if" en el código de la expresion
        condition = self.exp.ejecutar(ast, env, gen)
        # Se agregan las etiquetas verdaderas
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)
        # Instrucciones While
        while_env = Environment(env, "WHILE")
        StatementExecuter(self.block, ast, while_env, gen)
        # Salto etiqueta de retorno
        gen.add_jump(newLabel)
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            gen.new_body_label(lvl)
        return None