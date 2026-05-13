from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Se crea la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

# Conexión entre Flask y SQLAlchemy
db = SQLAlchemy(app)


# Modelo de usuarios
class User(db.Model):

    # ID único de cada usuario
    id = db.Column(db.Integer, primary_key=True)

    # Nombre del usuario
    name = db.Column(db.String(100), nullable=False)

    # Correo del usuario
    email = db.Column(db.String(100), nullable=False)


# Ruta para crear usuarios
@app.route('/users', methods=['POST'])
def create_user():

    # Obtiene el JSON enviado en la petición
    data = request.get_json()

    # Crea un nuevo usuario con los datos recibidos
    new_user = User(
        name=data['name'],
        email=data['email']
    )

    # Agrega el usuario a la sesión
    db.session.add(new_user)

    # Guarda los cambios en la base de datos
    db.session.commit()

    # Devuelve una respuesta en formato JSON
    return {
        "message": "Usuario creado",
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }, 201


# Ruta para comprobar que la API funciona
@app.route('/health', methods=['GET'])
def health():

    return {"status": "ok"}, 200


# Ruta que simula un error 400
@app.route('/bad-request', methods=['GET'])
def bad_request():

    return {"error": "bad request"}, 400


# Ruta que simula un error 401
@app.route('/unauthorized', methods=['GET'])
def unauthorized():

    return {"error": "unauthorized"}, 401


# Ruta que simula un error 404
@app.route('/not-found', methods=['GET'])
def not_found():

    return {"error": "not found"}, 404


# Ruta que simula un error 500
@app.route('/server-error', methods=['GET'])
def server_error():

    return {"error": "internal server error"}, 500


# Crea las tablas si no existen
with app.app_context():
    db.create_all()


# Inicia el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)