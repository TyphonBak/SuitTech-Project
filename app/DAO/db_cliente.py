from app.extensions import db
from app.BLL.models.cliente import Cliente

def listar():
    try:
        clientes = Cliente.query.all()
        print('Esses clientes... ', clientes)
        return None, clientes
    except Exception as e:
        return str(e), []

def buscar(id):
    try:
        cliente = Cliente.query.get(id)
        if not isinstance(cliente, Cliente):
            return None, None
        return None, cliente
    except Exception as e:
        return str(e), None

def criar(dados):
    try:
        cliente = Cliente(**dados)
        db.session.add(cliente)
        db.session.commit()
        return None, cliente
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = Cliente.query.filter_by(clienteid=id)
        cliente = _query.first()
        if not isinstance(cliente, Cliente):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, cliente
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        cliente = Cliente.query.get(id)
        if not isinstance(cliente, Cliente):
            return None, None
        db.session.delete(cliente)
        db.session.commit()
        return None, cliente
    except Exception as e:
        db.session.rollback()
        return str(e), None