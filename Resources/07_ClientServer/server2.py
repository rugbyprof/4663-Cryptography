import os
import sys
import json

from flask import Flask  
from flask import request           # grab params off the URL
from flask import jsonify           # package stuff in json the 
                                    #    flask way
from flask_cors import CORS         # Cross origin scripting 
                                    #    ignore for now
from flask import send_file         # shouldn't need
import glob                         # glob reads directories
from crypto_class import Crypto     # import the crypto class

crypt_helper = Crypto()             # instance of crypto class              

app = Flask(__name__)               # set app here so its globale
CORS(app)



#    ____   ___  _   _ _____ _____ ____  
#   |  _ \ / _ \| | | |_   _| ____/ ___| 
#   | |_) | | | | | | | | | |  _| \___ \ 
#   |  _ <| |_| | |_| | | | | |___ ___) |
#   |_| \_\\___/ \___/  |_| |_____|____/ 

@app.route("/", methods=["GET"])
def getRoutes():
    """ getRoutes: this gets all the routes and shows them 
            when you goto "http://localhost:8080/"
    """
    routes = {}
    for r in app.url_map._rules:
        
        routes[r.rule] = {}
        routes[r.rule]["functionName"] = r.endpoint
        routes[r.rule]["help"] = formatHelp(r.endpoint)
        routes[r.rule]["methods"] = list(r.methods)

    routes.pop("/static/<path:filename>")
    routes.pop("/")

    response = json.dumps(routes,indent=4,sort_keys=True)
    response = response.replace("\n","<br>")
    return "<pre>"+response+"</pre>"


@app.route('/hello/<string:name>/<string:adj>')
def hello_name(name,adj):
    """ Route: hello
        Description: 
            simply says hello to a variable passed in using the 
            flask method of param passing. I altered this method 
            to need 2 params.
        Params:
            name <string> : someones name 
            adj  <string> : descriptive word
        
        Example
            http://localhost:8080/hello/Bob/heck

    """
    return f"Hello, <b>{name}</b> how in the {adj} are you!!"
    
@app.route('/frequency')
def frequency():
    """ Route: frequency
        Description: 
            gets you the frequency for a given letter by reading
            in a json file with the frequencies and then accessing the 
            actual frequency using the letter as a key.
        Params:
            letter <string> : lowercase letter of alaphabet
        Example: 
            http://localhost:8080/frequency?letter=e

    """
    # Open the json file with frequencits in it as an 
    # example data source for one of our routes.
    with open('avg_english_freq.json') as f:
        fdata = json.loads(f.read())

    # check if "key" called letter passed on URL
    letter = request.args.get('letter',None)

    # if no letter send back an error
    if not letter:
        result = {"error":"nothing there"}
    else:
        # get the frequency
        result =  {"letter":letter,"frequency":fdata[letter]}

    return handle_response(result,request.args)


@app.route('/public_key/<string:id>')
def public_key(id):
    """ public_key
        Description: gets you the public key
    """

    # os.path.join joins string segments to make a directory path
    key_path = os.path.join('keys',id+'.public.pem')

    # os.path.isfile returns true if file exists
    if os.path.isfile(key_path): 
        # open and read key
        with open(os.path.join('keys',id+'.public.pem')) as f:
            key = f.read() 
        
        return handle_response({"public_key":key},{"id":id})
    
@app.route('/message', methods = ['GET', 'POST', 'DELETE'])
def message_handler():
    """ public_key
        Description: receives messages
    """
    print(request.method)
    print(request.json)

    with open("messages.txt","w") as f:
        f.write(json.dumps(request.json))

    return request.json

@app.route('/servername', methods = ['GET', 'POST', 'DELETE'])
def servername():
    """ public_key
        Description: receives messages
    """

    return handle_response({"name":"server_01"})

#   __  __ ___ ____   ____    _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#  |  \/  |_ _/ ___| / ___|  |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#  | |\/| || |\___ \| |      | |_  | | | |  \| | |     | |  | | | | |  \| \___ \ 
#  | |  | || | ___) | |___   |  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |
#  |_|  |_|___|____/ \____|  |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 

def load_public_keys(path):
    """ This reads a directory (path) for .pem files
        and returns a list with file names in it. Not really
        used (just as an example glob).
    """
 
    key_files = glob.glob(f"{path}/*.pem")

    return key_files

def formatHelp(route):
    """ formatHelp
        Description: 
            Grabs the __doc__ string for the given route (function)
            if it exists and returns it or it returns "no help provided"
        Params:
            route <string> : the function name within this file.
                e.g. formatHelp(frequency) # notice no quotes 
    """
    help = globals().get(str(route)).__doc__
    if help != None:
        help = help.split("\n")
        clean_help = []
        for i in range(len(help)):
            help[i] = help[i].rstrip()
            if len(help[i]) > 0:
                clean_help.append(help[i])
    else:
        clean_help = "No Help Provided."
    return clean_help

#   ____  _____ ____  ____   ___  _   _ ____  _____ 
#  |  _ \| ____/ ___||  _ \ / _ \| \ | / ___|| ____|
#  | |_) |  _| \___ \| |_) | | | |  \| \___ \|  _|  
#  |  _ <| |___ ___) |  __/| |_| | |\  |___) | |___ 
#  |_| \_\_____|____/|_|    \___/|_| \_|____/|_____|
                                                  

def handle_response(data,params=None,error=None):
    """ handle_response
    """
    success = True
    if data:
        if not isinstance(data,list):
            data = [data]
        count = len(data)
    else:
        count = 0
        error = "Data variable is empty!"

    
    result = {"success":success,"count":count,"results":data,"params":params}

    if error:
        success = False
        result['error'] = error
    
    
    return jsonify(result)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Error: need a port number")
        sys.exit()


    app.run(host='0.0.0.0', port=int(sys.argv[1]),debug=True)
      