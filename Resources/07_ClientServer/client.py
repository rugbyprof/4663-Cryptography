"""
https://requests.readthedocs.io/en/master/user/quickstart/
https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
"""
import requests
from crypto_class import Crypto     # import the crypto class
import os
import sys

crypt_helper = Crypto()             # instance of crypto class  

def generate_keys():
    r = requests.get('http://localhost:8080/public_key/02')
    print(r.text)

def message():
    m = input("Message:")
    p = requests.post('http://localhost:8080/message',json={"message":m})
    

def end_program():
    print("Great ... quitter.")
    sys.exit()

choice_functions = {
    "Generate Keys":generate_keys,
    #"See Online":get_logged_in
    "Message":message,
    "Quit":end_program
}

def getChoice():
    i = 1
    choices = [None]
    for k,v in choice_functions.items():
        print(f"{i}. {k}")
        choices.append(k)
        i += 1
    c=input(">>> ")
    return choices[int(c)]

if __name__=='__main__':

    func_key = getChoice()

    print(func_key)
    while True:
        choice_functions[func_key]()
        func_key = getChoice()


