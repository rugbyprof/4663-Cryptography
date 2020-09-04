## Assignment 4 - ADFGX Implementation
#### Due: 09-11-2020 (Friday @ 5:00 p.m.)

# Almost Done ... 

- Needs deliverables
- And clarification on decrypting


### ADFGX Cipher
 
The ADFGX cipher was a field cipher used by the German Army during World War I. It is closely related to the ADFGVX cipher. ADFGX is a fractionating transposition cipher which combined a modified Polybius square with a single columnar transposition. The cipher is named after the five possible letters used in the ciphertext: A, D, F, G and X. These letters were chosen deliberately because they sound very different from each other when transmitted via morse code. The intention was to reduce the possibility of operator error.

### Building The Polybius Square

- The first step in encoding a message with ADFGX is by creating the modified `Polybius` square. 
- You first choose a "keyword" and write it as if it were in a 5x5 matrix (we'll call this keyword<sub>**1**</sub>).
- If our keyword were **superbad**, our 5x5 would be started like this:

```txt

 s u p e r 
 b a d 
 
```

We then fill in the remaining letters in the alphabet (except `j`) to complete the 5x5 square. 

```txt

 s u p e r 
 b a d c f 
 g h i k l 
 m n o q t 
 v w x y z
```

Once we have the "key square" built, we can then add the corresponding "keys" (the letters ADFGX for which the cipher is named) at the beginning and top of every row and column. We now have a complete modified **polybius** square. By using a "keyword" to build the square, we can avoid transmitting the entire square to the receiver, and the message receiver can
simply build it themselves using their knowledge of keyword<sub>**1**</sub>.

```txt
  A D F G X 
A s u p e r 
D b a d c f 
F g h i k l 
G m n o q t 
X v w x y z 
```

### Using the Polybius Square

The **polybius** square works by locating the letter in the matrix, then pulling out the letter at the beginning of the row, and the letter at the top of the column. For example, if you wanted to encode `nerd`:

**n = GD**
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/polybius_sqaure_1_2020_n.png" width="900">

**e = AG**
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/polybius_sqaure_1_2020_e.png" width="900">

**r = AX**
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/polybius_sqaure_1_2020_r.png" width="900">

**d = DF**
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/polybius_sqaure_1_2020_d.png" width="900">

So, `nerd` => `GD AG AX DF`


### The Algorithm

Ok, we know how to build our **polybius** square and use it to encode a word. But, were just getting started! There are a couple of steps that are involved in this whole ADFGX world-wind tour of encryption. So lets do this!

- We have already chosen keyword<sub>**1**</sub> to build the square with.
- We built the square.
- We can encrypt a message with said polybius square (essentially doubling the text length).

For the next steps, let us assume we are going to encrypt a single word: **discombobulate** (meaning: to confuse someone). This word gets encrypted to: 

```
DF FF AA DG GF GA DA GF DA AD FX DD GX AG
```

- Choose yet another keyword (that does not have duplicate letters) (we'll call this keyword<sub>**2**</sub>).
- Write your encoded message below keyword<sub>**2**</sub> as if each letter of keyword<sub>**2**</sub> is a column header. 
- Lets say our keyword<sub>**2**</sub> is: **hijack** (I will capitalize for readability).

```
6 letter key      5 letter key

H I J A C K       Q U A R K 
- - - - - -       - - - - - 
D F F F A A       D F F F A 
D G G F G A       A D G G F
D A G F D A       G A D A G
A D F X D D       F D A A D
G X A G           F X D D G
                  X A G
```

Perform a columnar transposition. Sort the code word alphabetically, moving the columns as you go. Note that the letter pairs that make up each letter get split apart during this step, this is called **fractionating**.

```
A C H I J K      A K Q R U
- - - - - -      - - - - - 
F A D F F A      F A D F F
F G D G G A      G F A G D
F D D A G A      D G G A A
X D A D F D      A D F A D
G   G X A        D G F D X 
                 G   X   A
```

Read the final ciphertext off in columns to get the message that will be sent: 

```
Hijack: FF FX GA GD DD DD AG FG AD XF GG FA AA AD 
Quark:  FD GA DG AF GD GD AG FF XF GA AD FD AD XA
```

### Decrypting

To decrypt the message sent using our `ADFGX` cipher, we "simply" (LOL) reverse the steps. Of course the receiver needs keyword<sub>**1**</sub> and keyword<sub>**2**</sub> so they can build the modified Polybius square. But also piece together the message that they received. 

- For keyword: Hijack
  - We know that the keyword had a length of 6. The number of letters in the message was 28.
  - Based on the keyword length, and message size, were sure that the *columnar transposition matrix* and would have 5 rows for at least "some" of the columns.


- For keyword: Quark
  - We know that the keyword had a length of 5. The number of letters in the message was 28.
  - Based on the keyword length, and message size, were sure that the *columnar transposition matrix* and would have 6 rows for at least "some" of the columns.


- As long as we know keyword<sub>**2**</sub>, we can deduce what the original matrix should look like (😂 no ... seriously).

- 6 * 5 = 30
- 30 - 28 = 2
- So, 2 of the 6 columns will be short.
- Which 2? C and K because they are the last 2 letters in Hijack

```
A C H I J K
- - - - - - 
5 4 5 5 5 4
```

- 5 cols * 6 rows = 30
- 30 - 28 = 2
- So, 2 of the 5 columns will be short.
- Which 2? R and K because they are the last 2 letters in Quark

```
A K Q R U
- - - - - 
6 5 6 5 6
```

### Helper Code

- I know helper code isn't always helpful! It takes time to figure out what another brain is doing. 
- So I tried to comment the class with decent comments. 
- Usage of the [python class](polybius.py) you can see below.
- This snippet, builds the initial lookup table needed to do the first round of encoding.  

```python
# Create an instance of the class using a super long keyword
# with duplicate letters. The class removes those duplicates
# and then builds the matrix. 
B = AdfgxLookup('helloworldhowareyou')

# build my lookup table 
lookup = B.build_polybius_lookup()

# print out my adfgx lookup table
pp.pprint(lookup)

# print out the actual matrix I 
# know I'm not insane!
B.sanity_check()
```

The **sanity_check** is to print out the created substitution matrix. I need to "see" it working. But it's only to visualize the matrix.

```txt
  A D F G X 
A h e l o w 
D r d a y u 
F b c f g i 
G k m n p q 
X s t v x z 
```

The lookup table is what you use to start the encryption process. 

```python
{'a': 'DF',
 'b': 'FA',
 'c': 'FD',
 'd': 'DD',
 'e': 'AD',
 'f': 'FF',
 'g': 'FG',
 'h': 'AA',
 'i': 'FX',
 'k': 'GA',
 'l': 'AF',
 'm': 'GD',
 'n': 'GF',
 'o': 'AG',
 'p': 'GG',
 'q': 'GX',
 'r': 'DA',
 's': 'XA',
 't': 'XD',
 'u': 'DX',
 'v': 'XF',
 'w': 'AX',
 'x': 'XG',
 'y': 'DG',
 'z': 'XX'}
 ```
Using the lookup table from above: 

```python
message = "theattackisatdawn"
for x in message:
    print(lookup[x],end=' ')
```
Results in:

```
XD AA AD DF XD XD DF FD GA FX XA DF XD DD DF AX GF
```

### Requirements

- You are responsible for everything after the first round of encoding. 
- You can use ALL the code I put in this folder ... or NONE its up to you.
- Ultimately write a program (in language of choice) that implements the steps described in this document to implement the `ADFGX` cipher.
- Your program should include functions that implement various components of the cipher to encrypt and decrypt.
- Key components are building the *columnar transposition matrix*:
```
H I J A C K       Q U A R K 
- - - - - -       - - - - - 
D F F F A A       D F F F A 
D G G F G A       A D G G F
D A G F D A       G A D A G
A D F X D D       F D A A D
G X A G           F X D D G
                  X A G
```
- As well as **fractionating** it (cool word):
```
A C H I J K      A K Q R U
- - - - - -      - - - - - 
F A D F F A      F A D F F
F G D G G A      G F A G D
F D D A G A      D G G A A
X D A D F D      A D F A D
G   G X A        D G F D X 
                 G   X   A
```
- Having the ability to traversing the  **fractionated** matrix in a column-wise fashion to build the actual encrypted message.
- FINALLY: reverse it all to decipher a message.

### Running your program

- Your program should be invoked like the following:

```
                     1              2        3            4
python adfgx.py input_file_name keyword1 keyword2 [encrypt,decrypt] 
```

1. The file to be encrypted or decrypted
2. keyword to build adfgx matrix 
3. keyword used with transposition matrix and fractionating the message
4. whether to "encrypt" or "decrypt" the message.

- To test your program we will run it in class and attempt to encrypt and then decrypt a message. 
- The big test is if you can decrypt a file not encrypted by your own program.

### Deliverables

- Make sure you have an "assignments" folder on your Github repo.
- Create a folder called `A04` and place all files (source code or text) that were used in the decrypting of these messages.
- Follow the guidelines of [this](../../Resources/02-Readmees/README.md) to help you write a README.md for your assignment. (10% of grade).
- Include any and all files used to complete this project. 
- Your main program should be named `adfgx.py`
- The README.md is for you to assist anyone with necessary libraries and or the running of your program. 
- Any sources used should be in the description as well as a link to every file. 
- Examples of input and output would be helpful as well.


<sup>Source: http://practicalcryptography.com/ciphers/adfgx-cipher/</sup>