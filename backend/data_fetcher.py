import requests
from flask import jsonify

def search_arxiv(query):
    url = f"http://export.arxiv.org/api/query?search_query={query}"
    response = requests.get(url)
    return jsonify(response.text)  # Restituisce dati ad app.py
