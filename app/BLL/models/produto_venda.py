from app.extensions import db

class ProdutoVenda(db.Model):
    __tablename__ = 'produtovenda_tb'

    produtovendaid = db.Column(db.Integer, primary_key=True)
    vendaid = db.Column(db.Integer, db.ForeignKey('venda_tb.vendaid'), nullable=False)
    produtoid = db.Column(db.Integer, db.ForeignKey('produto_tb.produtoid'), nullable=False)
    qtdproduto = db.Column(db.Integer, nullable=False)
    dt_inclusao = db.Column(db.DateTime)

    def __init__(self, vendaid, produtoid, qtdproduto, produtovendaid=None):
        self.produtovendaid = produtovendaid
        self.vendaid = vendaid
        self.produtoid = produtoid
        self.qtdproduto = qtdproduto

    def serialize(self):
        return {
            "produtoid": self.produtoid,
            "qtdproduto": self.qtdproduto
        }
