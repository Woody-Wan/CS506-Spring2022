import requests
import json

"""
    Google Books Api
    See: https://developers.google.com/books/
    get https://www.googleapis.com/books/v1/volumes?q=
"""

def get(topic=""):
    BASEURL = 'https://www.googleapis.com/books/v1/volumes'
    headers = {'Content-Type': 'application/json'}

    response = requests.get(BASEURL + "?q=" + topic, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

    return response # this return a dict



