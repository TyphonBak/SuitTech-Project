from app.extensions import db

class Categoria(db.Model):
    __tablename__ = 'categoria_tb'

    categoriaid = db.Column(db.Integer)
    nome = db.Column(db.String)

    def __init__(self, nome, categoriaid=None):
        self.categoriaid = categoriaid
        self.nome = nome

    def __repr__(self):
        return f'<id {self.categoriaid}>'

    def serialize(self):
        return {
            'categoriaid': self.categoriaid,
            'nome': self.nome
        }