import requests as req

def criaCliente(nome: str, cpf: str, email: str, logradouro: str, cep: str, numero:str , cidade: str, uf: str, telefone: str):
    return {
        'nome': nome,
        'cpf_cnpj': cpf_cnpj,
        'email': email,
        'logradouro': logradouro,
        'cep': cep,
        'numero': numero,
        'cidade': cidade,
        'uf': uf,
        'telefone': telefone
    }

def criaProduto(categoriaid: int, nome: str, imagens: list, peso: float, altura: float, largura: float, cor: str, material: str, precocusto: float, precovendavarejo: float, precovendaatacado: float, imposto: float, estoque: int, descricao: str):
    """
    Categoriaid deve ser um numero de id já cadastrado
    Imagens deve ser uma lista de nomes de imagem na pasta de produtos
    """
    return {
        "categoriaid": categoriaid,
        "nome": nome,
        "imagens": imagens,
        "peso": peso,
        "altura": altura,
        "largura": largura,
        "cor": cor,
        "material": material,
        "precocusto": precocusto,
        "precovendavarejo": precovendavarejo,
        "precovendaatacado": precovendaatacado,
        "imposto": imposto,
        "estoque": estoque,
        "descricao": descricao
    }

def criaVenda(vendedorid: int, clienteid: int, produtos: list):    
    """
    /vendas
    Produtos deve ser uma lista de dicionario com "produtoid" (id já cadastrado) e "quantidade" (inteiro)
    """
    return {
        "vendedorid": vendedorid,
        "clienteid": clienteid,
        "produtos": produtos
    }

# Sessão de Preparação
categorias = ["Acessório", "Casa", "Decoração", "Papel & Cia", "Outros"]

produtos = [
    [2,'Toalha de Rosto',[],0.17,0.82,0.50,'Diversos','Algodão',10.00,23.00,25.00,0.00,6,'Toalha de rosto com pintura personalizada.'],
    [2,'Tapete Emborrachado',[],0.28,0.45,0.67,'Diversos','Borracha',12.00,27.00,30.00,0.00,1,'Tapete de borracha pintado e com crochê.'],
    [2,'Jogo Banheiro 3 Pçs',[],0.66,0.45,0.67,'Diversos','Borracha',36.00,81.00,90.00,0.00,1,'Inclui 2 tapetes (um para vaso sanitário e um para saida do box) e uma capa para tampa do assento. Todos pintados e com crochê'],
    [2,'Pano de Prato',[],0.07,0.78,0.40,'Branco','Algodão',6.00,16.00,18.00,0.00,4,'Pano de prato com desenho temático e personalizado.'],
    [2,'Bate mão',[],0.05,0.55,0.35,'Branco','Algodão',7.00,16.00,18.00,0.00,4,'Bate mão com bordado personalizado.'],
    [1,'Touca de cozinha',[],0.02,0.18,0.26,'Diversos','Algodão',5.00,18.00,25.00,0.00,2,'Touca personalizada utilizada em cozinha, hospitais, etc.'],
    [2,'Avental porta pregador',[],0.05,0.34,0.30,'Diversos','Algodão',5.00,18.00,20.00,0.00,1,'Avental porta pregador personalizado.'],
    [1,'Necessaire higienica',[],0.05,0.50,0.29,'Diversos','Algodão',5.00,18.00,20.00,0.00,3,'Necessaire personalizada usada para portar pasta, escova e etc.'],
    [2,'Toalha Lavabo',[],0.06,0.46,0.31,'Diversos','Algodão',6.40,14.00,15.00,0.00,5,'Toalha de lavabo com pintura personalizada.'],
    [1,'Avental Escolar',[],0.13,0.75,0.58,'Diversos','Poliester',9.00,36.00,40.00,0.00,3,'Avental para professora com pintura personalizada.'],
    [3,'Caixa decorada',[],0.28,0.21,0.16,'Diversos','MDF',6.00,18.00,20.00,0.00,2,'Caixa com decoração personalizada.'],
    [1,'Necessaire (caixa)',[],0.11,0.18,0.14,'Diversos','Plástico',5.00,14.00,15.00,0.00,1,'Necessaire feita com caixa de sorvete com decoração personalizada.'],
    [2,'Tapete em Crochê',[],0.59,0.76,0.60,'Diversos','Algodão',10.00,27.00,30.00,0.00,2,'Tapete em crochê.'],
    [2,'Jogo de banheiro (2 Pçs)',[],0.68,0.57,0.50,'Diversos','Algodão',10.00,63.00,70.00,0.00,2,'Jogo de banheiro com 2 peças.'],
    [4,'Agenda Decorada',[],0.24,0.21,0.15,'Diversos','Papel',6.00,14.00,15.00,0.00,7,'Agenda decorada com tecido.'],
    [4,'Agenda Vovó',[],0.26,0.21,0.15,'Diversos','Papel',12.00,23.00,25.00,0.00,2,'Agenda decorada com tecido e boneca de vovó.'],
    [2,'Puxa saco',[],0.07,0.46,0.29,'Diversos','Poliester',16.00,27.00,30.00,0.00,3,"Puxa saco com decoração de galinha d'angola."],
    [2,"Toalha de Banho",[],0.39,1.60,0.82,"Diversos","Algodão",21,50,55,0,6,"Toalha de banho decorada"],
    [2,"Fralda Decorada",[],0.58,0.70,0.70,"Branco","Algodão",10,16,18,0,2,"Fralda personalizada à pintura"],
    [2,"Porta guardanapo",[],0.25,0.18,0.18,"Diversos",'MDF',6,18,20,0,1,"Porta guardanapo decorado"]
]
print(len(produtos))
"""
# Sessão das Requisições
baseUrlHeroku = 'https://titarte.herokuapp.com/api'
baseUrlLocal = 'http://localhost:5000/api'
baseUrl = baseUrlHeroku
categoriasids = [cat['categoriaid'] for cat in req.get(f'{baseUrl}/categorias').json()]

print(categoriasids)
"""