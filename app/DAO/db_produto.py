from app.extensions import db
from app.BLL.models.produto import Produto
from app.BLL.models.categoria import Categoria

def listar():
    try:
        produtos = Produto.query.join(Categoria).all()
        return None, produtos
    except Exception as e:
        return e, []

def buscar(id):
    try:
        produto = Produto.query.join(Categoria).filter(Produto.produtoid==id).first()
        if not isinstance(produto, Produto):
            return None, None
        return None, produto
    except Exception as e:
        return e, None

def criar(dados):
    try:
        produto = Produto(**dados)
        db.session.add(produto)
        db.session.commit()
        return None, produto
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = Produto.query.filter_by(produtoid=id)
        produto = _query.first()
        if not isinstance(produto, Produto):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, produto
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        produto = Produto.query.get(id)
        if not isinstance(produto, Produto):
            return None, None
        db.session.delete(produto)
        db.session.commit()
        return None, produto
    except Exception as e:
        db.session.rollback()
        return e, None