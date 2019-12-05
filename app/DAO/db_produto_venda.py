from functools import reduce
from datetime import date, datetime
from app.extensions import db
from app.BLL.models.produto_venda import ProdutoVenda
from app.DAO.db_produto import buscar as buscar_produto_db
from app.BLL.models.produto import Produto

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

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

def relatorio_mensal():
    start = datetime.now().date()
    end = monthdelta(start, -12)

    try:
        vendas = ProdutoVenda.query.filter(ProdutoVenda.dt_inclusao > end).filter(ProdutoVenda.dt_inclusao < start).all()
        meses = {}
        for i in range(1, 13):
            vendas_mes = list(filter(lambda venda: venda.dt_inclusao.month == i, vendas))
            if len(vendas_mes):
                meses[f'{vendas_mes[0].dt_inclusao.year}-{i}'] = [venda.serialize() for venda in vendas_mes]
        return None, meses
    except Exception as e:
        print(e)
        return str(e), None


def relatorio_categorias():
    try:
        start = datetime.now().date()
        end = monthdelta(start, -12)

        produtos_id = [venda.produtoid for venda in ProdutoVenda.query.with_entities(ProdutoVenda.produtoid).distinct().all()]
        produtos = [buscar_produto_db(prodid)[1] for prodid in produtos_id]
        relacao = {}
        for produto in produtos:
            if produto.categoriaid not in relacao:
                relacao[produto.categoriaid] = [produto]
            else:
                relacao[produto.categoriaid] += [produto]
        relacao_final = {}
        for categid, products in relacao.items():
            lista_vendas = [ProdutoVenda.query.filter(ProdutoVenda.dt_inclusao > end).filter(ProdutoVenda.dt_inclusao < start).filter(ProdutoVenda.produtoid == prod.produtoid).all() for prod in products]
            relacao_final[categid] = [venda.serialize() for venda in lista_vendas[0]]
            
        return None, relacao_final
    except Exception as e:
        return str(e), None

def relatorio_produtos():
    try:
        start = datetime.now().date()
        end = monthdelta(start, -12)

        produtos_id = [venda.produtoid for venda in ProdutoVenda.query.with_entities(ProdutoVenda.produtoid).distinct().all()]
        lista_vendas = [ProdutoVenda.query.filter(ProdutoVenda.dt_inclusao > end).filter(ProdutoVenda.dt_inclusao < start).filter(ProdutoVenda.produtoid == prodid).all() for prodid in produtos_id]
        return None, [{ "produtoid": lista[0].produtoid, "vendas": [venda.serialize() for venda in lista]} for lista in lista_vendas]
    except Exception as e:
        return str(e), None

def relatorio(tipo):
    relatorios = {
        "mensal": relatorio_mensal,
        "categorias": relatorio_categorias,
        "produtos": relatorio_produtos
    }

    try:
        erro, relacao = relatorios[tipo]()
        return erro, relacao
    except Exception as e:
        print(e)
        return str(e), None