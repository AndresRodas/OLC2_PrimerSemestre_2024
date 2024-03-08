from environment.types import ExpressionType

def RootExecuter(instructionList, ast, env):
    for inst in instructionList:
        inst.ejecutar(ast, env)

def StatementExecuter(instructionList, ast, env):
    for inst in instructionList:
        res = inst.ejecutar(ast, env)
        if res != None:
            if res.type == ExpressionType.RETURN:
                return res.value
            return res
    return None