import pytest
from app.extensions import db
from tests.helper import client, copia_sem_sa_instance
from tests.factory_class import ProdutoFactory

class TestProduto:
    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        produto = ProdutoFactory.build()
        retorno = client.post("/api/produtos", json=copia_sem_sa_instance(produto.__dict__))

        assert 201 == retorno.status_code
        assert set(copia_sem_sa_instance(produto.__dict__).keys()) and set(retorno.json.keys())
        assert "produtoid" in retorno.json.keys()
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        produto = ProdutoFactory.build()
        produto.peso = 'Um Quilo'
        
        retorno = client.post("/api/produtos", json=copia_sem_sa_instance(produto.__dict__))

        assert 400 == retorno.status_code
        assert 'Um Quilo' in retorno.json

    #GET    
    def test_deve_retornar_200_e_lista_de_produtos(self, client):
        
        retorno = client.get('/api/produtos')

        assert retorno.status_code == 200
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_produto_em_dict_quando_passado_id_valido(self, client):

        produto = ProdutoFactory.build()
        client.post('/api/produtos', json=copia_sem_sa_instance(produto.__dict__))

        retorno = client.get('/api/produtos/1')

        assert retorno.status_code == 200
        assert produto.serialize().keys() == retorno.json.keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/api/produtos/99999")

        assert retorno.status_code == 404

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        produto = ProdutoFactory.build()
        produto_criado = client.post("/api/produtos", json=copia_sem_sa_instance(produto.__dict__)).json
        valores_a_alterar = ProdutoFactory.build()
        retorno = client.put(f"/api/produtos/{produto_criado.get('produtoid')}", json=copia_sem_sa_instance(valores_a_alterar.__dict__))

        assert 200 == retorno.status_code
        assert produto_criado.keys() == retorno.json.keys()

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        produto = ProdutoFactory.build()
        produto_criado = client.post("/api/produtos", json=copia_sem_sa_instance(produto.__dict__)).json
        valores_a_alterar = ProdutoFactory.build()
        valores_a_alterar.peso = 'Um quilo'
        retorno = client.put(f"/api/produtos/{produto_criado.get('produtoid')}", json=copia_sem_sa_instance(valores_a_alterar.__dict__))

        assert 400 == retorno.status_code
        assert 'Um quilo' in retorno.json

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/api/produtos/999999999", json={'dummy': 'dummy'})

        assert 404 == retorno.status_code

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        produto = ProdutoFactory.build()
        produto_criado = client.post("/api/produtos", json=copia_sem_sa_instance(produto.__dict__)).json
        retorno = client.delete(f"/api/produtos/{produto_criado.get('produtoid')}")

        assert 204 == retorno.status_code

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/api/produtos/999999999")

        assert 404 == retorno.status_code
