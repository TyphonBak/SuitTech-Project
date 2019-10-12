from app.extensions import db

class Venda(db.Model):
    __tablename__ = 'venda_tb'

    vendaid = db.Column(db.Integer, primary_key=True)
    vendedorid = db.Column(db.Integer)
    clienteid = db.Column(db.Integer)

    def __init__(self, vendedorid, clienteid, vendaid=None):
        self.vendaid = vendaid
        self.vendedorid = vendedorid
        self.clienteid = clienteid
        
    def serialize(self):
        return {
            'vendaid': self.vendaid,
            'vendedorid': self.vendedorid,
            'clienteid': self.clienteid
        }
