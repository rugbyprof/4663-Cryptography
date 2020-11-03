#!/Users/griffin/.pyenv/shims/python
import os
import sys
import json

from flask import Flask,  url_for
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import send_file

from misc_functions import haversine, bearing

app = Flask(__name__)
CORS(app)

data = open("../../Data/color.names.json",'r').read()
COLORS = json.loads(data)

"""
   ____    _  _____  _    
  |  _ \  / \|_   _|/ \   
  | | | |/ _ \ | | / _ \  
  | |_| / ___ \| |/ ___ \ 
  |____/_/   \_\_/_/   \_\
"""



"""
   ____   ___  _   _ _____ _____ ____  
  |  _ \ / _ \| | | |_   _| ____/ ___| 
  | |_) | | | | | | | | | |  _| \___ \ 
  |  _ <| |_| | |_| | | | | |___ ___) |
  |_| \_\\___/ \___/  |_| |_____|____/ 
"""

@app.route("/token", methods=["GET"])
def getToken():
    """ getToken: this gets mapbox token
    """
    token = {'token':'pk.eyJ1IjoicnVnYnlwcm9mIiwiYSI6ImNpZ3M1aDZwbzAyMnF1c20xcnM4ZGowYWQifQ.s6ghscOu98he230FV1_72w'}

    return token

@app.route("/", methods=["GET"])
def getRoutes():
    """ getRoutes: this gets all the routes!
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

@app.route('/image/<string:filename>')
def get_image(filename):
    """ Description: Return an image for display
        Params: 
            name (string)  : name of image to return
        Example: http://localhost:8080/image/battle_ship_1.png
    """

    image_dir= "./images/"

    image_path = os.path.join(image_dir,filename)

    if not os.path.isfile(image_path):
        return handle_response([],{'filename':filename,'imagepath':image_path},"Error: file did not exist!")

    return send_file(image_path, mimetype='image/png')

@app.route('/geo/direction/')
def get_direction():
    """ Description: Return the direction between two lat/lon points.
        Params: 
            lng1 (float) : point 1 lng
            lat1 (float) : point 1 lat
            lng2 (float) : point 1 lat
            lat2 (float) : point 1 lat

        Example: http://localhost:8080/geo/direction/?lng1=-98.4035194716&lat1=33.934640760&lng2=-98.245591004&lat2=34.0132220288
    """
    lng1 = request.args.get('lng1',None)
    lat1 = request.args.get('lat1',None)
    lng2 = request.args.get('lng2',None)
    lat2 = request.args.get('lat2',None)

    b = bearing((float(lng1),float(lat1)), (float(lng2),float(lat2)))

    return handle_response([{"bearing":b}],{'lat1':lat1,'lng1':lng1,'lat2':lat2,'lng2':lng2})


"""
  ____  ____   ___      _ _____ ____ _____
 |  _ \|  _ \ / _ \    | | ____/ ___|_   _|
 | |_) | |_) | | | |_  | |  _|| |     | |
 |  __/|  _ <| |_| | |_| | |__| |___  | |
 |_|   |_| \_\\___/ \___/|_____\____| |_|

"""

@app.route('/color/hex/<string:name>', methods=["GET"])
def rgb(name):
    """ Description: return hex value for a color
        Params: 
            name (string) : color name
        Example: http://localhost:8080/color/hex/blue
    """
    data = []

    for color in COLORS:
        if color["name"] == name:
            data = color["hex"]

    return handle_response(data)

@app.route('/menu', methods=["GET"])
def menu():
    """ Description: return menu for front end
        Params: 
            None
        Example: http://localhost:8080/menu
    """
    data = open('menu.json','r').read()

    data = json.loads(data)

    return handle_response(data)

"""
   ____  ____  _____     ___  _____ _____ 
  |  _ \|  _ \|_ _\ \   / / \|_   _| ____|
  | |_) | |_) || | \ \ / / _ \ | | |  _|  
  |  __/|  _ < | |  \ V / ___ \| | | |___ 
  |_|   |_| \_\___|  \_/_/   \_\_| |_____|
"""

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

def formatHelp(route):
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

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080,debug=True)
      
