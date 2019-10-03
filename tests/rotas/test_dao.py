from app.DAO.db_cliente import listar as listar_db

class TestClienteDao():

    def test_dao(cliente):
        retorno = listar_db()

        assert retorno == ''