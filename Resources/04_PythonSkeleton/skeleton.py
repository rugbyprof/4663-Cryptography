import sys
import os
import pprint

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def main(args,**kwargs):
    """ Example main function. Of course params would change as necessary.
    Params:
        kwargs <dict> : keyword params

    """
    pprint.pprint(args)
    pprint.pprint(kwargs)

def usage(message=None):
    if message:
        print(message)
    print("Usage: python skeleton.py [key1=string] [key2=int] [key3=int] [keyX=sometype]")
    print("Example:\n\t python skeleton.py arg1 arg2 var1='Param 1' path=./some_path a=25 b=50\n")
    sys.exit()

if __name__=='__main__':
    """
    Change the required params value below accordingly.

    """
    required_params = 4 # adjust accordingly
    argv = sys.argv[1:] # strip file name (skeleton.py) out of args

    # print usage if not called correctly
    if len(argv) < required_params:
        usage()

    # get processed command line args
    args,kwargs = mykwargs(argv)

    # you could also check to make sure certain keyword params exist at this point.
    # e.g. 
    # if 'encryption_key' not in kwargs:
    #   usage("Missing param: 'encryption_key'. Cannot continue!")
        

    # command line params are processed

    # do more param processing if necessary

    # or send all to main
    main(args,**kwargs)