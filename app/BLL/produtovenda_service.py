from app.DAO.db_produto_venda import criar as criar_db, alterar as alterar_db, deletar as deletar_db, buscar_por_produto as buscar_db

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
            pass

    
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