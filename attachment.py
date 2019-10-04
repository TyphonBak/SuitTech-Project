import config
import os
import smtplib
import imghdr
import re
from email.message import EmailMessage

cliente = []

def check(): #Checa validade do e-mail
    if(re.search(config.validacao,config.EMAIL_SENDER)):  
        print("Email Válido")
        cliente.append(config.EMAIL_SENDER)
          
    else:  
        return "Email Inválido"

def monta_email_sac(mensagemCliente, logo): #Cria e-mail sac
    conteudo = f'<h1> Olá {mensagemCliente}</h1>'
    titulo = f'<h1> Obrigado por ter entrado em contato conosco!</h1>'
    imagem = f'<img src={logo}>'
    info_institucional = """
    <p>Obrigado Por Ecolher a TITA'RTE</p>
    """

    return f"""
    <!DOCTYPE html>
    <html>
        <body style="background-color: gray; width: 600px">
            {titulo} \
            {conteudo}\
            {imagem} \
            {info_institucional} \
                
        </body>
    </html>
    """

def envia_email_sac(cliente): #Envia e-mail sac
    EMAIL_ADDRESS = config.EMAIL_ADRESS
    EMAIL_PASSWORD = config.PASSWORD
    try:
        mensagem = EmailMessage()
        mensagem['Subject'] = 'Recebemos Seu E-mail!!!'
        mensagem['From'] = EMAIL_ADDRESS
        mensagem['To'] = cliente
        corpo_email = monta_email_sac(mensagemCliente, logo)
        mensagem.add_alternative(corpo_email, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, 
            EMAIL_PASSWORD)
            smtp.send_message(mensagem)
    except Exception as e:
        #import pdb; pdb.set_trace()
        print('ERROR!! ',e)


def monta_html_promo(produto, cliente): #Cria email promocional
    titulo = f'<h1>Bom dia {cliente.get("nome")}, temos um novo produto!</h1>'
    imagem = f'<img src={produto.get("url")}>'
    nome_produto = f'<h3>{produto.get("nome")}</h3>'
    descricao = f'<p>{produto.get("descricao")}</p>'
    info_institucional = """
    <p>Texto fixo generico</p>
    """

    return f"""
    <!DOCTYPE html>
    <html>
        <body style="background-color: gray; width: 600px">
            {titulo} \
            {imagem} \
            {nome_produto} \
            {descricao} \
            {info_institucional} \
        </body>
    </html>
    """

def envia_email_promo(id_produto): #Envia e-mail promocional

    EMAIL_ADDRESS = config.EMAIL_ADRESS
    EMAIL_PASSWORD = config.PASSWORD
    #Mudar chamada do produto e de clientes
    produto = {'buscar produto com id_produto': id_produto}
    clientes = [{'email': 'email@inexistente'}, {'email': 'cezar.filho@aluno.faculdadeimpacta.com.br'}, {'email': None}]#'chama api listar clientes'

    for cliente in clientes:
        try:
            mensagem = EmailMessage()
            mensagem['Subject'] = 'Venha conferir as novidades!!!'
            mensagem['From'] = EMAIL_ADDRESS
            mensagem['To'] = cliente.get('email')
            corpo_email = monta_html_promo(produto, cliente)
            mensagem.add_alternative(corpo_email, subtype='html')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, 
                EMAIL_PASSWORD)
                smtp.send_message(mensagem)
        except Exception as e:
            #import pdb; pdb.set_trace()
            print('ERROR!! ',e)


mensagemCliente = "Bixão Safadinho!"
logo = "https://i.imgur.com/gw0nosg.png"

check()
envia_email_promo(1)
envia_email_sac(cliente)
