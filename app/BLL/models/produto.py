class Produto():
    def __init__(self, id, categoria, nome, peso, altura, largura, cor, material, precoCusto, precoVendaVarejo, precoVendaAtacado, impostos, estoque, descricao):
        self.id = id
        self.categoria = categoria
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.largura = largura  
        self.cor = cor
        self.material = material
        self.precoCusto = precoCusto
        self.precoVendaVarejo = precoVendaVarejo
        self.precoVendaAtacado = precoVendaAtacado
        self.impostos = impostos
        self.estoque = estoque
        self.descricao = descricao 
    
    def atualizar(self, dados):
        try:
            categoria = dados["categoria"]
            self.categoria = categoria 
            nome = dados['nome'] 
            self.nome = nome
            peso = dados['peso'] 
            self.peso = peso
            altura = dados['altura']
            self.altura = altura
            largura = dados['largura']
            self.largura = largura
            cor = dados['cor']
            self.cor = cor
            material = dados['material']
            self.material = material
            precoCusto = dados['precoCusto']
            self.precoCusto = precoCusto
            precoVendaVarejo = dados['precoVendaVarejo']
            self.precoVendaVarejo = precoVendaVarejo
            precoVendaAtacado = dados['precoVendaAtacado']
            self.precoVendaAtacado = precoVendaAtacado
            impostos = dados['impostos']
            self.impostos = impostos
            estoque = dados['estoque']
            self.estoque = estoque
            descricao = dados['descricao']
            self.descricao = descricao
            return self, None
        except Exception as e:
            None, e

    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['categoria'] = self.categoria
        dados['nome'] = self.nome 
        dados['peso'] = self.peso 
        dados['altura'] = self.altura 
        dados['largura'] = self.largura
        dados['cor'] = self.cor 
        dados['material'] = self.material 
        dados ['precoCusto'] = self.precoCusto
        dados['precoVendaVarejo'] = self.precoVendaVarejo
        dados ['precoVendaAtacado'] = self.precoVendaAtacado
        dados ['impostos'] = self.impostos 
        dados ['estoque'] = self.estoque
        dados ['descricao'] = self.descricao 
        return dados

    @staticmethod
    def cria(dados):
        try:
            categoria = dados["categoria"] 
            nome = dados['nome'] 
            peso = dados['peso'] 
            altura = dados['altura']
            largura = dados['largura']
            cor = dados['cor']
            material = dados['material']
            precoCusto = dados['precoCusto']
            precoVendaVarejo = dados['precoVendaVarejo']
            precoVendaAtacado = dados['precoVendaAtacado']
            impostos = dados['impostos']
            estoque = dados['estoque']
            descricao = dados['descricao']
            return Produto(id=None, categoria=categoria, nome=nome, peso=peso, altura=altura, largura=largura, cor=cor, material=material, precoCusto=precoCusto, precoVendaVarejo=precoVendaVarejo, precoVendaAtacado=precoVendaAtacado, impostos=impostos, estoque=estoque, descricao=descricao), None
        except Exception as e:
            None, e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            categoria = dados[0]
            nome = dados[1]
            peso = dados[2]
            altura = dados[3]
            largura = dados[4]
            cor = dados[5]
            material = dados[6]
            precoCusto = dados[7]
            precoVendaVarejo = dados[8]
            precoVendaAtacado = dados[9]
            impostos = dados[10]
            estoque = dados[11]
            descricao = dados[12]
            return Produto(id=id, categoria=categoria, nome=nome, peso=peso, altura=altura, largura=largura, cor=cor, material=material, precoCusto=precoCusto, precoVendaVarejo=precoVendaVarejo, precoVendaAtacado=precoVendaAtacado, impostos=impostos, estoque=estoque, descricao=descricao), None
        except Exception as e:
            None, e