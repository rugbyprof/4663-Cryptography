"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json

TOKEN = '892db29a750c4bd0e87184c04db19237ece'
UID = '8020'
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}

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
            user['pubkey'] = PUBKEYS[user['uid']]
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

    print(USERS)
    active = getActive()

    for a in active:
        print(a)

    result = postMessage("Hey sarah, thank's for making it. Again...",'5147600')

    #print(result)
    #5147600

