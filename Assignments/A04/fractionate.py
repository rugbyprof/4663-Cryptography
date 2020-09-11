"""
    This file uses the 2nd key2word to take an existing message that was encoded
    using the first polybius square and performs the "columnar transposition" 
    thereby fractionating the message. 
"""
import math

def print_matrix(matrix,rows):
    """ Print the matrix so we can visually confirm that our
        columnar transposition is actually working
    """
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")


def print_message(matrix,key2word):
    """ Prints the message in a left to right fashion, but reads it from
        the matrix by using fractionated matrix. If you think about it
        we don't even need to swap the columns around, if we alphabatize
        the key2word, then use the alphabetized letters to access the 
        matrix. 
    """
    i = 1
    for k in sorted(key2word):
        for d in matrix[k]:

            print(d,end='')

            # the spaces between every two letters is only for appearance
            if i % 2 == 0:
                print(' ',end='')
            i += 1
    print("")



# key2 = "bugsy".upper()
# message = "DF FF AA DG GF GA DA GF DA AD FX DD GX AG XA XX DD FF AF FA XA"

# key2 = "quark".upper()
# message = "DF FF AA DG GF GA DA GF DA AD FX DD GX AG"


key2 = 'quark'.upper()
message = "XD AA AD DF XD XD DF FD GA FX XA DF XD DD DF AX GF"

message = message.replace(' ','')   # get rid of spaces

# get sizes to help calculate matrix column lengths
key2_length = len(key2)             # length of key
message_length = len(message)       # message length 

# figure out the rows and how many short columns
rows = math.ceil(float(message_length)/float(key2_length))
short_cols = key2_length - (message_length%key2_length)

# dictionary for our new matrix
matrix = {}

# every letter is a key that points to a list
for k in key2:
    matrix[k] = []

# add the message to the each list in a row-wise fashion
# meaning DFFDGAFXXA gets loaded like:
# 
#           QUARK
#           -----
#           DFFDG
#           AFXXA
i = 0
for m in message:
    matrix[key2[i]].append(m)
    i += 1
    i = i % len(key2)


print_matrix(matrix,rows)

# Alphabetize the matrix (not really necessary) if you just
# alphabetize the key2 word and use it to access the dictionary
# in alphabetical order instead. BUT this does stick to the 
# algorithm
temp_matrix = sorted(matrix.items())


print("")

sorted_matrix = {}

# Rebuild the sorted matrix into a dictionary again
# Rememnber sorted returns a list of tuples and we 
# need to make another dictionary. This is another 
# reason NOT to sort the matrix, but simply access
# it via an alphabetized word.
for item in temp_matrix:
    sorted_matrix[item[0]] = item[1]

# Print the matrix for visual confirmation
# not necessary for the encryption process
print_matrix(sorted_matrix,rows)

print("")

# Print the message using the sorted unnecessary matrix
print_message(sorted_matrix,key2)

# print message with original matrix to show we get the same output!
print_message(matrix,key2)
