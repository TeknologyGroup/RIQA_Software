import requests

def upload_to_dataverse(data):
    response = requests.post('<https://dataverse.org/api/datasets>', json=data)
    return response.json()
