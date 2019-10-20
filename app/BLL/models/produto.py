from app.extensions import db

class Produto(db.Model):
    __tablename__ = 'produto_tb'

    produtoid = db.Column(db.Integer, primary_key=True)
    categoriaid = db.Column(db.Integer, db.ForeignKey('categoria_tb.categoriaid'))
    nome = db.Column(db.String)
    peso = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    altura = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    largura = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    cor = db.Column(db.String)
    material = db.Column(db.String)
    precocusto = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    precovendavarejo = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    precovendaatacado = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    imposto = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    estoque = db.Column(db.Integer)
    descricao = db.Column(db.String)

    categoria = db.relationship('Categoria', backref="produto_tb", lazy="joined")

    def __init__(self, categoriaid, nome, peso, altura, largura, cor, material, precocusto, precovendavarejo, precovendaatacado, imposto, estoque, descricao, produtoid=None):
        self.produtoid = produtoid
        self.categoriaid = categoriaid
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.largura = largura  
        self.cor = cor
        self.material = material
        self.precocusto = precocusto
        self.precovendavarejo = precovendavarejo
        self.precovendaatacado = precovendaatacado
        self.imposto = imposto
        self.estoque = estoque
        self.descricao = descricao

    def __repr__(self):
        return f'<Produto {self.produtoid}>'

    def serialize(self):
        return {
            "produtoid": self.produtoid,
            "categoria": None if not self.categoria else self.categoria.serialize(),
            "nome": self.nome,
            "peso": self.peso,
            "altura": self.altura,
            "largura": self.largura,
            "cor": self.cor,
            "material": self.material,
            "precocusto": self.precocusto,
            "precovendavarejo": self.precovendavarejo,
            "precovendaatacado": self.precovendaatacado,
            "imposto": self.imposto,
            "estoque": self.estoque,
            "descricao": self.descricao
        }

    def serialize_min(self):
        return {
            'produtoid': self.produtoid,
            'nome': self.nome,
            'categoriaid': self.categoriaid
        }
