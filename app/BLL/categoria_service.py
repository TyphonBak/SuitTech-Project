from app.DAO.db_categoria import listar as listar_db

def listar():
    try:
        return 200, [categoria.serialize() for categoria in listar_db()]
    except Exception:
        return 503, None
