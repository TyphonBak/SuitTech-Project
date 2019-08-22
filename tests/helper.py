import pytest
from app import create_app
from wsgi import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    cliente_teste = app.test_client()
    return cliente_teste