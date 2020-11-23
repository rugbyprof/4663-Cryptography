"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests
from crypto_class import Crypto 
import sys

"""
 Its up to you to alter the Crypto class to store keys correctly 
 as well as use them to encrypt messages with the proper public key. 
"""
C = Crypto()

"""
 These two statemets generate keys and save them, but with hard
 coded values. Definitely needs changed up. 
"""
C.generate_keys()
C.store_keys()

BASEURL = "http://msubackend.xyz/api/"

def editUser(uid,fname,lname,screen_name,email,token):
    posturl = BASEURL+"?route=postUser"
    payload = {
        'uid':uid,
        'fname':fname,
        'lname':lname,
        'screen_name':screen_name,
        'email':email,
        'token':token
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
    return r.text


def publishKey(uid,token,pubkey):
    posturl = BASEURL+"?route=postPubKey"
    payload = {
        'pub_key':pubkey,
        'uid':uid,
        'token':token
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post( posturl, headers=headers, json=payload)
    return r.text


def sendMessage(from_id,to_id,message,token):
    posturl = BASEURL+"?route=postMessage"
    payload = {
       'from_id':from_id,
       'to_id':to_id,
       'message':message,
       'token':token
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
    return r.text

def getUser(**kwargs):
    getUrl = BASEURL+"?route=getUser"

    params = {}
    params['token'] = kwargs.get('token',0)
    params['uid'] = kwargs.get('uid',0)
    params['email'] = kwargs.get('email',0)
    params['fname']  = kwargs.get('fname',0)
    params['lname']  = kwargs.get('lname',0)

    if params['token'] == 0 or params['uid'] == 0:
        print("Error: need tokan and uid")
        sys.exit()
    
    for k,v in params.items():
        getUrl += f"&{k}={v}"

    r = requests.get(getUrl)
    return r.text

def getActive(**kwargs):
    getUrl = BASEURL+"?route=getUser"

    params = {}
    params['token'] = kwargs.get('token',0)
    params['uid'] = kwargs.get('uid',0)

    if params['token'] == 0 or params['uid'] == 0:
        print("Error: need tokan and uid")
        sys.exit()
    
    for k,v in params.items():
        getUrl += f"&{k}={v}"

    r = requests.get(getUrl)
    return r.text

def getKeys(**kwargs):
    getUrl = BASEURL+"?route=getUser"

    params = {}
    params['token'] = kwargs.get('token',0)
    params['uid'] = kwargs.get('uid',0)

    if params['token'] == 0 or params['uid'] == 0:
        print("Error: need tokan and uid")
        sys.exit()
    
    for k,v in params.items():
        getUrl += f"&{k}={v}"

    r = requests.get(getUrl)
    return r.text

if __name__== '__main__':
    token = '52e59d8486f6a67e1ec6c281e665e'
    uid = '3818'

    # r = sendMessage('3818','8020','Hey Ricky Bobby. You wanna shake n bake?',token)
    # print(r)

    key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvI3QjAT3naoP8ZGFwKmc
9b01//L0uUVKOZH33333333333333333333333333333333V5mxJzGvqYekqg0SL
VGHkpH33333333333333333333333333333333uBgkJo35hwK8HfIiYtwQxCdDWi
INA7XYoy5/D11GauZN0a3/7mZU4uDY6iw3Js7wNlm6job93JVGTq4Fc9QGEZz6Pk
TwIDAQAB
-----END PUBLIC KEY-----"""

    r = publishKey(uid,token,key)
    print(r)

    r = getUser(token=token,uid=uid)
    print(r)

    r = getActive(token=token,uid=uid)
    print(r)