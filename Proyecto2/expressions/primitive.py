from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.value import Value

class Primitive(Expression):
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.type = type

    def ejecutar(self, ast, env, gen):
        if(self.type == ExpressionType.INTEGER):
            temp = gen.new_temp()
            gen.add_br()
            gen.add_li('t0', str(self.value))
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return  Value(str(temp), self.value, self.type, [], [], [])