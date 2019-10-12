from app.extensions import db

class Cliente(db.Model):
    __tablename__ = 'cliente_tb'

    clienteid = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None), unique=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    logradouro = db.Column(db.String)
    cep = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    numero = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))
    cidade = db.Column(db.String)
    uf  = db.Column(db.String)
    telefone = db.Column(db.Numeric(asdecimal=False, decimal_return_scale=None))

    def __init__(self, nome, cpf_cnpj, email, logradouro, cep, numero, cidade, uf, telefone, clienteid=None):
        self.clienteid = clienteid
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.cep = cep  
        self.numero = numero
        self.cidade = cidade
        self.uf = uf
        self.telefone = telefone

    def __repr__(self):
        return f'<id {self.clienteid}>'
        
    def serialize(self):
        return {
            'clienteid': self.clienteid,
            'nome': self.nome,
            'cpf_cnpj': self.cpf_cnpj,
            'email': self.email,
            'logradouro': self.logradouro,
            'cep': self.cep,
            'numero': self.numero,
            'cidade': self.cidade,
            'uf': self.uf,
            'telefone': self.telefone
        }

    def serialize_min(self):
        return {
            'clienteid': self.clienteid,
            'nome': self.nome,
            'email': self.email
        }
