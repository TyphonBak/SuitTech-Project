class Pedido():
    def __init__(self, id, itensPedido, email):
        self.id = id
        self.itensPedido = itensPedido
        self.email = email

        
    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['itensPedido'] = self.itensPedido 
        dados['email'] = self.email 
        return dados
    
    def atualizar(self, dados):
        try:
            itensPedido = dados["itensPedido"]
            self.itensPedido = itensPedido 
            email = dados['email'] 
            self.email = email
            return self, None
        except Exception as e:
            print("deu ruim")

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            itensPedido = dados["itensPedido"] 
            email = dados['email'] 
            return Pedido(id=id, itensPedido=itensPedido, email=email), None
        except Exception as e:
            print("deu ruim")

