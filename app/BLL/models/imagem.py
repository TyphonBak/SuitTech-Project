from app.extensions import db

class Imagem(db.Model):
    __tablename__ = 'imagem_tb'

    imagemid = db.Column(db.Integer, primary_key=True)
    produtoid = db.Column(db.Integer, db.ForeignKey('produto_tb.produtoid'), nullable=False)
    imgur_id = db.Column(db.String, nullable=False, unique=True)
    url = db.Column(db.String, nullable=False)
    delete_hash = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, imgur_id, url, delete_hash, imagemid=None):
        self.imagemid = imagemid
        self.imgur_id = imgur_id
        self.url = url
        self.delete_hash = delete_hash

    def __repr__(self):
        return f'<imagem {self.imagemid}>'

    def serialize(self):
        return {
            "imagemid": self.imagemid,
            "imgur_id": self.imgur_id,
            "url": self.url
        }

    def serialize_min(self):
        return {
            "imagemid": self.imagemid,
            "url": self.url
        }
