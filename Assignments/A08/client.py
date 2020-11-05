"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests

r = requests.get('http://localhost:8080/public_key/02')

print(r.text)