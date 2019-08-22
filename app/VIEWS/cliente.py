from flask import Blueprint, jsonify, request

bp_cliente = Blueprint('bp_cliente', __name__)

@bp_cliente.route('/clientes')
def listar():
    return jsonify([{}]), 200