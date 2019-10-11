from app.DAO.db_vendedor import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db
from .models.vendedor import Vendedor

def listar():
    erro, vendedores = listar_db()
    if erro:
        return 404, erro
    return 200, [vendedor.serialize() for vendedor in vendedores]

def buscar(id):
    erro, vendedor = buscar_db(id)
    if erro:
        return 400, erro
    try:
        if vendedor:
            return 200, vendedor.serialize()
        return 404, None
    except Exception as e:
        return 400, e

def criar(dados):
    try:
        erro, vendedor = criar_db(dados)
        if erro:
            return 400, erro
        if vendedor:
            return 201, vendedor.serialize()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def alterar(id, dados):
    try:
        dados['vendedorid'] = id
        erro, vendedor = alterar_db(id, dados)
        if erro:
            return 400, erro
        if vendedor:
            return 200, vendedor.serialize()
        return 404, 'vendedor não encontrado'
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
