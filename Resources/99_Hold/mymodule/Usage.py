import os,sys

def usage(message=None):
    if message:
        print(message)
    #name = os.path.basename(__file__)
    print(f"Usage: python filename.py [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python filename.py input=input_file.txt output=output_file.txt key=machine op=encrypt\n")
    sys.exit()