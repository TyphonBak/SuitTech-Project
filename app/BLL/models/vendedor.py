class Vendedor():
    def __init__(self, nome, cpf, email, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        
    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['nome'] = self.nome
        dados['cpf'] = self.cpf 
        dados['email'] = self.email 
        return dados
    
    def atualizar(self, dados):
        try:
            nome = dados['nome']
            self.nome = nome
            cpf = dados["cpf"]
            self.cpf = cpf 
            email = dados['email'] 
            self.email = email
            return self, None
        except Exception as e:
            None, e

    @staticmethod
    def cria(dados):
        try:
            nome = dados['nome']
            cpf = dados["cpf"]
            email = dados['email']
            return Vendedor(id=None, cpf=cpf, email=email), None
        except Exception as e:
            None, e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            cpf = dados[2]
            email = dados[3]
            return Vendedor(id=id, nome=nome, cpf=cpf, email=email), None
        except Exception as e:
            None, e