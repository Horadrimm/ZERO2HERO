import requests
import json


def data_from_url(url):
    url_responce = requests.get(url)
    bc_price = url_responce.json()
    return bc_price
