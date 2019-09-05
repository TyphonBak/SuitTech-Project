class Pedido():
    def __init__(self, id, itensPedido):
        self.id = id
        self.itensPedido = itensPedido

    
    def atualizar(self, dados):
        try:
            itensPedido = dados["itensPedido"]
            self.itensPedido = itensPedido 
            return self, None
        except Exception as e:
            None, e

    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['itensPedido'] = self.itensPedido 
        return dados    

    @staticmethod
    def cria(dados):
        try:
            itensPedido = dados["itensPedido"]  
            return Pedido(id=None, itensPedido=itensPedido), None
        except Exception as e:
            None, e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            itensPedido = dados[1]
            return Pedido(id=id, itensPedido=itensPedido), None
        except Exception as e:
            None, e