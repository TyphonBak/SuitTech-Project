import pytest
from tests.helper import client
from tests.factory_class import ClienteFactory
#importar Cliente

class TestCliente:
    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        cliente = ClienteFactory.build()
        retorno = client.post("/clientes", json=cliente.serialize())

        assert 201 == retorno.status_code
        assert [cliente.serialize().keys()]
        assert set(cliente.serialize().keys()) and set(retorno.json.keys())
        assert "clienteid" in retorno.json.keys()
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        cliente2 = ClienteFactory.build()
        cliente2.numero = 'Dois'
        retorno2 = client.post("/clientes", json=cliente2.serialize())

        assert 400 == retorno2.status_code
        assert 'error' in retorno2.json

    #GET    
    def test_deve_retornar_200_e_lista_de_clientes(self, client):
        
        retorno = client.get('/clientes')

        assert retorno.status_code == 200
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_cliente_em_dict_quando_passado_id_valido(self, client):

        cliente = ClienteFactory.build()
        client.post('/clientes', json=cliente.serialize())

        retorno = client.get('/clientes/1')

        assert retorno.status_code == 200
        assert retorno.json.keys()==cliente.serialize().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/clientes/999999")

        assert retorno.status_code == 404

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        cliente = ClienteFactory.build()
        cliente_criado = client.post("/clientes", json=cliente.serialize())
        cliente.nome = 'João'
        retorno = client.put(f"/clientes/{cliente_criado.json['clienteid']}", json=cliente.serialize())

        assert 200 == retorno.status_code
        assert cliente_criado.json.keys() == retorno.json.keys()
        assert cliente.nome == retorno.json.get('nome')

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        cliente = ClienteFactory.build()
        cliente_criado = client.post("/clientes", json=cliente.serialize())
        valores_a_alterar = {'name': 'Paulo', 'age': '27'}
        retorno = client.put(f"/clientes/{cliente_criado.json.get('clienteid')}", json=valores_a_alterar)

        assert 400 == retorno.status_code
        #assert 'error' in retorno.json

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/clientes/999999999", json={})

        assert 404 == retorno.status_code

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        cliente = ClienteFactory.build()
        cliente_criado = client.post("/clientes", json=cliente.serialize())
        retorno = client.delete(f"/clientes/{cliente_criado.json['clienteid']}")

        assert 204 == retorno.status_code

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/clientes/999999999")

        assert 404 == retorno.status_code
        assert 'Referencia' in retorno.json
