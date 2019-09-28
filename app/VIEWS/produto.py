from flask import Blueprint, jsonify, request

bp_produto = Blueprint('bp_produto', __name__)

@bp_produto.route('/api/produtos', methods=['GET'])
def listar():
    # busca serviço - code, conteudo = listar_service()
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['GET'])
def buscar(id):
    # busca serviço - code, conteudo = buscar_service(id)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 404
    # busca serviço - code, conteudo = criar_service(request.json)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 404
    # busca serviço - code, conteudo = alterar_service(request.json)
    return jsonify(conteudo), code

@bp_produto.route('/api/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    # busca serviço - code, conteudo = deletar_service(id)
    return jsonify(conteudo), code
