from functools import reduce
from app.extensions import db
from app.BLL.models.produto_venda import ProdutoVenda

def listar():
    try:
        produtos_venda = ProdutoVenda.query.all()
        return None, produtos_venda
    except Exception as e:
        return e, []

def buscar_por_venda(id_venda):
    try:
        produtos_venda = ProdutoVenda.query.filter_by(vendaid=id_venda)
        if not all([lambda prod: isinstance(prod, ProdutoVenda) for prod in produtos_venda]):
            return None, None
        return None, produtos_venda
    except Exception as e:
        return e, None

def criar(dados):
    try:
        produto_venda = produto_venda(**dados)
        db.session.add(produto_venda)
        db.session.commit()
        return None, produto_venda
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(id, dados):
    try:
        _query = ProdutoVenda.query.filter_by(produto_vendaid=id)
        produto_venda = _query.first()
        if not isinstance(produto_venda, ProdutoVenda):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, produto_venda
    except Exception as e:
        db.session.rollback()
        return str(e), None

def deletar(id):
    try:
        produto_venda = ProdutoVenda.query.get(id)
        if not isinstance(produto_venda, ProdutoVenda):
            return None, None
        db.session.delete(produto_venda)
        db.session.commit()
        return None, produto_venda
    except Exception as e:
        db.session.rollback()
        return e, None