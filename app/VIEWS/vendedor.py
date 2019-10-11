from flask import Blueprint, request, jsonify
from app.BLL.vendedor_service import criar as criar_service, listar as listar_service, buscar as buscar_service, alterar as alterar_service, deletar as deletar_service

bp_vendedor = Blueprint('bp_vendedor', __name__)

@bp_vendedor.route('/api/vendedores', methods=['GET'])
def listar():
    code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_vendedor.route('/api/vendedores/<int:id>', methods=['GET'])
def buscar(id):
    code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_vendedor.route('/api/vendedores', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 400
    code, conteudo = criar_service(request.json)
    return jsonify(conteudo), code

@bp_vendedor.route('/api/vendedores/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 404
    code, conteudo = alterar_service(id, request.json)
    return jsonify(conteudo), code

@bp_vendedor.route('/api/vendedores/<int:id>', methods=['DELETE'])
def deletar(id):
    code, conteudo = deletar_service(id)
    return jsonify(conteudo), code