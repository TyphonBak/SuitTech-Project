from app.extensions import db
from app.BLL.models.venda import Venda

def listar():
    try:
        vendas = Venda.query.all()
        return None, vendas
    except Exception as e:
        return e, []

def buscar(id):
    try:
        venda = Venda.query.get(id)
        if not isinstance(venda, Venda):
            return None, None
        return None, venda
    except Exception as e:
        return e, None

def criar(dados):
    try:
        venda = Venda(**dados)
        db.session.add(venda)
        db.session.commit()
        return None, venda
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = Venda.query.filter_by(vendaid=id)
        venda = _query.first()
        if not isinstance(venda, Venda):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, venda
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        venda = Venda.query.get(id)
        if not isinstance(venda, Venda):
            return None, None
        db.session.delete(venda)
        db.session.commit()
        return None, venda
    except Exception as e:
        db.session.rollback()
        return e, None