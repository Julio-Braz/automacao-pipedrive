import smtplib
import email.message
import dotenv
import os
import pega_dados_leads

import busca_id

dotenv.load_dotenv(dotenv.find_dotenv())
id = busca_id.busca_id()
nome = pega_dados_leads.pega_nomes(id)
horario = pega_dados_leads.pega_horario_reuniao(id)
link = pega_dados_leads.pega_link_reuniao(id)
email_endereco = pega_dados_leads.pega_email(id)
length = len(id)

def enviar_email(nome, horario,link,email_endereco):
    corpo_email = f'''Olá {nome} tudo bem? <br/><br/>Aqui é o Julio Braz consultor comercial da Fintera,
    e esse contato é para confirmar que estarei presente na demonstração hoje as {horario} h. <br/>
    <br/>Peço que acessem o link do Google meet abaixo no momento da videoconferência: {link} <br/><br/>
    Até lá.<br/><br/>
    Julio Braz<br/>
    Consultor Comercial<br/>
    (21) 98543-1195'''

    msg = email.message.Message()
    msg['Subject'] = "Lembrete Reunião Fintera"
    msg ['From'] = "julio.braz@fintera.com.br"
    msg["To"] = email_endereco
    password = os.getenv("senha_email")
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    #logando
    s.login(msg["From"], password)
    s.sendmail(msg["From"],[msg["To"]], msg.as_string().encode('-utf-8'))
    print("email enviado")

for i in range(length):
    enviar_email(nome[i], horario[i], link[i], email_endereco[i])