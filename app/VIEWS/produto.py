from flask import Blueprint, jsonify, request
from app.BLL.produto_service import listar as listar_service, buscar as buscar_service, criar as criar_service, alterar as alterar_service, deletar as deletar_service

bp_produto = Blueprint('bp_produto', __name__)

@bp_produto.route('/api/produtos', methods=['GET'])
def listar():
    code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['GET'])
def buscar(id):
    code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 400
    code, conteudo = criar_service(**request.json)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 400
    code, conteudo = alterar_service(id, **request.json)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    code, conteudo = deletar_service(id)
    return jsonify(conteudo), code