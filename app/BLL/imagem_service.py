import base64
import requests
from app.DAO.db_imagem import listar_por_produto as listar_por_produto_db, criar as criar_db, deletar as deletar_db
from app.BLL.imgur_controller.image_management import upload_image as imgur_upload, delete_image as imgur_delete

def gerenciar(imagens_bin, produto_id):
    try:
        erro, imagens_db = listar_por_produto_db(produto_id)

        if imagens_db:
            imagens_db_base64 = [base64.b64encode(requests.get(imagem.url).content) for imagem in imagens_db]

            diff_images = set(imagens_bin) ^ set(imagens_db_base64)

            for img in diff_images:
                if img in imagens_bin:
                    img_gur = imgur_upload(img)
                    err, imagem = criar_db({ "produto_id": produto_id, **img_gur })
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
