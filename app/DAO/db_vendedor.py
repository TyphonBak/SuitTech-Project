from app.extensions import db
from app.BLL.models.vendedor import Vendedor

def listar():
    try:
        vendedores = Vendedor.query.all()
        return None, vendedores
    except Exception as e:
        return e, []

def buscar(id):
    try:
        vendedor = Vendedor.query.get(id)
        if not isinstance(vendedor, Vendedor):
            return None, None
        return None, vendedor
    except Exception as e:
        return e, None

def criar(dados):
    try:
        vendedor = Vendedor(**dados)
        db.session.add(vendedor)
        db.session.commit()
        return None, vendedor
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = Vendedor.query.filter_by(vendedorid=id)
        vendedor = _query.first()
        if not isinstance(vendedor, Vendedor):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, vendedor
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        vendedor = Vendedor.query.get(id)
        if not isinstance(vendedor, Vendedor):
            return None, None
        db.session.delete(vendedor)
        db.session.commit()
        return None, vendedor
    except Exception as e:
        db.session.rollback()
        return e, None