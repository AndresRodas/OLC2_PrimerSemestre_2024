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

        temp = gen.new_temp()

        if self.operador == "+":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion suma')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')

            # Traducción de suma
            gen.add_operation('add', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
    
        if self.operador == "-":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion resta')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de resta
            gen.add_operation('sub', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "*":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion multiplicacion')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de multiplicación
            gen.add_operation('mul', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "/":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion division')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de división
            gen.add_operation('div', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "<":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion menor que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de menor qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_blt('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == ">":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion mayor que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de mayor qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bgt('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        
        if self.operador == ">=":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion mayor o igual que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de mayor o igual qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bge('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == "<=":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion menor o igual que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de menor o igual qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_blez('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "==":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion igual que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de igual qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_beq('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "!=":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)

            gen.add_br()
            gen.comment('Realizando operacion diferente que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de diferente
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bne('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
    
        if self.operador == "&&":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion and')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Se agregan las etiquetas verdaderas
            for lvl in op1.truelvl:
                gen.new_body_label(lvl)
            # Ejecución de segundo operando
            op2 = self.opR.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])

            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op1.falselvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "||":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion or')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Se agregan las etiquetas falsas
            for lvl in op1.falselvl:
                gen.new_body_label(lvl)
            # Ejecución de segundo operando
            op2 = self.opR.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])

            result.truelvl.extend(op1.truelvl)
            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "!":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion not')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.extend(op1.falselvl)
            result.falselvl.extend(op1.truelvl)

            return result

        return None