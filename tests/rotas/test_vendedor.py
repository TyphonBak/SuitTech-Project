import pytest
from tests.helper import client
from tests.factory_class import VendedorFactory

class TestVendedor:

    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        vendedor = VendedorFactory.build()
        retorno = client.post("/vendedor", json=vendedor.__dict__())

        assert 201 == retorno.status_code
        assert vendedor.__dict__().keys() in retorno.json.keys()
        assert "id" in retorno.json.keys()
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        vendedor = VendedorFactory.build()
        vendedor2 = VendedorFactory.build()
        vendedor2.idVendedor = 'Sete'

        retorno = client.post("/vendedor", json=vendedor.__dict__())
        retorno2 = client.post("/vendedor", json=vendedor2.__dict__())

        assert 400 == retorno.status_code
        assert 400 == retorno2.status_code
        assert 'errors' in retorno.json
        assert 'errors' in retorno2.json

    #GET
    def test_deve_retornar_200_e_lista_de_vendedor(self, client):
        
        retorno = client.get('/vendedor')

        assert 200 == retorno.status_code
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_vendedor_em_dict_quando_passado_id_valido(self, client):

        vendedor = VendedorFactory.build()
        
        client.post('/vendedor', json=vendedor.__dict__())
        retorno = client.get('/vendedor/1')

        assert retorno.status_code == 200
        assert retorno.json.keys()==vendedor.__dict__().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/vendedor/99999")

        assert 404 == retorno.status_code

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        vendedor = VendedorFactory.build()
        valores_a_alterar = VendedorFactory.build()

        vendedor_criada = client.post("/vendedor", json=vendedor.__dict__())
        retorno = client.put(f"/vendedor/{vendedor_criada.id}", json=valores_a_alterar.__dict__())

        assert 200 == retorno.status_code
        assert vendedor_criada.keys() in retorno.json

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        vendedor = VendedorFactory.build()
        valores_a_alterar = VendedorFactory.build()
        valores_a_alterar.idVendedor = 'Sete'

        vendedor_criada = client.post("/vendedor", json=vendedor.__dict__())
        retorno = client.put(f"/vendedor/{vendedor_criada.id}", json=valores_a_alterar.__dict__())

        assert 400 == retorno.status_code
        assert 'errors' in retorno.json

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/vendedor/999999999", json={})

        assert 404 == retorno.status_code

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        vendedor = VendedorFactory.build()

        vendedor_criada = client.post("/vendedor", json=vendedor)        
        retorno = client.delete(f"/vendedor/{vendedor_criada.id}")

        assert 204 == retorno.status_code

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/vendedor/999999999")

        assert 404 == retorno.status_code
