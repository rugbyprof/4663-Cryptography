"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json
import base64

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


class ClientHelper:
    def __init__(self,**kwargs):

        self.uid = kwargs.get('uid',None)
        self.token = kwargs.get('token',None)
        self.api = kwargs.get('api',None)
        self.public_key = ''
        self.private_key = ''
        self.pubKeys = {}
        self.users = {}
        
        self.generate_keys()
        self.publishKey()
        
        self.getPubkeys()
        self.loadUsers()
        
    def serializePubKey(self,pubkey):
        """serializePubKey

        Args:
            pubkey (string): loads a byte type public key into serialized string

        Returns:
            string: serialized key
        """
        return serialization.load_pem_public_key(pubkey)

    def generate_keys(self,exp=65537,ksize=2048):
        """
        public_exponent (int) – The public exponent of the new key. Often 
                        one of the small Fermat primes 3, 5, 17, 257 or 65537.
        key_size (int) – The length in bits of the modulus. Should be at least 2048.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=exp,
            key_size=ksize
            # backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        

    def getPubkeys(self):
        route = 'getPubKey'
        url = f"{self.api}{route}&token={self.token}&uid={self.uid}"
        r = requests.get(url)

        try:
            keys = r.json()
        except ValueError as e:
            print("Invalid Json!!!")
            print(r.text)

        for key in keys['data']:
            self.pubKeys[key['uid']] = key


    def loadUsers(self):
        route = 'getUser'
        url = f"{self.api}{route}&token={self.token}&uid={self.uid}"
        r = requests.get(url)

        try:
            users = r.json()
        except ValueError as e:
            print("Invalid Json!!!")
            print(r.text)

        for user in users['data']:
            if user['uid'] in self.pubKeys:
                user['pubkey'] = self.pubKeys[user['uid']]['pubkey']
                self.users[user['uid']] = user

    def encryptMessage(self,message,uid):
        # this is me loading a public key from my key dictionary
        pk = self.serializePubKey(self.users[uid]['pubkey'].encode('utf-8'))

        # this encrypts the encoded plaintext mesage with a users public key
        encrypted = pk.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return encrypted

    def getActive(self):
        route = 'getActive'
        url = f"{self.api}{route}&token={self.token}&uid={self.uid}"
        r = requests.get(url)

        active_users = r.json()
        active_users = active_users['data']

        real_active_users = []
        for active in active_users:
            active['fname'] = self.users[active['uid']]['fname']
            active['lname'] = self.users[active['uid']]['lname']
            active['email'] = self.users[active['uid']]['email']
            active['pubkey'] = self.pubKeys[active['uid']]
            real_active_users.append(active)

        return real_active_users

    def decryptMessage(self,encrypted):
        # I decrypt message encoded with public key
        message = self.private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return message

    def postMessage(self,message,to_uid):
        route = 'postMessage'
        url = f"{self.api}{route}&token={self.token}&uid={self.uid}"

        message = self.encryptMessage(message,to_uid)

        payload = {
            'uid':self.uid,
            'to_uid':to_uid,
            'message':message,
            'token':self.token
        }

        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers, json=payload)
        return r.json()


    def publishKey(self):
        route = 'postPubKey'
        url = f"{self.api}{route}&token={self.token}&uid={self.uid}"
        
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        # serialized = serialization.load_pem_public_key(pem)
        #8wIDAQAB
        payload = {
            'pub_key':pem.decode('utf8'),
            'uid':self.uid,
            'token':self.token
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post( url, headers=headers, json=payload)
        
        return r.json()

if __name__=='__main__':
    config = {
        'token' : '892db29a750c4bd0e87184c04db19237ece',
        'uid' : '8020',
        'api' : 'http://msubackend.xyz/api/?route='
    }
    #result = postMessage("This is a plaintext message encrypted with public key 5147600",'5147600')


    # # this is me loading a public key from my key dictionary
    # pk = serializePubKey(self.users['5147600']['pubkey'].encode('utf-8'))

    # # this encrypts the encoded plaintext mesage with a users public key
    # encrypted = pk.encrypt(
    #     "This is a plaintext message encrypted with public key 5147600".encode('utf-8'),
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #     )
    # )
    # print(encrypted)

    # # For testing, I load same persons private key from a file
    # with open('./keys/5147600.private.key', "rb") as key_file:
    #     private_key = serialization.load_pem_private_key(
    #         key_file.read(),
    #         password=None
    #     )
    # # I decrypt message encoded with public key
    # original_message = private_key.decrypt(
    #     encrypted,
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #     )
    # )

    # # print decrypted message
    # print(original_message)
    # encoded = base64.b64encode(encrypted)
    # result = postMessage(encoded.decode('utf8'),'8020')


    # # now get the message and decode it
    # route = 'getMessage'
    # url = f"{self.api}{route}&token={self.token}&uid={self.uid}&latest=true"
    # r = requests.get(url)
    # data = r.json()
    # message = data["data"][0]

    # #print messages (still encrypted)
    # print(message)

    # # turn it back into its original bytes form
    # decoded = base64.b64decode(message['message'])
    # print(decoded)

    # private_key = None
    # public_key = None
    
    # private_key = rsa.generate_private_key(
    #     public_exponent=65537,
    #     key_size=2048
    #     # backend=default_backend()
    # )
    # public_key = private_key.public_key()

    # pem = public_key.public_bytes(
    #     encoding=serialization.Encoding.PEM,
    #     format=serialization.PublicFormat.SubjectPublicKeyInfo
    # )
    
    # r = publishKey(pem.decode('utf8'))
    # print(r)

    # #should be decryptable now with right private key.

    # #5147600

