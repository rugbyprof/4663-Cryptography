from random import shuffle
from random import randint

# list of letters
alphabet = [chr(x+97) for x in range(26)]

#list of letters to substitute
subs = [chr(x+97) for x in range(26)]

# shuffle (randomize) our list between 5 and 25 times
ns = randint(5,25)
print(ns)
for i in range(ns):
    shuffle(subs)

# print the list of substitution letters out
print(subs)

# here is where you would put your plain text
plaintext = "".lower()

# here is where you would write to the out file
f = open("ciphertext.txt","w")

# performs the substitution
for p in plaintext:
    i = ord(p)-97
    if p in alphabet:
        i = ord(p)-97
        f.write(subs[i])
    else:
        f.write(p)
