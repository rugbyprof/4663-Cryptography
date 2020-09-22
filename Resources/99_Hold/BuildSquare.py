import sys
import os
import pprint

from mymodule.CmdParams import cmd_params
from mymodule.Usage import usage
from mymodule.RemoveDups import remove_dups

alphabet = [chr(x+97) for x in range(26)]

def build_square(key):
    key = key.replace(' ','')
    key = remove_dups(key)
    print(key)

    square = []
    i = 
    for row in range(5):
        square.append([])
        for col in range(5):
            square[row][col] = None


if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 1 # adjust accordingly

    # get processed command line arguments 
    _,params = cmd_params(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    key = params.get('key',None)

    if not key:
        usage()

    build_square(key)