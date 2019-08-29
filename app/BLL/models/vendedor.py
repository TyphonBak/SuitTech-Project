class Vendedor():
    def __init__(self, id, cpf, email):
        self.id = id
        self.cpf = cpf
        self.email = email

        
    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['cpf'] = self.cpf 
        dados['email'] = self.email 
        return dados
    
    def atualizar(self, dados):
        try:
            cpf = dados["cpf"]
            self.cpf = cpf 
            email = dados['email'] 
            self.email = email
            return self, None
        except Exception as e:
            print("deu ruim")

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            cpf = dados["cpf"] 
            email = dados['email'] 
            return Vendedor(id=id, cpf=cpf, email=email), None
        except Exception as e:
            print("deu ruim")

