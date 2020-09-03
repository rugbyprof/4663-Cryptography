## Assignment 4 - ADFGX Implementation
#### Due: 09-11-2020 (Friday @ 5:00 p.m.)

# NOT DONE!

### ADFGX Cipher
 
The ADFGX cipher was a field cipher used by the German Army during World War I. It is closely related to the ADFGVX cipher. ADFGX is a fractionating transposition cipher which combined a modified Polybius square with a single columnar transposition. The cipher is named after the five possible letters used in the ciphertext: A, D, F, G and X. These letters were chosen deliberately because they sound very different from each other when transmitted via morse code. The intention was to reduce the possibility of operator error.

### The Algorithm 

The 'key' for a ADFGX cipher starts with a 'key square' that is built using a keyword that is placed into a 5x5 matrix like so: 

**keyword: superbad**

```txt

 s u p e r 
 b a d 
 
 
 
```

Then the remaining letters in the alphabet (except `j`) fill out the rest of the 'key square'.

```txt

 s u p e r 
 b a d c f 
 g h i k l 
 m n o q t 
 v w x y z
```

Once we have the "key square" built, we can then add the corresponding "keys" at the beginning of every row and column. We now have a **polybius** square. By using a "keyword" to build the square, we can avoid transmitting the entire square, and the message receiver can
build it themselves using the same keyword.

```txt
  A D F G X 
A s u p e r 
D b a d c f 
F g h i k l 
G m n o q t 
X v w x y z 
```

Encode the plaintext using this matrix, to encode the laetter 'a', locate it in the matrix and read off the letter on the far left side on the same row, followed by the letter at the top in the same column. In this way each plaintext letter is replaced by two cipher text letters. E.g. 'attack' -> 'DD XF XF DD GA FG'. The ciphertext is now twice as long as the original plaintext. Note that so far, it is just a simple substitution cipher, and trivial to break.

Write the code word with the enciphered plaintext underneath e.g.

G E R M A N
D D X F X F
D D G A F G
Perform a columnar transposition. Sort the code word alphabetically, moving the columns as you go. Note that the letter pairs that make up each letter get split apart during this step, this is called fractionating.

A E G M N R
X D D F F X
F D D A G G
Read the final ciphertext off in columns.

-> XF DD DD FA FG XG

<sup>Source: http://practicalcryptography.com/ciphers/adfgx-cipher/</sup>