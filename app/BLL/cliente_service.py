from app.DAO.db_cliente import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db
from .models.cliente import Cliente

def listar():
    erro, clientes = listar_db()
    if erro:
        return 404, erro
    return 200, [cliente.serialize() for cliente in clientes]

def buscar(id):
    erro, cliente = buscar_db(id)
    if erro:
        return 400, erro
    try:
        if cliente:
            return 200, cliente.serialize()
        return 404, None
    except Exception as e:
        return 400, e

def criar(dados):
    try:
        erro, cliente = criar_db(dados)
        if erro:
            return 400, erro
        if cliente:
            return 201, cliente.serialize()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def alterar(id, dados):
    try:
        dados['clienteid'] = id
        erro, cliente = alterar_db(id, dados)
        if erro:
            return 400, erro
        if cliente:
            return 200, cliente.serialize()
        return 404, 'Cliente não encontrado'
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
