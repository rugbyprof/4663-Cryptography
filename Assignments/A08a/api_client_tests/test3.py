"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json

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
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}


def loadPubKey(pubkey):
    return serialization.load_pem_public_key(pubkey)

def pubKey():
    global PUBKEYS
    route = 'getPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        keys = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for key in keys['data']:
        PUBKEYS[key['uid']] = key



def getUsers():
    global USERS
    global PUBKEYS

    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        users = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for user in users['data']:
        if user['uid'] in PUBKEYS:
            user['pubkey'] = PUBKEYS[user['uid']]['pubkey']
            USERS[user['uid']] = user



def getActive():
    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = PUBKEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users


def postMessage(message,to_uid):
    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

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
    pubKey()
    getUsers()

    active = getActive()

    # for a in active:
    #     print(a)

    #result = postMessage("This is a plaintext message encrypted with public key 5147600",'5147600')


    # this is me loading a public key from my key dictionary
    pk = loadPubKey(USERS['5147600']['pubkey'].encode('utf-8'))

    # this encrypts the encoded plaintext mesage with a users public key
    encrypted = pk.encrypt(
        "This is a plaintext message encrypted with public key 5147600".encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(encrypted)

    # For testing, I load same persons private key from a file
    with open('./keys/5147600.private.key', "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    # I decrypt message encoded with public key
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # print decrypted message
    print(original_message)



    #5147600

