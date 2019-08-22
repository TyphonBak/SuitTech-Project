from flask import Blueprint, jsonify, request

bp_venda = Blueprint('bp_venda', __name__)

@bp_venda.route('/vendas')
def listar():
    return jsonify([{}]), 200
