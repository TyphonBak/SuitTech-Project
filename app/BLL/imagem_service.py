import base64
import requests
from app.DAO.db_imagem import listar_por_produto as listar_por_produto_db, criar as criar_db, deletar as deletar_db
from app.BLL.imgur_controller.image_management import upload_image as imgur_upload, delete_image as imgur_delete
from app.BLL.models.imagem import Imagem

def gerenciar(imagens_bin, produto_id):
    try:
        erro, imagens_db = listar_por_produto_db(produto_id)

        if isinstance(imagens_db, list):
            imagens_db_base64 = [base64.b64encode(requests.get(imagem.url).content) for imagem in imagens_db]

            diff_images = set(imagens_bin) ^ set(imagens_db_base64)
            print("Dif ", diff_images)

            for img in diff_images:
                if img in imagens_bin:
                    img_gur = imgur_upload(img)
                    print('>',img_gur)
                    err, imagem = criar_db({ "produtoid": produto_id, **img_gur })
                    if err:
                        print(err)
                elif img in imagens_db_base64:
                    imagem_db = imagens_db[imagens_db_base64.index(img)]
                    err, imagem = deletar_db(imagem_db.imagemid)
                    if err:
                        print(err)
                else:
                    print("Somethins is wrong! ", img)

            return listar_por_produto_db(produto_id)
        else:
            return erro, None
    except Exception as e:
        return str(e), None

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
