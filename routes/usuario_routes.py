from flask import Blueprint

from controllers.usuario_controller import (
    atualizar_usuario,
    buscar_usuario_por_id,
    cadastrar_usuario,
    listar_usuarios,
    remover_usuario
)


usuario_routes = Blueprint("usuario_routes", __name__)


usuario_routes.route(
    "/usuarios",
    methods=["GET"]
)(listar_usuarios)


usuario_routes.route(
    "/usuarios",
    methods=["POST"]
)(cadastrar_usuario)


usuario_routes.route(
    "/usuarios/<int:id>",
    methods=["GET"]
)(buscar_usuario_por_id)


usuario_routes.route(
    "/usuarios/<int:id>",
    methods=["PUT"]
)(atualizar_usuario)


usuario_routes.route(
    "/usuarios/<int:id>",
    methods=["DELETE"]
)(remover_usuario)