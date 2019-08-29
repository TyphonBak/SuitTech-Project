from flask import Blueprint, jsonify, request
from app.BLL.cliente_service import listar as listar_service, buscar as buscar_service, criar as criar_service, alterar as alterar_service, deletar as deletar_service

bp_cliente = Blueprint('bp_cliente', __name__)

@bp_cliente.route('/clientes')
def listar():
    code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_cliente.route('/clientes/<int:id>', methods=['GET'])
def buscar(id):
    code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_cliente.route('/clientes', methods=['POST'])
def criar():
    code, conteudo = criar_service(request.json)
    return jsonify(conteudo), code

@bp_cliente.route('/clientes/<int:id>', methods=['PUT'])
def alterar(id):
    code, conteudo = alterar_service(id, request.json)
    return jsonify(conteudo), code

@bp_cliente.route('/clientes/<int:id>', methods=['DELETE'])
def deletar(id):
    code, conteudo = deletar_service(id)
    return jsonify(conteudo), code