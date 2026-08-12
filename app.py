from flask import Flask, jsonify

from routes.usuario_routes import usuario_routes


app = Flask(__name__)

app.register_blueprint(usuario_routes)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensagem": "API Connect funcionando com sucesso!"
    }), 200


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )