import config
import os
import smtplib
import imghdr
import re
from email.message import EmailMessage

def email_promo(produto):
    conteudo = '''html_promo_base'''
    emails = lista_emails()
    envia_email(conteudo, emails)

def email_sac(mensagem, de):
    envia_email(mensagem, config.EMAIL_ADRESS)    


def check():
    if(re.search(config.validacao,config.EMAIL_SENDER)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")

def envia_email(conteudo, lista_dest):

    EMAIL_ADDRESS = config.EMAIL_ADRESS
    EMAIL_PASSWORD = config.PASSWORD

    mensagem = EmailMessage()
    mensagem['Subject'] = 'Testando Menssagem No E-mail Sender Python mais imagens!!!'
    mensagem['From'] = EMAIL_ADDRESS
    mensagem['To'] = config.EMAIL_SENDER

    mensagem.set_content('This is SPARTAN email') # Simple mail html??

    mensagem.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">TESTANDO MEU SEND MAIL COM FOTOS</h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Logo_2013_Google.png">
        </body>
    </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(mensagem)

check()
envia_email()
