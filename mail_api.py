from flask import Blueprint, request
from email_service

bp_mail = Blueprint('BP mail', __name__)

@bp_mail.route('/mail_service/promo', methods=['POST'])
def email_promo():
    request.get_json()

@bp_mail.route('/mail_service/email_sac', methods=['POST'])
def email_sac():
    request.get_json()
