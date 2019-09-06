doc= {
    "url base": "api-titarte.herokuapp.com/",
    "topicos": {
        "Referencia API": "A API SuitTech esta organizada em REST. a API possui URLs orientada a recursos, \
        aceitando solicitaÃ§Ãµes via JSON com o protocolo HTTP padrÃ£o, retornando respostas codificadas em JSON.",
        "Autenticação": "Atualmente a API Ã© exclusiva para uso interno, desta forma a \
        autenticaÃ§Ã£o para terceiros foi esta desabilitada.",
        "Respostas da API": {
            "descricao": "Utilizamos as respostas do protocolo HTTP para indicar requisiÃ§Ãµes com falhas ou sucesso \
                da nossa API. No geral os cÃ³digos que contÃ©m o range de -2xx- indicam que a requisiÃ§Ã£o foi feita com \
                sucesso. JÃ¡ os de range -4xx- e -5xx- indicam um erro.",
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
        "/produtos": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de produtos.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{
                      'id': '245',
                      'categoria': 'Caixa MDF',
                      'nome': 'Caixa Decorada Blevers',
                      'img_url': 'imgur.com/imglink'
                    }],
                    "descricao": "Lista de produtos simplificados"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo produto dentro do banco de dados.",
                "pacote": {
                      'categoria': 'Caixa MDF',
                      'nome': 'Caixa Decorada Blevers',
                      'peso': 1.05,
                      'altura': 0.20,
                      'largura': 0.60,
                      'cor_predominante': 'Laranja',
                      'material': 'Madeira',
                      'precoCusto': 12.00,
                      'precoVendaVarejo': 25.00,
                      'precoVendaAtacado': 22.00,
                      'impostos': 5,
                      'estoque': 5,
                      'descricao': 'Caixa de mdf decorada a mão.' 
                    },
                "retorno": {
                    "code": 201,
                    "exemplo": {},
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            }
        },
        "/produtos/id": {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único produto.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {
                        'id': 123,
                        'categoria': 'Caixa MDF',
                        'nome': 'Caixa Decorada Blevers',
                        'peso': 1.05,
                        'altura': 0.20,
                        'largura': 0.60,
                        'cor_predominante': 'Laranja',
                        'material': 'Madeira',
                        'precoCusto': 12.00,
                        'precoVendaVarejo': 25.00,
                        'precoVendaAtacado': 22.00,
                        'impostos': 5,
                        'estoque': 5,
                        'descricao': 'Caixa de mdf decorada a mão.' 
                    },
                    "descricao": "Caracteristicas do produto consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um produto dentro do banco de dados.",
                "pacote": {
                    'categoria': 'Caixa MDF',
                    'nome': 'Caixa Decorada Blevers',
                    'peso': 1.05,
                    'altura': 0.20,
                    'largura': 0.60,
                    'cor_predominante': 'Laranja',
                    'material': 'Madeira',
                    'precoCusto': 12.00,
                    'precoVendaVarejo': 25.00,
                    'precoVendaAtacado': 22.00,
                    'impostos': 5,
                    'estoque': 5,
                    'descricao': 'Caixa de mdf decorada a mão.' 
                },
                "retorno": {
                    "code": 200,
                    "exemplo": {
                      'id': 123,
                      'categoria': 'Caixa MDF',
                      'nome': 'Caixa Decorada Blevers',
                      'peso': 1.05,
                      'altura': 0.20,
                      'largura': 0.60,
                      'cor_predominante': 'Laranja',
                      'material': 'Madeira',
                      'precoCusto': 12.00,
                      'precoVendaVarejo': 25.00,
                      'precoVendaAtacado': 22.00,
                      'impostos': 5,
                      'estoque': 5,
                      'descricao': 'Caixa de mdf decorada a mão.' 
                    },
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
        "/clientes": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de clientes.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{
                      'id': 23,
                      'nome': 'Fernando Napoli',
                      'email': 'fernando@email.com'
                    }],
                    "descricao": "Esta requisição retornará apenas as informações principais como ID, nome e e-mail."
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo cliente dentro do banco de dados.",
                "pacote": {
                      'nome': 'Fernando Napoli',
                      'cpf': '12345678912',
                      'email': 'fernando@email.com',
                      'logradouro': 'Rua Ontem não é hoje',
                      'cep': '01234678',
                      'numero': '123',
                      'cidade': 'São Paulo',
                      'estado': 'São Paulo'
                    },
                "retorno": {
                    "code": 201,
                    "exemplo": {
                      'id': 23,
                      'nome': 'Fernando Napoli',
                      'cpf': '12345678912',
                      'email': 'fernando@email.com',
                      'logradouro': 'Rua Ontem não é hoje',
                      'cep': '01234678',
                      'numero': '123',
                      'cidade': 'São Paulo',
                      'estado': 'São Paulo'
                    },
                    "descricao": "Caracteristicas de clientes consolidadas."
                }
            }
        },
        "/clientes/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único cliente.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {
                        'id': 23,
                        'nome': 'Fernando Napoli',
                        'cpf': '12345678912',
                        'email': 'fernando@email.com',
                        'logradouro': 'Rua Ontem não é hoje',
                        'cep': '01234678',
                        'numero': '123',
                        'cidade': 'São Paulo',
                        'estado': 'São Paulo'
                    },
                    "descricao": "Caracteristicas do cliente consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um cliente do banco de dados.",
                "pacote": {
                    "code": 200,
                    "exemplo": {
                        'nome': 'Fernando Napoli',
                        'cpf': '12345678912',
                        'email': 'fernando@email.com',
                        'logradouro': 'Rua Ontem não é hoje',
                        'cep': '01234678',
                        'numero': '123',
                        'cidade': 'São Paulo',
                        'estado': 'São Paulo'
                    }
                },
                "retorno": {
                    "code": 200,
                    "exemplo": {
                        'id': 23,
                        'nome': 'Fernando Napoli',
                        'cpf': '12345678912',
                        'email': 'fernando@email.com',
                        'logradouro': 'Rua Ontem não é hoje',
                        'cep': '01234678',
                        'numero': '123',
                        'cidade': 'São Paulo',
                        'estado': 'São Paulo'
                    },
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
        "/vendas": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de vendas.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{
                      'id': 24,
                      'idVendedor': 1,
                      'idCliente': 57
                    }],
                    "descricao": "Lista de vendas"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um nova venda dentro do banco de dados.",
                "pacote": {
                      'idVendedor': 1,
                      'idCliente': 57
                    },
                "retorno": {
                    "code": 201,
                    "exemplo": {
                      'id': 24,
                      'idVendedor': 1,
                      'idCliente': 57
                    },
                    "descricao": "Caracteristicas da venda consolidada."
                }
            }
        },
        "/vendas/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar um único venda.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {
                      'id': 24,
                      'idVendedor': 1,
                      'idCliente': 57
                    },
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
                    "exemplo": {
                      'id': 24,
                      'idVendedor': 1,
                      'idCliente': 57
                    },
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
        "/vendedores": {
            "GET": {
                "descricao": "Este objeto permite executar uma requisição para consultar uma lista de vendedores.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": [{
                      'id': 3,
                      'nome': 'Napoli Fernando',
                      'cpf': '12345678912',
                      'email': 'napoli@email.com'
                    }],
                    "descricao": "Lista de vendedores"
                }
            },
            "POST": {
                "descricao": "Este objeto permite criar um novo vendedor dentro do banco de dados.",
                "pacote": {
                      'nome': 'Napoli Fernando',
                      'cpf': '12345678912',
                      'email': 'napoli@email.com'
                    },
                "retorno": {
                    "code": 201,
                    "exemplo": {
                      'id': 3,
                      'nome': 'Napoli Fernando',
                      'cpf': '12345678912',
                      'email': 'napoli@email.com'
                    },
                    "descricao": "Caracteristicas da vendedor consolidadas."
                }
            }
        },
        "/vendedores/id" : {
            "GET": {
                "descricao": "Este Objeto permite executar uma requisição para consultar uma lista de vendedores.",
                "pacote": None,
                "retorno": {
                    "code": 200,
                    "exemplo": {
                      'id': 3,
                      'nome': 'Napoli Fernando',
                      'cpf': '12345678912',
                      'email': 'napoli@email.com'
                    },
                    "descricao": "Caracteristicas dos vendedores consolidadas."
                }
            },
            "PUT": {
                "descricao": "Este objeto permite realizar alterações de um vendedor dentro do banco de dados.",
                "pacote": {
                    'nome': 'Napoli Fernando',
                    'cpf': '12345678912',
                    'email': 'napoli@email.com'
                },
                "retorno": {
                    "code": 200,
                    "exemplo": {
                      'id': 3,
                      'nome': 'Napoli Fernando',
                      'cpf': '12345678912',
                      'email': 'napoli@email.com'
                    },
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
