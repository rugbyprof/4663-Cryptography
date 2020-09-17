import sys
import os
import pprint

from mymodule.CmdParams import cmd_params
from mymodule.Usage import usage

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

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 4 # adjust accordingly

    # get processed command line arguments 
    _,params = cmd_params(sys.argv[1:])

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