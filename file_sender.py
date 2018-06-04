import requests

url = 'http://0.0.0.0:5000/files/'

with open('sample.txt', 'rb') as f:
    r = requests.post(url, files={'sample.txt': f})
