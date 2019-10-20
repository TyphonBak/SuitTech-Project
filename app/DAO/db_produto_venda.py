from functools import reduce
from app.extensions import db
from app.BLL.models.produto_venda import ProdutoVenda

def listar():
    try:
        produtos_venda = ProdutoVenda.query.all()
        return None, produtos_venda
    except Exception as e:
        return e, []

def buscar_por_produto(vendaid, id_produto):
    try:
        produto_venda = ProdutoVenda.query.filter(ProdutoVenda.vendaid==vendaid, ProdutoVenda.produtoid==id_produto).first()
        if not isinstance(produto_venda, ProdutoVenda):
            return None, None
        return None, produto_venda
    except Exception as e:
        return e, None

def criar(dados):
    try:
        produto_venda = ProdutoVenda(**dados)
        db.session.add(produto_venda)
        db.session.commit()
        return None, produto_venda
    except Exception as e:
        db.session.rollback()
        return str(e.__dict__.get('orig')), None

def alterar(dados):
    try:
        _query = ProdutoVenda.query.filter(ProdutoVenda.vendaid==dados.get('vendaid'), ProdutoVenda.produtoid==dados.get('produtoid'))
        produto_venda = _query.first()
        if not isinstance(produto_venda, ProdutoVenda):
            return None, None
        _query.update(dados)
        db.session.commit()
        return None, produto_venda
    except Exception as e:
        import pdb; pdb.set_trace()
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