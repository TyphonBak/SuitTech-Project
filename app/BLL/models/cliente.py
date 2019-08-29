class Cliente():
    def __init__(self, nome, cpf, email, logradouro, cep, numero, cidade, estado, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.logradouro = logradouro
        self.cep = cep  
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

        
    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['nome'] = self.nome
        dados['cpf'] = self.cpf 
        dados['email'] = self.email 
        dados['logradouro'] = self.logradouro 
        dados['cep'] = self.cep
        dados['numero'] = self.numero 
        dados['cidade'] = self.cidade 
        dados['estado'] = self.estado
        return dados
    
    def atualizar(self, dados):
        try:
            nome = dados["nome"]
            self.nome = nome 
            cpf = dados['cpf'] 
            self.cpf = cpf
            email = dados['email'] 
            self.email = email
            logradouro = dados['logradouro']
            self.logradouro = logradouro
            cep = dados['cep']
            self.cep = cep
            numero = dados['numero']
            self.numero = numero
            cidade = dados['cidade']
            self.cidade = cidade
            estado = dados['estado']
            self.estado = estado
            return self, None
        except Exception as e:
            print("deu ruim")

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"] 
            cpf = dados['cpf'] 
            email = dados['email'] 
            logradouro = dados['logradouro']
            cep = dados['cep']
            numero = dados['numero']
            cidade = dados['cidade']
            estado = dados['estado']
            return Cliente(id=id, nome=nome, cpf=cpf, email=email, logradouro=logradouro, cep=cep, numero=numero, cidade=cidade, estado=estado)
        except Exception as e:
            return e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1] 
            cpf = dados[2] 
            email = dados[3] 
            logradouro = dados[4]
            cep = dados[5]
            numero = dados[6]
            cidade = dados[7]
            estado = dados[8]
            return Cliente(id=id, nome=nome, cpf=cpf, email=email, logradouro=logradouro, cep=cep, numero=numero, cidade=cidade, estado=estado)
        except Exception as e:
            return None
