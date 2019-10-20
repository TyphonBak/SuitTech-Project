from app.DAO.db_venda import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db
from .models.venda import Venda
from .produto_service import buscar as busca_produto
from .produtovenda_service import gerencia as gerencia_produtovenda

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
        return 400, str(e)

def criar(produtos=None, **dados):
    try:
        erro, venda = criar_db(dados)
        if erro:
            return 400, erro
        if venda:
            if produtos:
                gerencia_produtovenda(venda.vendaid, produtos)
            return 201, venda.serialize()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, "Algo está incorreto."

def alterar(id, produtos=None, **kwargs):
    if produtos:
        gerencia_produtovenda(id, produtos)
    try:
        if kwargs:
            erro, venda = alterar_db(id, kwargs)
            if erro:
                return 400, erro
            if venda:
                return 200, venda.serialize()
            else:
                return 400, None
        return 404, 'venda não encontrado'
    except Exception as e:
        return 400, str(e)

def deletar(id):
    try:
        erro, reposta = deletar_db(id)
        if erro:
            return 404, erro
        elif reposta:
            return 204, 'No Content'
        return 404, 'Referencia não existente'
    except Exception as e:
        return 400, str(e)
