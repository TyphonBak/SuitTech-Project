from flask import Blueprint, jsonify, request

bp_produto = Blueprint('bp_produto', __name__)

@bp_produto.route('/produtos', methods=['GET'])
def listar():
    return jsonify([{}]), 200

@bp_produto.route('/produtos/<int:id>', methods=['GET'])
def buscar(id):
    #chama servico de busca
    return jsonify('conteudo'), 900

@bp_produto.route('/produtos', methods=['POST'])
def criar():
    if not request.json:
        return jsonify(), 404
    #chama servico, request.json

@bp_produto.route('/produtos/<int:id>', methods=['PUT'])
def alterar(id):
    if not request.json:
        return jsonify(), 404
    #code, conteudo = chamaservico alterar
    return jsonify('conteudo'), 900

@bp_produto.route('/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    #code, conteudo = servico_alterar
    return jsonify('conteudo'), 900
