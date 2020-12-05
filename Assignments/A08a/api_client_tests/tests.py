"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests
from crypto_class import Crypto 
import sys
import json
from random import shuffle
# Import the necessary packages
# https://pypi.org/project/console-menu/
from consolemenu import *
from consolemenu.items import *

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

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


TOKEN = '892db29a750c4bd0e87184c04db19237ece'
UID = '8020'
BASEURL = f"http://msubackend.xyz/api/?token={TOKEN}&uid={UID}&route="

def random_user():
    shuffle(uids_tokens)
    return uids_tokens[0]

def runGetRequest(url,dbug=None):
    """
    """
    if dbug:
        print(dbug)
        print(url)
        
    r = requests.get(url)

    if dbug:
        print(r)

    try:
        response = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)
    
    if dbug:
        print(type(response))

    if not response['success']:
        print("Request Failed!!")
    
    return response['data']

def random_quote():
    shuffle(quotes)
    return quotes[0]

def editUser(uid,fname,lname,screen_name,email,token):
    posturl = BASEURL+"postUser"
    payload = {
        'fname':fname,
        'lname':lname,
        'screen_name':screen_name,
        'email':email,
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
    return r.json()


def publishKey(uid,token,pubkey):
    posturl = BASEURL+"postPubKey"
    payload = {
        'pub_key':pubkey,
        'uid':uid,
        'token':token
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post( posturl, headers=headers, json=payload)
    return r.json()

def sendMessage(uid,to_uid,message,token):
    posturl = BASEURL+"postMessage"
    payload = {
       'uid':uid,
       'to_uid':to_uid,
       'message':message,
       'token':token
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
    return r.json()

def getUser(**kwargs):
    getUrl = BASEURL+"getUser"

    params = {}
    params['email'] = kwargs.get('email',0)
    params['fname']  = kwargs.get('fname',0)
    params['lname']  = kwargs.get('lname',0)
    params['user_id']  = kwargs.get('user_id',0)
    
    for k,v in params.items():
        if str(v) != str(0):
            getUrl += f"&{k}={v}"

    return runGetRequest(getUrl)

def getActive(limit=None):
    #update `active` set last_connect = now() where uid in ('100','102','103')
    active_users = []
    getUrl = BASEURL+"getActive"

    if limit:
        getUrl += f"&limit={limit}"
    
    return runGetRequest(getUrl)

def getPublicKey(user_id=None):
    getUrl = BASEURL+"getPubKey"

    if user_id:
        getUrl += f"&user_id={user_id}"
   
    pubkey = runGetRequest(getUrl)
    return pubkey[0]['pubkey']

def grabActiveData():
    data = []
    active_users = getActive()

    for auser in active_users:
        user_info = getUser(user_id=auser['uid'])
        user_info = user_info[0]

        user_info['pubkey'] = getPublicKey(auser['uid'])
        data.append(user_info)
    
    return data

def getKeys():
    getUrl = BASEURL+"getKeys"

    r = requests.get(getUrl)
    return r.json()

def printMenu():

    active_data = grabActiveData()

    names = []
    for active in active_data:
        names.append(active['fname'])

    # Create the menu
    menu = ConsoleMenu("Console Messenger Project", "Encrypted Communication")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

    # A FunctionItem runs a Python function when selected
    function_item = FunctionItem("Active Users", getActive)

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command",  "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(names)

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Active Users", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(menu_item)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

if __name__== '__main__':
    printMenu()
    #active = grabActiveData()



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

    # r = sendMessage("5178600",UID,"Crepes are better than waffles.","e23a96ca37903c94a39b2a3792159e51")
    # print(r)