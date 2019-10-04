from app.extensions import db
from app.BLL.models.categoria import Categoria

def listar():
    try:
        categorias = Categoria.query.all()
        return None, categorias
    except Exception as e:
        return e, []

def buscar(id):
    try:
        categoria = Categoria.query.get(id)
        if not isinstance(categoria, Categoria):
            return None, None
        return None, categoria
    except Exception as e:
        return e, None

def criar(dados):
    try:
        categoria = Categoria(**dados)
        db.session.add(categoria)
        db.session.commit()
        return None, categoria
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = Categoria.query.filter_by(categoriaid=id)
        categoria = _query.first()
        if not isinstance(categoria, Categoria):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, categoria
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        categoria = Categoria.query.get(id)
        if not isinstance(categoria, Categoria):
            return None, None
        db.session.delete(categoria)
        db.session.commit()
        return None, categoria
    except Exception as e:
        db.session.rollback()
        return e, None