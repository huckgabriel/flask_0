from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/') #Primera ruta

#Funcion que se ejecuta cuando el usuario elige esa ruta
def index():
    return 'Index'

#defino una nueva ruta
@app.route('/ping')
def ping():
    return jsonify({"mensaje": "pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre}) #genera un objeto con un nombre de usuario

@app.route('/usuarios/<int:id>') #obtengo un objeto por el id
def usuario_by_id(id):
    return jsonify({"id":id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre) #cualquier ruta que no coincida con el nombre devuelve un error 404

#GET todos los 'recursos'
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"})

#POST nuevo 'recurso'
@app.route('/recurso', methods = ['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})

# GET un 'recurso' a traves de su id
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #buscar en la BD 
    return jsonify({"recurso":{
                    "name": "nombre correspondiente a ese id",
                    "modelo": "modelo correspondiente a ese id"
    }})
#Preparar para cuando se ejecute un servidor en la nube

if __name__ == '__main__':
    app.run(debug=True, port=5000)