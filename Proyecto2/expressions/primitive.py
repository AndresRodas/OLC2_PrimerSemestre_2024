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
        temp = gen.new_temp()
        if(self.type == ExpressionType.INTEGER):
            gen.add_br()
            gen.comment('Agregando un primitivo numerico')
            gen.add_li('t0', str(self.value))
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return  Value(str(temp), True, self.type, [], [], [])
        elif (self.type == ExpressionType.STRING):
            nameId = 'str_'+str(temp)
            gen.variable_data(nameId, 'string', '\"'+str(self.value)+'\"')
            return  Value(nameId, False, self.type, [], [], [])