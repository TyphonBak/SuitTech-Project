from flask import Blueprint, render_template
from app.VIEWS.doc_description import doc as documentacao

bp_doc = Blueprint('bp_doc', __name__)

@bp_doc.route('/doc')
def index():
    return render_template('documentacao.html', documentacao=documentacao)
