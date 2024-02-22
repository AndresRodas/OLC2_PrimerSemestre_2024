from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol

dominant_table = [
    [ExpressionType.INTEGER, ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.FLOAT,   ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.STRING,  ExpressionType.STRING, ExpressionType.STRING, ExpressionType.STRING,  ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.STRING, ExpressionType.BOOLEAN, ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.NULL,   ExpressionType.NULL,    ExpressionType.NULL],
]

class Operation(Expression):
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def ejecutar(self, ast, env):

        op1 = self.opL.ejecutar(ast, env)
        op2 = self.opR.ejecutar(ast, env)
        dominant_type = dominant_table[op1.type.value][op2.type.value]
        # Suma
        if self.operador == "+":
            symbol = Symbol(line=self.line, col=self.col, value=op1.value+op2.value, type=dominant_type)
            return symbol
        # Resta
        if self.operador == "-":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value-op2.value, type=dominant_type)
            print("Error: tipos incorrectos para restar")
        # Multiplicación
        if self.operador == "*":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value*op2.value, type=dominant_type)
            print("Error: tipos incorrectos para multiplicar")
        # División
        if self.operador == "/":
            if op2.value == 0:
                print("Error: no se puede dividir por 0")
                return 
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value/op2.value, type=dominant_type)
            print("Error: tipos incorrectos para dividir")
        
        return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)