#LEXICO
# Listado de tokens
tokens = (
    'CONSOLE',
    'LOG',
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PUNTO',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO'
)

t_CONSOLE  = r'console'
t_LOG  = r'log'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'

#Función de reconocimiento
def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = ''
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor del entero es incorrecto %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

#SINTACTICO
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
)

#START
def p_instrucciones_lista(t):
    '''instrucciones : instruccion instrucciones
                    | instruccion '''

#Listado de instrucciones
def p_instruccion_console(t):
    '''instruccion : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA'''
    print(t[5])

#Expresion
def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | CADENA'''
    t[0] = t[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")



import ply.lex as Lex
import ply.yacc as yacc

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input_text = f.read()
    print("************ENTRADA***************")
    print(input_text)
    lexer = Lex.lex()
    parser = yacc.yacc()
    print("************SALIDA***************")
    result = parser.parse(input_text)
