import copy
import pytest
from os import environ
from app.extensions import db
from app import create_app

@pytest.fixture(autouse=True)
def client():
    app = create_app()

    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('TEST_URL')
    db.init_app(app)

    cliente_teste = app.test_client()
    db.create_all(app=app)

    ctx = app.app_context()
    ctx.push()
    
    yield cliente_teste

    db.drop_all()
    ctx.pop()

def copia_sem_sa_instance(dicionario):
    dici_copy = copy.deepcopy(dicionario)
    dici_copy.pop('_sa_instance_state', None)
    return dici_copy
