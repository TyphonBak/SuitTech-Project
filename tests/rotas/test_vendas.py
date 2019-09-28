import pytest
from tests.helper import client
from tests.factory_class import VendaFactory

class TestVenda:

    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        venda = VendaFactory.build()
        retorno = client.post("/vendas", json=venda.__dict__())

        assert 201 == retorno.status_code
        assert Venda.__dict__().keys() in retorno.json.keys()
        assert "id" in retorno.json.keys()
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        venda = VendaFactory.build()
        venda2 = VendaFactory.build()
        venda2.idVendedor = 'Sete'

        retorno = client.post("/vendas", json=venda.__dict__())
        retorno2 = client.post("/vendas", json=venda2.__dict__())

        assert 400 == retorno.status_code
        assert 400 == retorno2.status_code
        assert 'errors' in retorno.json
        assert 'errors' in retorno2.json

    #GET
    def test_deve_retornar_200_e_lista_de_vendas(self, client):
        
        retorno = client.get('/vendas')

        assert 200 == retorno.status_code
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_venda_em_dict_quando_passado_id_valido(self, client):

        venda = VendaFactory.build()
        
        client.post('/vendas', json=venda.__dict__())
        retorno = client.get('/vendas/1')

        assert retorno.status_code == 200
        assert retorno.json.keys()==Venda.__dict__().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/vendas/99999")

        assert 404 == retorno.status_code

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        venda = VendaFactory.build()
        valores_a_alterar = VendaFactory.build()

        venda_criada = client.post("/vendas", json=venda.__dict__())
        retorno = client.put(f"/vendas/{venda_criada.id}", json=valores_a_alterar.__dict__())

        assert 200 == retorno.status_code
        assert venda_criada.keys() in retorno.json

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        venda = VendaFactory.build()
        valores_a_alterar = VendaFactory.build()
        valores_a_alterar.idVendedor = 'Sete'

        venda_criada = client.post("/vendas", json=venda.__dict__())
        retorno = client.put(f"/vendas/{venda_criada.id}", json=valores_a_alterar.__dict__())

        assert 400 == retorno.status_code
        assert 'errors' in retorno.json

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/vendas/999999999", json={})

        assert 404 == retorno.status_code

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        venda = VendaFactory.build()

        venda_criada = client.post("/vendas", json=venda)        
        retorno = client.delete(f"/vendas/{venda_criada.id}")

        assert 204 == retorno.status_code

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/vendas/999999999")

        assert 404 == retorno.status_code
