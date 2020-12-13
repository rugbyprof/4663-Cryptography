"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""

import requests
import json
import base64
import pprint

#pip install cryptography
import cryptography
# Used to Generate Keys
# from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

#Used to Store Keys and Read in Keys
from cryptography.hazmat.primitives import serialization

#Used to do Encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


TOKEN = '892db29a750c4bd0e87184c04db19237ece'
UID = '8020'
API = f"http://msubackend.xyz/api/?token={TOKEN}&uid={UID}&route="

USERS = {}
KEYS = {}

def get_users():
    global USERS
    route = 'getUser'
    url = f"{API}{route}"

    r = requests.get(url)

    data = r.json()
    for d in data['data']:
        USERS[d['uid']] = d

    pprint.pprint(USERS)

def get_pubkeys():
    global KEYS
    route = 'getPubKey'
    url = f"{API}{route}"

    r = requests.get(url)

    data = r.json()
    for d in data['data']:
        KEYS[d['uid']] = d

    pprint.pprint(KEYS)

def send_message(message,to_uid):
    global KEYS   # needed if you encrypt
    route = 'postMessage'
    url = f"{API}{route}"

    payload = {
       'uid':UID,
       'to_uid':to_uid,
       'message':message,
       'token':TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()

if __name__ == '__main__':
    get_pubkeys()
    get_users()

    res = send_message("Here is a test message. I hope it works.",8020)

    print(res)

    if choice == 1:
        pass
    elif choice == 2:
        pass
