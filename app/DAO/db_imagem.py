from app.extensions import db
from app.BLL.models.imagem import Imagem

def listar_por_produto(produto_id):
    try:
        imagens = Imagem.query.filter_by(produtoid=produto_id).all()
        return None, imagens
    except Exception as e:
        print(str(e))
        return str(e), None

def criar(dados):
    try:
        imagem = Imagem(**dados)
        db.session.add(imagem)
        db.session.commit()
        return None, imagem
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return str(e.__dict__.get('orig')), None

def deletar(imagemid):
    try:
        imagem = Imagem.query.get(imagemid)
        if not isinstance(imagem, Imagem):
            return None, None
        db.session.delete(imagem)
        db.session.commit()
        return None, imagem
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return str(e), None
