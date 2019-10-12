from app.DAO.db_categoria import listar as listar_db

def listar():
    try:
        return [categoria.serialize() for categoria in listar_db()]
    except Exception:
        return 503, None

def categorizar_produtos(categorias, produtos):
    [produto['categoria'] = {
        'categoriaid': produto.get('categoriaid'),
        'nome': categorias.get(produto.get('categoriaid'))
    } for produto in produtos]
    return produtos

def categoriza(produtos):
    categorias = listar()
    if isinstance(produtos, list):
        return categorizar_produtos(categorias, produtos)
    elif isinstance(produtos, dict):
        return categorizar_produtos(categorias, [produtos])
    else:
        return 'error'