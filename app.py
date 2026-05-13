# importamos Flask desde la libreria flask
# Flask sirve para crear APIs y servidores web en Python
from flask import Flask


# aqui se crea la aplicacion
# __name__ le dice a Flask cual es el archivo principal
app = Flask(__name__)


# ==================================================
# STATUS 200
# ==================================================

# esta ruta sirve para comprobar que la API funciona correctamente
@app.route('/health', methods=['GET'])

# esta funcion se ejecuta cuando alguien entra a /health
def health():

    # devolvemos un JSON
    # y el codigo 200 significa "todo salio bien"
    return {"status": "ok"}, 200


# ==================================================
# STATUS 400
# ==================================================

# esta ruta simula un bad request
@app.route('/bad-request', methods=['GET'])

# esta funcion se ejecuta cuando alguien entra a /bad-request
def bad_request():

    # devolvemos un mensaje de error
    # el status 400 significa que el cliente envio algo incorrecto
    return {"error": "bad request"}, 400


# ==================================================
# STATUS 401
# ==================================================

# esta ruta simula un acceso no autorizado
@app.route('/unauthorized', methods=['GET'])

# esta funcion se ejecuta cuando alguien entra a /unauthorized
def unauthorized():

    # devolvemos un mensaje de error
    # el status 401 significa "no autorizado"
    return {"error": "unauthorized"}, 401


# ==================================================
# STATUS 404
# ==================================================

# esta ruta simula que el recurso no fue encontrado
@app.route('/not-found', methods=['GET'])

# esta funcion se ejecuta cuando alguien entra a /not-found
def not_found():

    # devolvemos un mensaje de error
    # el status 404 significa "no encontrado"
    return {"error": "not found"}, 404


# ==================================================
# STATUS 500
# ==================================================

# esta ruta simula un error interno del servidor
@app.route('/server-error', methods=['GET'])

# esta funcion se ejecuta cuando alguien entra a /server-error
def server_error():

    # devolvemos un mensaje de error
    # el status 500 significa "error interno del servidor"
    return {"error": "internal server error"}, 500


# esta condicion verifica si el archivo se esta ejecutando directamente
if __name__ == '__main__':

    # app.run() sirve para iniciar el servidor Flask
    # debug=True muestra errores detallados
    # y reinicia automaticamente cuando haces cambios
    app.run(debug=True)