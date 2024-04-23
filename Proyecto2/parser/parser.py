# PLY Imports
import parser.ply.yacc as yacc
import parser.ply.lex as Lex

# Expressions imports
from environment.types import ExpressionType
from expressions.primitive import Primitive
from expressions.operation import Operation
from expressions.access import Access
from expressions.array import Array
from expressions.array_access import ArrayAccess
from expressions.break_statement import Break
from expressions.continue_statement import Continue
from expressions.ternario import Ternario
from expressions.call import Call
from expressions.return_statement import Return
from expressions.interface_access import InterfaceAccess

# Instructions imports
from instructions.print import Print
from instructions.declaration import Declaration
from instructions.assignment import Assignment
from instructions.array_declaration import ArrayDeclaration
from instructions.if_instruction import If
from instructions.while_instruction import While
from instructions.function import Function
from instructions.interface import Interface
from instructions.interface_declaration import InterfaceDeclaration

class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column

#LEXICO
reserved_words = {
    'console': 'CONSOLE', 
    'log': 'LOG',
    'var': 'VAR',
    'float': 'FLOAT',
    'number': 'NUMBER',
    'string': 'STRING',
    'bool': 'BOOL',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'function' : 'FUNC',
    'interface' : 'INTERFACE'
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
    'DOSPTS',
    'COMA',
    'PYC',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'IG',
    'IGIG',
    'DIF',
    'CORIZQ',
    'CORDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'MAYOR',
    'MENOR',
    'MAYORIG',
    'MENORIG',
    'AND',
    'OR',
    'NOT',
    'TERN',
    'ID'
] + list(reserved_words.values())

t_MAYOR         = r'>'
t_MENOR         = r'<'
t_MAYORIG       = r'>='
t_MENORIG       = r'<='
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVIDIDO      = r'/'
t_PUNTO         = r'\.'
t_DOSPTS        = r':'
t_COMA          = r','
t_PYC           = r';'
t_IGIG          = r'=='
t_IG            = r'='
t_DIF           = r'!='
t_CORIZQ        = r'\['
t_CORDER        = r'\]'
t_LLAVEIZQ      = r'\{'
t_LLAVEDER      = r'\}'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_TERN          = r'\?'

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

def t_DECIMAL(t):
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
    #  t.type = reserved_words.get(t.value.lower(),'ID')
    t.type = reserved_words.get(t.value,'ID')
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
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENOR', 'MAYOR'),
    ('left', 'MENORIG', 'MAYORIG'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO')
)

#START
def p_start(t):
    '''s : block'''
    t[0] = t[1]

def p_instruction_block(t):
    '''block : block instruccion
            | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

#Listado de instrucciones
def p_instruction_list(t):
    '''instruccion : print
                | ifinstruction 
                | whileinstruction 
                | declaration
                | arraydeclaration
                | assignment
                | breakstmt
                | continuestmt
                | functionstmt
                | call
                | returnstmt
                | interfacecreation
                | interdeclaration'''
    t[0] = t[1]

def p_instruction_console(t):
    'print : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PYC'
    params = get_params(t)
    t[0] = Print(params.line, params.column, t[5])

def p_instruction_if(t):
    '''ifinstruction : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE LLAVEIZQ block LLAVEDER
                    | IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'''
    params = get_params(t)
    if len(t) > 8:
        t[0] = If(params.line, params.column, t[3], t[6], t[10])
    else:
        t[0] = If(params.line, params.column, t[3], t[6], None)

def p_instruction_while(t):
    'whileinstruction : WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    t[0] = While(params.line, params.column, t[3], t[6])

def p_instruction_declaration(t):
    'declaration : VAR ID DOSPTS type IG expression PYC'
    params = get_params(t)
    t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])

def p_instruction_array_declaration(t):
    'arraydeclaration : VAR ID DOSPTS type CORIZQ CORDER IG expression PYC'
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[2], t[4], t[8])

def p_instruction_interface_declaration(t):
    'interdeclaration : VAR ID DOSPTS ID IG LLAVEIZQ interfaceContent LLAVEDER PYC'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4], t[7])

def p_instruction_interface_content(t):
    '''interfaceContent : interfaceContent COMA ID DOSPTS expression
                | ID DOSPTS expression'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_assignment(t):
    'assignment : ID IG expression PYC'
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], t[3])

def p_instruction_return(t):
    '''returnstmt : RETURN expression PYC
                | RETURN PYC'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = Return(params.line, params.column, t[2])
    else:
        t[0] = Return(params.line, params.column, None)

def p_instruction_call_function(t):
    '''call : ID PARIZQ expressionList PARDER PYC
            | ID PARIZQ PARDER PYC'''
    params = get_params(t)
    if len(t) > 5:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])
    
def p_instruction_function(t):
    'functionstmt : FUNC ID funcparams functype LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    t[0] = Function(params.line, params.column, t[2], t[3], t[4], t[6])

def p_instruction_function_params_list(t):
    '''funcparams : PARIZQ paramsList PARDER
                |  PARIZQ PARDER'''
    if len(t) > 3:
        t[0] = t[2]
    else:
        t[0] = []

def p_instruction_interface_creation(t):
    'interfacecreation : INTERFACE ID LLAVEIZQ attributeList LLAVEDER PYC'
    params = get_params(t)
    t[0] = Interface(params.line, params.column, t[2], t[4])

def p_instruction_interface_attribute(t):
    '''attributeList : attributeList ID DOSPTS type PYC
                | ID DOSPTS type PYC'''
    arr = []
    if len(t) > 5:
        param = {t[2] : t[4]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_expression_param_list(t):
    '''paramsList : paramsList COMA ID DOSPTS type
                | ID DOSPTS type'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_function_type(t):
    '''functype : DOSPTS type
                | '''
    if len(t) > 2:
        t[0] = t[2]
    else:
        t[0] = ExpressionType.NULL

def p_instruction_break(t):
    'breakstmt : BREAK PYC'
    params = get_params(t)
    t[0] = Break(params.line, params.column)

def p_instruction_continue(t):
    'continuestmt : CONTINUE PYC'
    params = get_params(t)
    t[0] = Continue(params.line, params.column)

def p_type_prod(t):
    '''type : NUMBER
            | FLOAT
            | STRING
            | BOOL'''
    if t[1] == 'number':
        t[0] = ExpressionType.INTEGER
    if t[1] == 'float': 
        t[0] = ExpressionType.FLOAT
    if t[1] == 'string':
        t[0] = ExpressionType.STRING
    if t[1] == 'bool':
        t[0] = ExpressionType.BOOLEAN

def p_expression_list(t):
    '''expressionList : expressionList COMA expression
                    | expression '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

# Expresiones aritmeticas, relacionales y lógicas
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

def p_expression_mayor(t):
    'expression : expression MAYOR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, ">", t[1], t[3])

def p_expression_menor(t):
    'expression : expression MENOR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "<", t[1], t[3])

def p_expression_mayor_igual(t):
    'expression : expression MAYORIG expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, ">=", t[1], t[3])

def p_expression_menor_igual(t):
    'expression : expression MENORIG expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "<=", t[1], t[3])

def p_expression_igual(t):
    'expression : expression IGIG expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "==", t[1], t[3])

def p_expression_diferente(t):
    'expression : expression DIF expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!=", t[1], t[3])

def p_expression_and(t):
    'expression : expression AND expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "&&", t[1], t[3])

def p_expression_or(t):
    'expression : expression OR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "||", t[1], t[3])

def p_expression_not(t):
    'expression : NOT expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!", t[2], None)

def p_expression_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    t[0] = t[2]

def p_expression_ternario(t):
    'expression : expression TERN expression DOSPTS expression'
    params = get_params(t)
    t[0] = Ternario(params.line, params.column, t[1], t[3], t[5])

def p_expression_primitiva(t):
    '''expression    : ENTERO
                    | CADENA
                    | listArray'''
    t[0] = t[1]

def p_expression_array_primitiva(t):
    '''expression : CORIZQ expressionList CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])

def p_expression_call_function(t):
    '''expression : ID PARIZQ expressionList PARDER
            | ID PARIZQ PARDER'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])

def p_expression_list_array(t):
    '''listArray : ID CORIZQ expression CORDER
                | ID'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
    else:
        t[0] = Access(params.line, params.column, t[1])

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
        result = parser.parse(input)
        return result
