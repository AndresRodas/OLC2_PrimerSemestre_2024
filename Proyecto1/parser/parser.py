# PLY Imports
import parser.ply.yacc as yacc
import parser.ply.lex as Lex

# Expressions imports
from environment.types import ExpressionType
from expressions.primitive import Primitive
from expressions.operation import Operation

# Instructions imports
from instructions.print import Print

class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column

#LEXICO
reserved_words = {
    'console': 'CONSOLE', 
    'log': 'LOG', 
    'var': 'VAR'
}
# Listado de tokens
tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PUNTO',
    'COMA',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO',
    'FLOAT',
    'ID'
] + list(reserved_words.values())

t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_COMA    = r','
t_PUNTOCOMA    = r';'

#Función de reconocimiento
def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        strValue = str(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, strValue.replace('"', ''), ExpressionType.STRING)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        intValue = int(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, ExpressionType.INTEGER)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        floatValue = float(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, floatValue, ExpressionType.FLOAT)
    except ValueError:
        print("Error al convertir a decimal %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved_words.get(t.value.lower(),'ID')
     return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

#SINTACTICO
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO')
)

#START
def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion
                    | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

#Listado de instrucciones
def p_instruccion_console(t):
    'instruccion : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PUNTOCOMA'
    params = get_params(t)
    t[0] = Print(params.line, params.column, t[5])

# Expressions
def p_expression_list(t):
    '''expressionList : expressionList COMA expression
                    | expression '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

def p_expression_add(t):
    'expression : expression MAS expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "+", t[1], t[3])

def p_expression_sub(t):
    'expression : expression MENOS expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "-", t[1], t[3])

def p_expression_mult(t):
    'expression : expression POR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "*", t[1], t[3])

def p_expression_div(t):
    'expression : expression DIVIDIDO expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "/", t[1], t[3])

def p_expression_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    t[0] = t[2]

def p_expression_primitiva(t):
    '''expression    : ENTERO
                    | ID
                    | CADENA'''
    #t[0] = t[1]
    print('CHECK')
    print(t[1])
    t[0] = Primitive(0, 0, "ID ENCONTRADO", ExpressionType.STRING)

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)

class Parser:
    def __init__(self):
        pass

    def interpretar(self, input):
        lexer = Lex.lex()
        parser = yacc.yacc()
        result = parser.parse(input) #[inst1, inst2..]
        return result