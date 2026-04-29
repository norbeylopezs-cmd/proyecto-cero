from flask import Flask  # se importa flask que es la herramienta que nos permite crear la Api

app = Flask(__name__)  # desde aqui comienza la app

@app.route('/health', methods=['GET'])  # Cuando alguien entre a esta url, usa esta función
def health():  # se ejecuta cuando en la parte de arriba se ejecuta health y me da metodo bien en formato json 
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(debug=True)  # sirve para encender la api, escuchar peticiones, permitir el acceso desde el navegador