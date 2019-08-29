from app.DAO.db_cliente import listar as listar_db, buscar as buscar_db, criar as criar_db, alterar as alterar_db, deletar as deletar_db
from .models.cliente import Cliente

def listar():
    erro, lista = listar_db()
    if erro:
        return 404, erro
    return 200, lista

def buscar(id):
    erro, cliente_tupla = buscar_db(id)
    if erro:
        return 400, erro
    try:
        cliente = Cliente.cria_de_tupla(cliente_tupla)
        if cliente:
            return 200, cliente.__dict__()
        return 404, None
    except Exception as e:
        return 400, e

def criar(dados):
    try:
        cliente = Cliente.cria(dados)
        erro, cliente_tupla = criar_db(cliente)
        if erro:
            return 400, erro
        cliente = Cliente.cria_de_tupla(cliente_tupla)
        if cliente:
            return 201, cliente.__dict__()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def alterar(id, dados):
    try:
        cliente = Cliente.cria(dados)
        erro, cliente_tupla = alterar_db(id, cliente)
        if erro:
            400, erro
        cliente = Cliente.cria_de_tupla(cliente_tupla)
        if cliente:
            return 200, cliente.__dict__()
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e

def deletar(id):
    try:
        erro, reposta = deletar_db(id)
        if erro:
            return 404, erro
        elif reposta:
            return 204, 'No Content'
        return 503, 'Database Unavailable'
    except Exception as e:
        return 400, e