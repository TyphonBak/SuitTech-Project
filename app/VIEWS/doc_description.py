cliente_id = {"clienteid": 31}

cliente = {
  "cep": 7257820.0,
  "cidade": "Azevedo do Amparo",
  "cpf_cnpj": 92762978892.0,
  "email": "lais52@yahoo.com.br",
  "logradouro": "Praça de da Mata",
  "nome": "Ana Maria Gomes",
  "numero": 632.0,
  "telefone": 120577089.0,
  "uf": "AP"
}

cliente_min = {
    "clienteid": 31,
    "email": "lais52@yahoo.com.br",
    "nome": "Ana Maria Gomes",
    "telefone": 120577089.0
}

vendedor_id = {"vendedorid": 1}

vendedor = {
    "cpf": 1213454612.0,
    "email": "silvajoao@email.com",
    "nome": "Silva João"
}

categoria = { 
    "categoria": {
        "cateoriaid": 1,
        "nome": "Categoria"
    }
}

categoria_id = {"categoriaid": 1}

produto_id = {"produtoid": 1}

produto = {
  "altura": 50.0,
  "cor": "Azul",
  "descricao": "Descricao",
  "estoque": 2,
  "imposto": 7.0,
  "largura": 20.0,
  "material": "Lã sintétoca",
  "nome": "Tal Pano",
  "peso": 100.0,
  "precocusto": 5.5,
  "precovendaatacado": 13.0,
  "precovendavarejo": 15.0
}

produto_min = {
    "nome": "Tal Pano",
    "produtoid": 1
}

venda_id = {"vendaid": 13}

venda = {
  "produtos": [
    {
      "produtoid": 1,
      "qtdproduto": 2
    }
  ]
}

venda_req = {
    **cliente_id,
    **venda,
    **vendedor_id
}

doc= {
    "url base": "api-titarte.herokuapp.com/",
    "topicos": {
        "Referencia API": "A API SuitTech esta organizada em REST. a API possui URLs orientada a recursos, \
        aceitando solicitações via JSON com o protocolo HTTP padrão, retornando respostas codificadas em JSON.",
        "Autenticação": "Atualmente a API é exclusiva para uso interno, desta forma a \
        autenticação para terceiros foi esta desabilitada.",
        "Respostas da API": {
            "descricao": "Utilizamos as respostas do protocolo HTTP para indicar requisições com falhas ou sucesso \
                da nossa API. No geral os códigos que contém o range de -2xx- indicam que a requisição foi feita com \
                sucesso. Já os de range -4xx- e -5xx- indicam um erro.",
            "respostas": {
                200: {
                    "descricao": "Solicitação interpretada com exito",
                    "status": 'OK'
                },
                201: {
                    "descricao": "Objeto criado com exito",
                    "status": 'Criado'
                },
                204:  {
                    "descricao": "Objeto deletado com exito",
                    "status": 'Sem conteúdo'
                },        
                400: {
                    "descricao": "A requisição não pode ser entendida pelo servidor devido a erro de sintax. O client NÃO PODE repetir a requisição sem modificações",
                    "status": 'Requisição incorreta'
                },
                401: {
                    "descricao": "A requisição requer autenticação de usuário",
                    "status": 'Não autorizado'
                },
                404: {
                    "descricao": "Não foi possível encontrar a requisição",
                    "status": 'Não encontrado'
                },
                500: {
                    "descricao": "O servidor encontrou condição inesperada que impediu a requisição de ser completada",
                    "status": 'Erro interno do servidor'
                },
                503: {
                    "descricao": "O servidor esta indisponível para lidar com a requisição devido uma sobre carga temporaria ou manutenção.",
                    "status": 'Serviço indisponível'
                }
            }
        }
    },
    "rotas": {
        "/api/produtos": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de produtos.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{**produto_min, **categoria}],
                    "descricao": "Lista de produtos simplificados"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo produto dentro do banco de dados.",
                "pacote": [f'{param}: {type(produto[param]).__name__}' if not param == 'produtoid' else None for param in produto.keys()],
                "retorno": {
                    "code": 201,
                    "exemplo": {**produto_id, **produto, **categoria},
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            }
        },
        "/api/produtos/id": {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único produto.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {**produto_id, **produto, **categoria},
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um produto dentro do banco de dados.",
                "pacote": 'parametros',
                "retorno": {
                    "code": 200,
                    "exemplo": {**produto_id, **produto, **categoria},
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            },
            "DELETE": {
                "descricao": "Este objeto permite realizar a deleção de um produto específico dentro do banco de dados.",
                "pacote": None,
                "retorno": {
                    "code": 204,
                    "exemplo": None,
                    "descricao": "Esta requisição não retornará conteúdo pois o objeto foi deletado com sucesso."
                }
            }
        },
        "/api/clientes": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de clientes.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [cliente_min],
                    "descricao": "Esta requisição retornará apenas as informações principais como ID, nome e e-mail."
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo cliente dentro do banco de dados.",
                "pacote": 'parametros',
                "retorno": {
                    "code": 201,
                    "exemplo": {**cliente_id, **cliente},
                    "descricao": "Caracteristicas de clientes consolidadas."
                }
            }
        },
        "/api/clientes/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único cliente.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {**cliente_id, **cliente},
                    "descricao": "Caracteristicas do cliente consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um cliente do banco de dados.",
                "pacote": {
                    "code": 200,
                    "exemplo": 'parametros opicionais'
                },
                "retorno": {
                    "code": 200,
                    "exemplo": {**cliente_id, **cliente},
                    "descricao": "Caracteristicas do cliente consolidadas."
                }
            },
            "DELETE": {
                "descricao": "Este objeto permite realizar a deleção de um cliente específico dentro do banco de dados.",
                "pacote": None,
                "retorno": {
                    "code": 204,
                    "exemplo": None,
                    "descricao": "Esta requisição não retornará conteúdo pois o objeto foi deletado com sucesso."
                }
            }
        },
        "/api/vendas": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de vendas.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{**venda}],
                    "descricao": "Lista de vendas"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um nova venda dentro do banco de dados.",
                "pacote": 'parametros',
                "retorno": {
                    "code": 201,
                    "exemplo": venda,
                    "descricao": "Caracteristicas da venda consolidada."
                }
            }
        },
        "/api/vendas/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único venda.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": venda,
                    "descricao": "Caracteristicas do venda consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de uma venda dentro do banco de dados.",
                "pacote": {
                      'idVendedor': 1,
                      'idCliente': 57
                    },
                "retorno": {
                    "code": 200,
                    "exemplo": venda,
                    "descricao": "Caracteristicas da venda consolidada."
                }
            },
            "DELETE": {
                "descricao": "Este objeto permite realizar a deleção de um venda específico dentro do banco de dados.",
                "pacote": None,
                "retorno": {
                    "code": 204,
                    "exemplo": None,
                    "descricao": "Esta requisição não retornará conteúdo pois o objeto foi deletado com sucesso."
                }
            }
        },
        "/api/vendedores": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de vendedores.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{**vendedor, **vendedor_id}],
                    "descricao": "Lista de vendedores"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo vendedor dentro do banco de dados.",
                "pacote": 'parametros',
                "retorno": {
                    "code": 201,
                    "exemplo": {**vendedor, **vendedor_id},
                    "descricao": "Caracteristicas da vendedor consolidadas."
                }
            }
        },
        "/api/vendedores/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar uma lista de vendedores.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {**vendedor, **vendedor_id},
                    "descricao": "Caracteristicas dos vendedores consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um vendedor dentro do banco de dados.",
                "pacote": 'parametros',
                "retorno": {
                    "code": 200,
                    "exemplo": {**vendedor, **vendedor_id},
                    "descricao": "Caracteristicas do vendedor consolidada."
                }
            },
            "DELETE": {
                "descricao": "Este objeto permite realizar a deleção de um vendedor específico dentro do banco de dados.",
                "pacote": None,
                "retorno": {
                    "code": 204,
                    "exemplo": None,
                    "descricao": "Esta requisição não retornará conteúdo pois o objeto foi deletado com sucesso."
                }
            }
        }
    }
}
