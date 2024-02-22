from flask import Flask, request, jsonify
from parser.parser import Parser
from environment.ast import Ast
from environment.environment import Environment

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se define una ruta de Test
@app.route('/ping')
def saludo():
    return f'<h1>pong!</h1>'

@app.route('/interpreter', methods=['POST'])
def recibir_datos():
    # Obtención del código
    jsonObj = request.json
    input_data = jsonObj.get("code")
    # Creación del entorno global
    env = Environment(None, 'GLOBAL')
    # Creación del AST
    ast = Ast()
    # Creación del parser
    parser = Parser()
    instructionsArr = parser.interpretar(input_data)
    for inst in instructionsArr:
        inst.ejecutar(ast, env)
    # Estructurando respuesta
    res = {"result": True,"console":ast.getConsole(),"errors":ast.getErrors()}
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)