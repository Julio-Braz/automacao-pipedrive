import requests
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

headers = {'content-type': 'application/json'}

def busca_id():
    params = {'filter_id':'26','api_token':os.getenv('api')}
    url = 'https://fintera-sandbox.pipedrive.com/api/v1/deals'
    response = requests.get(url, params=params, headers=headers)

    filtro = response.json().get('data')

    ids = []

    for id in filtro:
        ids.append(id.get('id'))
        
    return ids