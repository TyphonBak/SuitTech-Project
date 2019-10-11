from app.extensions import db

class Vendedor(db.Model):
    __tablename__ = 'vendedor_tb'

    vendedorid = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    cpf = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    email = db.Column(db.String)

    def __init__(self, nome, cpf, email, vendedorid=None):
        self.vendedorid = vendedorid
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def __repr__(self):
        return f'<vendedorid {self.vendedorid}>'
        
    def serialize(self):
        return {
            'vendedorid': self.vendedorid,
            'nome': self.nome,
            'cpf': self.cpf ,
            'email': self.email
        }
    