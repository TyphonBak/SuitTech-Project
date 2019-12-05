import base64
import requests
from app.DAO.db_imagem import listar_por_produto as listar_por_produto_db, criar as criar_db, deletar as deletar_db
from app.BLL.imgur_controller.image_management import upload_image as imgur_upload, delete_image as imgur_delete
from app.BLL.models.imagem import Imagem

def gerenciar2(images_name, produto_id):
    try:
        erro, images_db = listar_por_produto_db(produto_id)

        if isinstance(images_db, list):
            nome_sem_match = set(images_name + [imagem.nome for imagem in images_db])
            for nome in nome_sem_match:
                if nome in images_name:
                    criar_db({ "produtoid": produto_id, "nome": nome })
                else:
                    imagens_a_deletar = list(filter(lambda img: img.nome == nome, images_db))
                    [deletar_db(imagem.imagemid) for imagem in imagens_a_deletar]
            erro, images_db = listar_por_produto_db(produto_id)
            print(erro)
            return erro, [img.serialize() for img in images_db]
        else:
            print(erro)
            return erro, None
    except Exception as e:
        print(e)
        return str(e), None
