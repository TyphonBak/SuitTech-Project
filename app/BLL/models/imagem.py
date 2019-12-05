from app.extensions import db

class Imagem(db.Model):
    __tablename__ = 'imagem_tb'

    imagemid = db.Column(db.Integer, primary_key=True)
    produtoid = db.Column(db.Integer, db.ForeignKey('produto_tb.produtoid'), nullable=False, )
    nome = db.Column(db.String, nullable=False)

    def __init__(self, nome, produtoid, imagemid=None):
        self.imagemid = imagemid
        self.nome = nome
        self.produtoid = produtoid

    def __repr__(self):
        return f'<imagem {self.imagemid}>'

    def serialize(self):
        return {
            "imagemid": self.imagemid,
            "nome": self.nome,
            "produtoid": self.produtoid
        }

    def serialize_min(self):
        return {
            "imagemid": self.imagemid,
            "nome": self.nome
        }
