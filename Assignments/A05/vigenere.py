import sys
import sys
import os
import pprint

ALPHABET = [chr(x+97) for x in range(26)]

def vigenere_cipher_encrypt(**kwargs):
    input_file = kwargs.get('input',None)
    output_file = kwargs.get('output',None)
    key = kwargs.get('key',None)

    # should test if file exists
    with open(input_file) as f:
        plaintext = f.read()

    plaintext = plaintext.lower()
    ciphertext = ''

    i = 0
    for letter in plaintext:
        if letter in ALPHABET:

            a = ord(letter)-97
            b = ord(key[i])-97
            ciphertext += chr(((a+b)%26)+97)

            i = (i + 1) % len(key)
        else:
            ciphertext += letter

    with open(output_file,'w') as f:
        f.write(ciphertext)

def vigenere_cipher_decrypt(**kwargs):
    input_file = kwargs.get('input',None)
    output_file = kwargs.get('output',None)
    key = kwargs.get('key',None)


    # should test if file exists
    with open(input_file) as f:
        ciphertext = f.read()

    decrypted = ''
    i = 0
    for letter in ciphertext:
        if letter in ALPHABET:
            a = ord(letter)-97
            b = ord(key[i])-97
            decrypted += chr(((a-b)%26)+97)

            i = (i + 1) % len(key)
        else:
            decrypted += letter

    with open(output_file,'w') as f:
        f.write(decrypted)


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


def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=input_file.txt output=output_file.txt key=machine op=encrypt\n")
    sys.exit()

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 4 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    outfile = params.get('output',None)
    key = params.get('key',None)

    if not operation and not infile and not outfile and not key:
        usage()

    if operation.lower() == 'encrypt':
        vigenere_cipher_encrypt(**params)
    elif operation.lower() == 'decrypt':
        vigenere_cipher_decrypt(**params)
    else:
        usage()