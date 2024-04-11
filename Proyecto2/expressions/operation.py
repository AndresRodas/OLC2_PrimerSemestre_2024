from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.value import Value

class Operation(Expression):
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def ejecutar(self, ast, env, gen):

        # Ejecución de operandos
        op1 = self.opL.ejecutar(ast, env, gen)
        op2 = self.opR.ejecutar(ast, env, gen)

        gen.add_br()
        gen.add_li('t3', str(op1.value))
        gen.add_lw('t1', '0(t3)')
        gen.add_li('t3', str(op2.value))
        gen.add_lw('t2', '0(t3)')
        temp = gen.new_temp()

        if self.operador == "+":
            gen.add_operation('add', 't0', 't1', 't2')
            newVal = op1.intValue + op2.intValue
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), newVal, ExpressionType.INTEGER, [], [], [])
    
        if self.operador == "-":
            gen.add_operation('sub', 't0', 't1', 't2')
            newVal = op1.intValue - op2.intValue
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), newVal, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "*":
            gen.add_operation('mul', 't0', 't1', 't2')
            newVal = op1.intValue * op2.intValue
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), newVal, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "/":
            gen.add_operation('div', 't0', 't1', 't2')
            newVal = op1.intValue / op2.intValue
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), newVal, ExpressionType.INTEGER, [], [], [])
        return None