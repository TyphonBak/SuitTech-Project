from tests.factory_class import ProdutoFactory, ClienteFactory, VendaFactory, VendedorFactory

produto_obj = ProdutoFactory.build()
produto_sample = produto_obj.serialize()
produto_sample_min = produto_obj.serialize_min()
produto_sample['produtoid'] = 1
produto_id = {'produtoid': produto_sample.pop('produtoid', None)}
cliente_obj = ClienteFactory.build()
cliente_sample = cliente_obj.serialize()
cliente_sample_min = cliente_obj.serialize_min()
cliente_sample['clienteid'] = 1
cliente_id = {'clienteid': cliente_sample.pop('clienteid', None)}
venda_sample = VendaFactory.build().serialize()
venda_sample['vendaid'] = 1
venda_id = {'vendaid': venda_sample.pop('vendaid', None)}
vendedor_sample = VendedorFactory.build().serialize()
vendedor_sample['vendedorid'] = 1
vendedor_id = {'vendedorid': vendedor_sample.pop('vendedorid', None)}

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
                    "exemplo": [{**produto_id, **produto_sample_min}],
                    "descricao": "Lista de produtos simplificados"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo produto dentro do banco de dados.",
                "pacote": produto_sample,
                "retorno": {
                    "code": 201,
                    "exemplo": {**produto_id, **produto_sample},
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
                    "exemplo": {**produto_id, **produto_sample},
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um produto dentro do banco de dados.",
                "pacote": produto_sample,
                "retorno": {
                    "code": 200,
                    "exemplo": {**produto_id, **produto_sample},
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
                    "exemplo": [{**cliente_id, **cliente_sample_min}],
                    "descricao": "Esta requisição retornará apenas as informações principais como ID, nome e e-mail."
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo cliente dentro do banco de dados.",
                "pacote": cliente_sample,
                "retorno": {
                    "code": 201,
                    "exemplo": {**cliente_id, **cliente_sample},
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
                    "exemplo": {**cliente_id, **cliente_sample},
                    "descricao": "Caracteristicas do cliente consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um cliente do banco de dados.",
                "pacote": {
                    "code": 200,
                    "exemplo": cliente_sample
                },
                "retorno": {
                    "code": 200,
                    "exemplo": {**cliente_id, **cliente_sample},
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
                    "exemplo": [{**venda_id, **venda_sample}],
                    "descricao": "Lista de vendas"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um nova venda dentro do banco de dados.",
                "pacote": venda_sample,
                "retorno": {
                    "code": 201,
                    "exemplo": {**venda_id, **venda_sample},
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
                    "exemplo": {**venda_id, **venda_sample},
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
                    "exemplo": {**venda_id, **venda_sample},
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
                    "exemplo": [{**vendedor_id, **vendedor_sample}],
                    "descricao": "Lista de vendedores"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo vendedor dentro do banco de dados.",
                "pacote": vendedor_sample,
                "retorno": {
                    "code": 201,
                    "exemplo": {**vendedor_id, **vendedor_sample},
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
                    "exemplo": {**vendedor_id, **vendedor_sample},
                    "descricao": "Caracteristicas dos vendedores consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um vendedor dentro do banco de dados.",
                "pacote": vendedor_sample,
                "retorno": {
                    "code": 200,
                    "exemplo": {**vendedor_id, **vendedor_sample},
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
