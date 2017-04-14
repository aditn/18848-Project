import requests

r = requests.post("http://0.0.0.0:5000", data = {"foo":"hello world"})
print r.text
