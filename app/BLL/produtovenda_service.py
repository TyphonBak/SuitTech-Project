from app.DAO.db_produto_venda import criar as criar_db, alterar as alterar_db, deletar as deletar_db, buscar_por_produto as buscar_db, relatorio as relatorio_db
from app.BLL.produto_service import buscar as buscar_produto
from app.BLL.categoria_service import listar as listar_categorias

def gerencia(vendaid, produtos):
    for produto in produtos:
        try:
            if produto["produtoid"] and produto['quantidade']:
                erro, produtovenda = buscar_db(vendaid, produto['produtoid'])
                if erro:
                    "erro"
                if produtovenda:
                    alterar(vendaid=vendaid, **produto)
                else:
                    criar(vendaid, produto)
            else:
                continue
        except Exception as e:
            print(e)
    
def alterar(**kwargs):
    alterar_db({
        "vendaid": kwargs.get('vendaid'),
        "produtoid": kwargs["produtoid"],
        "qtdproduto": kwargs["quantidade"]
    })

def criar(vendaid, produto):
    criar_db({
        "vendaid": vendaid,
        "produtoid": produto["produtoid"],
        "qtdproduto": produto["quantidade"]
    })

def relatorio_mensal():
    erro, relacao = relatorio_db("mensal")


    if not erro:
        relacao_final = {}
        for ano_mes, vendas in relacao.items():
            if vendas:
                produtos = [buscar_produto(id_produto, simplify=True)[1] for id_produto in set([produto['produtoid'] for produto in vendas])]
                relacao_final[ano_mes] = {}
                relacao_final[ano_mes]["produtos"] = [{ 
                        "produto": produto,
                        "qtd_total": sum(prod['qtdproduto'] if prod['produtoid'] == produto['produtoid'] else 0 for prod in vendas),
                        "renda": sum(prod['qtdproduto'] if prod['produtoid'] == produto['produtoid'] else 0 for prod in vendas) * produto['precovendavarejo']
                        } for produto in produtos]
                relacao_final[ano_mes]["renda"] = sum([prod['renda'] for prod in relacao_final[ano_mes]["produtos"] ])
                relacao_final[ano_mes]["total_produtos"] = sum([venda['qtdproduto'] for venda in vendas])
        return 200, relacao_final
    return 400, erro

def relatorio_categorias():
    erro, relacao = relatorio_db("categorias")

    relacao_final = {}

    for categoriaid, prod_vendas in relacao.items():
        print(">> ", prod_vendas)
        categoria_dict = list(filter(lambda cat: cat['categoriaid'] == categoriaid, listar_categorias()[1]))[0]
        produtos = [buscar_produto(produto_id, simplify=True)[1] for produto_id in list(set([produto["produtoid"] for produto in prod_vendas]))]
        relacao_final[categoriaid] = {}
        relacao_final[categoriaid]["detalhes"] = categoria_dict
        relacao_final[categoriaid]["produtos"] = produtos
        relacao_final[categoriaid]["renda"] = sum([prod_venda["qtdproduto"] * list(filter(lambda produto: produto['produtoid'] == prod_venda['produtoid'], produtos))[0]['precovendavarejo'] for prod_venda in prod_vendas])
        relacao_final[categoriaid]["total_produtos"] = sum([prod_venda["qtdproduto"] for prod_venda in prod_vendas])
        

    if erro: return 400, erro
    else:
        return 200, relacao_final

def relatorio_produtos():
    erro, relacao = relatorio_db("produtos")

    try:
        relacao_final = {}
        for relacao_produto in relacao:
            code, produto_dict = buscar_produto(relacao_produto["produtoid"], simplify=True)
            if code == 200:
                relacao_final[relacao_produto["produtoid"]] = {
                    "detalhes": produto_dict,
                    "total_produtos": sum([venda["qtdproduto"] for venda in relacao_produto["vendas"]])
                }
            else:
                pass
        if erro: return 400, "None"
        else: return 200, relacao_final
    except Exception as e:
        print(e)
        return 404, str(e)

def relatorios():
    relacao = {
        "mensal": relatorio_mensal()[1],
        "categoria": relatorio_categorias()[1],
        "produto": relatorio_produtos()[1]
    }
    return 200, { "relatorios": relacao, "periodo": "12 meses"}

