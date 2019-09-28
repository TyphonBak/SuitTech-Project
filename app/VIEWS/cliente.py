from flask import Blueprint, jsonify, request
from app.BLL.cliente_service import listar as listar_service, buscar as buscar_service, criar as criar_service, alterar as alterar_service, deletar as deletar_service

bp_cliente = Blueprint('bp_cliente', __name__)

@bp_cliente.route('/api/clientes')
def listar():
    # busca serviço - code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_cliente.route('/api/clientes/<int:id>', methods=['GET'])
def buscar(id):
    # busca serviço - code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_cliente.route('/api/clientes', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 404
    # busca serviço - code, conteudo = criar_service(request.json)
    return jsonify(conteudo), code

@bp_cliente.route('/api/clientes/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 404
    # busca serviço - code, conteudo = alterar_service(id, request.json)
    return jsonify(conteudo), code

@bp_cliente.route('/api/clientes/<int:id>', methods=['DELETE'])
def deletar(id):
    # busca serviço - code, conteudo = deletar_service(id)
    return jsonify(conteudo), code