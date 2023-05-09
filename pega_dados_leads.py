import requests
import dotenv
import os
import busca_id
from datetime import datetime, timedelta
dotenv.load_dotenv(dotenv.find_dotenv())

headers = {'content-type': 'application/json'}
params = {'api_token':os.getenv('api')}
ids = busca_id.busca_id()

def pega_email(ids):
    emails = []

    for id in ids:
        url = f'https://fintera-sandbox.pipedrive.com/api/v1/deals/{id}'
        response = requests.get(url, params=params, headers=headers)
        emails_pegos = response.json().get('data').get('person_id').get('email')[:]
        for email in emails_pegos:
            if email.get('label') == "work":
                emails.append(email.get('value'))
                break
    return emails

def pega_nomes(ids):
    nomes = []

    for id in ids:
        url = f'https://fintera-sandbox.pipedrive.com/api/v1/deals/{id}'
        response = requests.get(url, params=params, headers=headers)
        nomes_pegos = response.json().get('data').get('person_id').get('name')
        nomes.append(nomes_pegos.title())
    return nomes
  
def pega_horario_reuniao(ids):    
    horas = []
    
    for id in ids:
        url = f'https://fintera-sandbox.pipedrive.com/api/v1/deals/{id}'
        response = requests.get(url, params=params, headers=headers)
        horario_reuniao = response.json().get('data').get('next_activity').get('due_time')
        horas_corrigida = str(datetime.strptime(horario_reuniao,'%H:%M') -timedelta(hours=+3))
        horas.append(horas_corrigida[11:])
        
    return horas

def pega_link_reuniao(ids): 
    link = []

    for id in ids:
        url = f'https://fintera-sandbox.pipedrive.com/api/v1/deals/{id}'
        response = requests.get(url, params=params, headers=headers)
        link_reuniao = response.json().get('data').get('next_activity').get('conference_meeting_url')
        link.append(link_reuniao)
    return link

if __name__ == '__main__':
    print(pega_email(ids))
    print(pega_nomes(ids))
    print(pega_horario_reuniao(ids))
    print(pega_link_reuniao(ids))