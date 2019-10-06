from flask import Flask

from .extensions import db
from flask_sqlalchemy import SQLAlchemy
from .VIEWS.cliente import bp_cliente
from .VIEWS.produto import bp_produto
from .VIEWS.venda import bp_venda
from .VIEWS.documentacao import bp_doc

def create_app(config_file='settings.py'):

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    db.app = app

    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_venda)
    app.register_blueprint(bp_doc)
    
    @app.errorhandler(TypeError)
    def typehandler(error):
        return jsonify({'error': 'error'}), 400

    return app
