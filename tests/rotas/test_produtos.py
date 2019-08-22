import pytest
from tests.helper import client
#importar Produto

class TestProduto:

    #GET    
    def test_deve_retornar_200_e_lista_de_produtos(self, client):
        
        retorno = client.get('/produtos')

        assert retorno.status_code == 200
        assert isinstance(retorno.json, list)

    def test_deve_retornar_um_produto_em_dict_quando_passado_id_valido(self, client):

        retorno = client.get('/produtos/1')

        #Aguardando implementação do banco e modelos \/ \/ \/

        #assert retorno.status_code == 200
        #assert retorno.json.keys()==Produto.__dict__().keys()

    def test_deve_retornar_404_quando_for_buscado_um_id_inexistente(self, client):
        
        retorno = client.get("/produtos/99999")

        assert retorno.status_code == 404

    #POST
    def test_deve_retornar_201_e_objeto_criado_com_id_quando_usado_metodo_post_com_playload_correto(self, client):

        #produto = Produto.cria(dados)
        #retorno = client.post("/produtos", json=produto)

        #assert 201 == retorno.status_code
        #assert produto.__dict__().keys() in retorno.json.keys()
        #assert "id" in retorno.json.keys()
        pass
    
    def test_deve_retornar_400_quando_usado_metodo_post_com_payload_incorreto(self, client):

        #produto = { "nome": "Produto", "idade": 28 }
        #produto2 = { 'colocar aqui um produto com tipo de atributo incorreto' }
        #retorno = client.post("/produtos", json=produto)
        #retorno2 = client.post("/produtos", json=produto2)

        #assert 400 == retorno.status_code
        #assert 400 == retorno2.status_code
        #assert 'errors' in retorno.json
        #assert 'errors' in retorno2.json
        pass

    #DELETE
    def test_deve_retornar_204_quando_objeto_deletado_com_sucesso(self, client):

        #produto = Produto.cria(dados)
        #produto_criado = client.post("/produtos", json=produto)
        #retorno = client.delete(f"/produtos/{produto_criado.id}")

        #assert 204 == retorno.status_code
        pass

    def test_deve_retornar_404_quando_id_deletado_nao_existir(self, client):

        retorno = client.delete("/produtos/999999999")

        assert 404 == retorno.status_code

    #UPDATE - PUT
    def test_deve_retornar_200_e_objeto_alterado_quando_alterado_com_sucesso(self, client):

        #produto = Produto.cria()
        #produto_criado = client.post("/produtos")
        #valores_a_alterar = {}
        #retorno = client.put(f"/produtos/{produto_criado.id}", valores_a_alterar)

        #assert 200 == retorno.status_code
        #assert produto_criado.keys() in retorno.json
        pass

    def test_deve_retornar_400_quando_tipos_invalidos_forem_enviados(self, client):

        #produto = Produto.cria()
        #produto_criado = client.post("/produtos")
        #valores_a_alterar = {}
        #retorno = client.put(f"/produtos/{produto_criado.id}", valores_a_alterar)

        #assert 400 == retorno.status_code
        #assert 'errors' in retorno.json
        pass

    def test_deve_retornar_404_quando_id_a_alterar_nao_existir(self, client):

        retorno = client.put("/produtos/999999999", json={})

        assert 404 == retorno.status_code
