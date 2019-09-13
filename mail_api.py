from flask import Blueprint, request
from email_service

bp_mail = Blueprint('BP mail', __name__)

@bp_mail.route('/mail_service/promo', methods=['POST'])
def email_promo():
    
    promo_email = request.get_json()
    #Chamar camada logica passando promo_email
    
    return 'Retorno da Camada Logica'

@bp_mail.route('/mail_service/email_sac', methods=['POST'])
def email_sac():
    
    sac_email = request.get_json()
    #Chamar camada logica passando sac_email
    
    return 'Retorno da Camada Logica'
