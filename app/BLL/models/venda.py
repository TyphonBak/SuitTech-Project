class Venda():
    def __init__(self, id, idVendedor, idCliente):
        self.id = id
        self.idVendedor = idVendedor
        self.idCliente = idCliente

        
    def __dict__(self):
        dados = dict()
        dados['id'] = self.id
        dados['idVendedor'] = self.idVendedor 
        dados['idCliente'] = self.idCliente 
        return dados
    
    def atualizar(self, dados):
        try:
            idVendedor = dados["idVendedor"]
            self.idVendedor = idVendedor 
            idCliente = dados['idCliente'] 
            self.idCliente = idCliente
            return self, None
        except Exception as e:
            print("deu ruim")

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            idVendedor = dados["idVendedor"] 
            idCliente = dados['idCliente'] 
            return Venda(id=id, idVendedor=idVendedor, idCliente=idCliente), None
        except Exception as e:
            print("deu ruim")
