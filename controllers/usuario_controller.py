from flask import jsonify, request

from data.usuarios import usuarios, gerar_id


def listar_usuarios():
    return jsonify(usuarios), 200


def cadastrar_usuario():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "error": "O corpo da requisição deve conter JSON."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome:
        return jsonify({
            "error": "O campo nome é obrigatório."
        }), 400

    if not email:
        return jsonify({
            "error": "O campo e-mail é obrigatório."
        }), 400

    novo_usuario = {
        "id": gerar_id(),
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201

def buscar_usuario_por_id(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    return jsonify(usuario), 200

def atualizar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "erro": "O corpo da requisição deve conter JSON."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "erro": "Nome e e-mail são obrigatórios."
        }), 400

    usuario["nome"] = nome
    usuario["email"] = email

    return jsonify(usuario), 200


def remover_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    usuarios.remove(usuario)

    return "", 204