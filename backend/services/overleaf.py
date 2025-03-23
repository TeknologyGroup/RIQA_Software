import requests

def upload_to_overleaf(data):
    response = requests.post('<https://api.overleaf.com/projects>', json=data)
    return response.json()
