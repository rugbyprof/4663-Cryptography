"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json

TOKEN = '892db29a750c4bd0e87184c04db19237ece'
UID = '8020'
API = 'http://msubackend.xyz/api/?route='


def test_json(data):
    try:
        json.loads(data)
    except:
        return False
    
    return True


def get_user_with_id(id,users):
    for user in users:
        if user['uid'] == id:
            return user
        #print(user)

    return None            


def get_users():
    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    r = requests.get(url)

    data = r.json()

    with open("/Users/griffin/Dropbox/_Courses/4663-Cryptography/Assignments/A08a/api_client_tests/chat_users.json","w") as f:
        f.write(json.dumps(data['data']))

    return data['data']

def send_message(message,to_uid):
    route = 'postMessage'
    posturl = f"{API}{route}"

    payload = {
       'uid':UID,
       'to_uid':to_uid,
       'message':message,
       'token':TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
    return r.json()

if __name__ == '__main__':
    users = get_users()

    user = get_user_with_id('5519700',users)

    print(user)

    resp = send_message("hey hows it goin im still flustered, and pregnant again with triplets and aliens",'5519700')

    print(resp)

    print(resp['success'])
  
