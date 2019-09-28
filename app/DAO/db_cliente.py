def listar():
    try:
        return None, []
    except Exception as e:
        return e, []

def buscar(id):
    try:
        return None, ()
    except Exception as e:
        return e, None

def criar(dados):
    try:
        return None, 'cliente'
    except Exception as e:
        return e, None

def alterar(id, dados):
    try:
        return None, 'cliente'
    except Exception as e:
        return e, None

def deletar(id):
    try:
        return None, ()
    except Exception as e:
        return e, None