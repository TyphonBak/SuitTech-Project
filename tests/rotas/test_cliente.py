import pytest
from tests.helper import client
#importar Cliente

class TestCliente:

    #GET    
    def test_deve_retornar_200_e_lista_de_clientes(self, client):
        
        retorno = client.get('/clientes')

        assert retorno.status_code == 200
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_cliente_em_dict_quando_passado_id_valido(self, client):

        retorno = client.get('/clientes/1')

        #Aguardando implementação do banco e modelos \/ \/ \/

        #assert retorno.status_code == 200
        #assert retorno.json.keys()==Cliente.__dict__().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/clientes/999999")

        assert retorno.status_code == 404

    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        #cliente = Cliente.cria(dados)
        #retorno = client.post("/clientes", json=cliente)

        #assert 201 == retorno.status_code
        #assert Cliente.__dict__().keys() in retorno.json.keys()
        #assert "id" in retorno.json.keys()
        pass
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        #cliente = { "nome": "cliente", "idade": 28 }
        #cliente2 = { 'colocar aqui um cliente com tipo de atributo incorreto' }
        #retorno = client.post("/clientes", json=cliente)
        #retorno2 = client.post("/clientes", json=cliente2)

        #assert 400 == retorno.status_code
        #assert 400 == retorno2.status_code
        #assert 'errors' in retorno.json
        #assert 'errors' in retorno2.json
        pass

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        #cliente = Cliente.cria(dados)
        #cliente_criado = client.post("/clientes", json=cliente)
        #retorno = client.delete(f"/clientes/{cliente_criado.id}")

        #assert 204 == retorno.status_code
        pass

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        #retorno = client.delete("/clientes/999999999")

        #assert 404 == retorno.status_code
        pass

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        #cliente = Cliente.cria()
        #cliente_criado = client.post("/clientes")
        #valores_a_alterar = {}
        #retorno = client.put(f"/clientes/{cliente_criado.id}", valores_a_alterar)

        #assert 200 == retorno.status_code
        #assert cliente_criado.keys() in retorno.json
        pass

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        #cliente = Cliente.cria()
        #cliente_criado = client.post("/clientes")
        #valores_a_alterar = {}
        #retorno = client.put(f"/clientes/{cliente_criado.id}", valores_a_alterar)

        #assert 400 == retorno.status_code
        #assert 'errors' in retorno.json
        pass

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        #retorno = client.put("/clientes/999999999", json={})

        #assert 404 == retorno.status_code
        pass