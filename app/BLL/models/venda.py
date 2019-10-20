from app.extensions import db

class Venda(db.Model):
    __tablename__ = 'venda_tb'

    vendaid = db.Column(db.Integer, primary_key=True)
    vendedorid = db.Column(db.Integer, db.ForeignKey('vendedor_tb.vendedorid'))
    clienteid = db.Column(db.Integer, db.ForeignKey('cliente_tb.clienteid'))

    vendedor = db.relationship('Vendedor', backref="venda_tb", lazy="joined")
    cliente = db.relationship('Cliente', backref="venda_tb", lazy="joined")
    produtos = db.relationship('ProdutoVenda', backref="venda_tb", lazy="joined", cascade="all, delete-orphan")

    def __init__(self, vendedorid, clienteid, vendaid=None):
        self.vendaid = vendaid
        self.vendedorid = vendedorid
        self.clienteid = clienteid

    def __repr__(self):
        return f'<Venda {self.vendaid}>'

    def serialize(self):
        return {
            'vendaid': self.vendaid,
            'vendedor': None if not self.vendedor else self.vendedor.serialize(),
            'cliente': None if not self.cliente else self.cliente.serialize_min(),
            'produtos': None if not self.produtos else [produto.serialize() for produto in self.produtos]
        }
