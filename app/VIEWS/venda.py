from flask import Blueprint, jsonify, request
from app.BLL.venda_service import listar as listar_service, buscar as buscar_service, criar as criar_service,  alterar as alterar_service, deletar as deletar_service

bp_venda = Blueprint('bp_venda', __name__)

@bp_venda.route('/api/vendas', methods=['GET'])
def listar():
    code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_venda.route('/api/vendas/<int:id>', methods=['GET'])
def buscar(id):
    code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_venda.route('/api/vendas', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 404
    code, conteudo = criar_service(request.json)
    return jsonify(conteudo), code

@bp_venda.route('/api/vendas/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 400
    code, conteudo = alterar_service(request.json)
    return jsonify(conteudo), code

@bp_venda.route('/api/vendas/<int:id>', methods=['DELETE'])
def deletar(id):
    code, conteudo = deletar_service(id)
    return jsonify(conteudo), code