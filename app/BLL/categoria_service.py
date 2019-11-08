from app.DAO.db_categoria import listar as listar_db

def listar():
    try:
        erro, categorias = listar_db()
        if categorias:
            return 200, [categoria.serialize() for categoria in categorias]
        else:
            return 404, None
    except Exception:
        return 503, None
