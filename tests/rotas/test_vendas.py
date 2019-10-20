import pytest
from tests.helper import client, copia_sem_sa_instance
from tests.factory_class import VendaFactory, ClienteFactory
from app.extensions import db

class TestVenda:

    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        venda = VendaFactory.build()
        retorno = client.post("/api/vendas", json=copia_sem_sa_instance(venda.__dict__))

        assert 201 == retorno.status_code
        assert set(venda.serialize().keys()) == set(retorno.json.keys())
        assert "vendaid" in retorno.json.keys()
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        venda2 = VendaFactory.build()
        venda2.clienteid = 'Sete'

        retorno2 = client.post("/api/vendas", json=copia_sem_sa_instance(venda2.__dict__))

        assert 400 == retorno2.status_code
        assert 'Sete' in retorno2.json

    #GET
    def test_deve_retornar_200_e_lista_de_vendas(self, client):
        
        retorno = client.get('/api/vendas')

        assert 200 == retorno.status_code
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_venda_em_dict_quando_passado_id_valido(self, client):

        venda = VendaFactory.build()
        venda.clienteid = 1
        db.session.add(ClienteFactory.build())
        db.session.commit()
        
        venda_criada = client.post('/api/vendas', json=copia_sem_sa_instance(venda.__dict__)).json
        retorno = client.get(f'/api/vendas/{venda_criada.get("vendaid")}')

        assert retorno.status_code == 200
        assert retorno.json.keys()==venda.serialize().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/api/vendas/99999")

        assert 404 == retorno.status_code

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        venda = VendaFactory.build()
        valores_a_alterar = VendaFactory.build()

        venda_criada = client.post("/api/vendas", json=copia_sem_sa_instance(venda.__dict__)).json
        retorno = client.put(f"/api/vendas/{venda_criada.get('vendaid')}", json=copia_sem_sa_instance(valores_a_alterar.__dict__))

        assert 200 == retorno.status_code
        assert venda_criada.keys() == retorno.json.keys()

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        venda = VendaFactory.build()
        valores_a_alterar = VendaFactory.build()
        valores_a_alterar.vendedorid = 'Sete'

        venda_criada = client.post("/api/vendas", json=copia_sem_sa_instance(venda.__dict__)).json
        retorno = client.put(f"/api/vendas/{venda_criada.get('vendaid')}", json=copia_sem_sa_instance(valores_a_alterar.__dict__))

        assert 400 == retorno.status_code
        assert 'Sete' in retorno.json

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/api/vendas/999999999", json={'none': 'none'})

        assert 404 == retorno.status_code

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        venda = VendaFactory.build()

        venda_criada = client.post("/api/vendas", json=copia_sem_sa_instance(venda.__dict__)).json
        retorno = client.delete(f"/api/vendas/{venda_criada.get('vendaid')}")

        assert 204 == retorno.status_code

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/api/vendas/999999999")

        assert 404 == retorno.status_code
