from flask import Flask, request
from parser.parser import Parser

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se define una ruta de Test
@app.route('/ping')
def saludo():
    return f'<h1>pong!</h1>'

@app.route('/interpreter', methods=['POST'])
def recibir_datos():
    jsonObj = request.json
    input_data = jsonObj.get("code")
    parser1 = Parser("ast1", "env1")
    instructionsArr = parser1.interpretar(input_data)
    for inst in instructionsArr:
        inst.ejecutar(None, None)
    return "Codigo ejecutado"

if __name__ == '__main__':
    app.run(debug=True)