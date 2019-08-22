from flask import Flask

from .extensions import db
from .VIEWS.cliente import bp_cliente
from .VIEWS.produto import bp_produto
from .VIEWS.venda import bp_venda

def create_app(config_file='settings.py'):

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_venda)

    return app
