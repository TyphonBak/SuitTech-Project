from app.DAO.db_venda import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db
from .models.venda import Venda

def listar():
    erro, vendas = listar_db()
    if erro:
        return 404, erro
    return 200, [venda.serialize() for venda in vendas]

def buscar(id):
    erro, venda = buscar_db(id)
    if erro:
        return 400, erro
    try:
        if venda:
            return 200, venda.serialize()
        return 404, None
    except Exception as e:
        return 400, e

def criar(dados):
    try:
        erro, venda = criar_db(dados)
        if erro:
            return 400, erro
        if venda:
            return 201, venda.serialize()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def alterar(id, dados):
    try:
        dados['vendaid'] = id
        erro, venda = alterar_db(id, dados)
        if erro:
            return 400, erro
        if venda:
            return 200, venda.serialize()
        return 404, 'venda não encontrado'
    except Exception as e:
        return 400, e

def deletar(id):
    try:
        erro, reposta = deletar_db(id)
        if erro:
            return 404, erro
        elif reposta:
            return 204, 'No Content'
        return 404, 'Referencia não existente'
    except Exception as e:
        return 400, e
