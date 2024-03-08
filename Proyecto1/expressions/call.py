from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.environment import Environment
from environment.execute import StatementExecuter
from expressions.continue_statement import Continue

class Call(Expression):
    def __init__(self, line, col, id, params):
        self.line = line
        self.col = col
        self.id = id
        self.params = params

    def ejecutar(self, ast, env):
        # Buscar la función
        func = env.getFunction(ast, self.id)
        if func == {}:
            return
        # Validar cantidad de parámetros
        if len(self.params) != len(func['params']):
            ast.setErrors(f"La función esperaba {len(func['params'])} parámetros, pero se obtuvieron {len(self.params)}")
            return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)
        # Crear entorno de funcion
        function_env = Environment(env.getGlobalEnvironment(), 'FUNCTION_'+self.id)
        # Validar parámetros
        if len(self.params) > 0:
            symbolList = []
            # Lista de parámetros
            for i in range(len(self.params)):
                # Obteniendo simbolo del parámetro
                symParam = self.params[i].ejecutar(ast, env)
                symbolList.append(symParam)
                # Guardando valores de funcion
                id_param = list(func['params'][i].keys())[0]
                type_param = list(func['params'][i].values())[0]
                # Validando tipos
                if type_param != symParam.type:
                    ast.setErrors('Los tipos de parámetros son incorrectos')
                    return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)
                # Agregar parámetros al entorno
                function_env.saveVariable(ast, id_param, symParam)
        # Ejecutar bloque
        returnValue = StatementExecuter(func['block'], ast, function_env)
        if returnValue != None:
            if returnValue.type != func['type']:
                ast.setErrors('El tipo de retorno es incorrecto')
                return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)  
            return returnValue        
        return None

