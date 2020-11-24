"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests
from crypto_class import Crypto 
import sys
import json
from random import shuffle



# get user ids 
with open('uids_tokens.json') as f:
    uids_tokens = json.loads(f.read())

with open('quotes.json') as f:
    temp = json.loads(f.read())
quotes = []
for row in temp:
    quotes.append(row['quote'])

with open('enterpreneur-quotes.json') as f:
    temp = json.loads(f.read())
for row in temp:
    quotes.append(row['text'])

BASEURL = "http://msubackend.xyz/api/"

TOKEN = '892db29a750c4bd0e87184c04db19237ece'

UID = '8020'

def random_user():
    shuffle(uids_tokens)
    return uids_tokens[0]

def random_quote():
    shuffle(quotes)
    return quotes[0]

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


def sendMessage(uid,to_uid,message,token):
    posturl = BASEURL+"?route=postMessage"
    payload = {
       'uid':uid,
       'to_uid':to_uid,
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
    getUrl = BASEURL+"?route=getActive"

    params = {}
    params['token'] = kwargs.get('token',0)
    params['uid'] = kwargs.get('uid',0)
    params['limit']= kwargs.get('limit',0)

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

    # for user in uids_tokens:
    #     C = Crypto()
    #     C.generate_keys()
    #     public,private = C.get_storable_keys()
    #     uid = user['uid']
    #     token = user['token']
    #     with open(f"./keys/{uid}.private.key","wb") as f:
    #         f.write(private)
    #     with open(f"./keys/{uid}.public.key","wb") as f:
    #         f.write(public)

    #     print(public.strip().decode())
    #     r = publishKey(uid,token,public.strip().decode())
    #     print(r)

    # for i in range(300):
    #     user1 = random_user()
    #     user2 = random_user()
    #     quote = random_quote()

    #     print(quote)

    #     r = sendMessage(user1['uid'],user2['uid'],quote,user1['token'])
    #     print(r)

    
    # user = random_user()
    # r = getUser(token=user['token'],uid=user['uid'])
    # print(r)

    # user = random_user()
    # r = getActive(token=user['token'],uid=user['uid'],limit=900)
    # print(r)

    # r = editUser(UID,'Cal','Norton Jr.','silly name','itookrickybobbyswife@gotcha.com',TOKEN)
    # print(r)

# {"uid":"5178600","token":"e23a96ca37903c94a39b2a3792159e51"}

    r = sendMessage("5178600",UID,"Crepes are better than waffles.","e23a96ca37903c94a39b2a3792159e51")
    print(r)