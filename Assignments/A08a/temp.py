def sendMessage(from_id,to_id,message,token):
    posturl = "http://msubackend.xyz/api/?route=postMessage"
    payload = {
        'from_id':from_id,
        'to_id':to_id,
        'message':message,
        'token':token
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(posturl, headers=headers, json=payload)
