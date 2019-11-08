from flask import Flask, jsonify
from flask_cors import CORS

from .extensions import db
from .VIEWS.cliente import bp_cliente
from .VIEWS.produto import bp_produto
from .VIEWS.venda import bp_venda
from .VIEWS.vendedor import bp_vendedor
from .VIEWS.categoria import bp_categoria
from .VIEWS.documentacao import bp_doc

def create_app(config_file='settings.py'):

    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile(config_file)
    app.config['JSON_AS_ASCII'] = False

    db.init_app(app)
    db.app = app

    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_venda)
    app.register_blueprint(bp_vendedor)
    app.register_blueprint(bp_categoria)
    app.register_blueprint(bp_doc)

    return app
