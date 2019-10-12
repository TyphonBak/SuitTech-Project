from flask import Blueprint, jsonify
from app.BLL.categoria_service import listar as listar_service

bp_categoria = Blueprint('Categoria BP', __name__)

@bp_categoria('/categorias', methods=['GET'])
def listar():
    code, conteudo = listar_service()
    return jsonify(conteudo), code