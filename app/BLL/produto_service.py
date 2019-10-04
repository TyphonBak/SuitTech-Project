from app.DAO.db_produto import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db

def listar():
    erro, produtos = listar_db()
    if erro:
        return 404, erro
    return 200, [produto.serialize() for produto in produtos]

def buscar(id):
    erro, produto = buscar_db(id)
    if erro:
        return 400, erro
    try:
        if produto:
            return 200, produto.serialize()
        return 404, None
    except Exception as e:
        return 400, e

def criar(dados):
    try:
        erro, produto = criar_db(dados)
        if erro:
            return 400, erro
        if produto:
            return 201, produto.serialize()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def alterar(id, dados):
    try:
        dados['produtoid'] = id
        erro, produto = alterar_db(id, dados)
        if erro:
            return 400, erro
        if produto:
            return 200, produto.serialize()
        return 404, 'produto não encontrado'
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
