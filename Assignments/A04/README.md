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
- We can start the encryption of a message with said polybius square (essentially doubling the text length).

For the next steps, let us assume we are going to encrypt a single word: **discombobulate** (meaning: to confuse someone). This word gets encrypted to: 

```
DF FF AA DG GF GA DA GF DA AD FX DD GX AG
```

- Choose yet another keyword (that does not have duplicate letters) (we'll call this keyword<sub>**2**</sub>).
- Write your encoded message below keyword<sub>**2**</sub> as if each letter of keyword<sub>**2**</sub> is a column header. 
- Add the message to the matrix in a row-wise fashion, meaning the keyword `BUG` would have a message like `DFFDGAFXXA` loaded like the following:
 
```
      B U G
      - - -
      D F F
      D G A
      F X X
      A
```

- Using the message encrypted from discombobulate, here are two different length keyword<sub>**2**</sub>'s loaded.
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

- The next step is to perform a columnar transposition. Sort the code word alphabetically, moving the columns as you go. Note that the letter pairs that make up each letter get split apart during this step, this is called **fractionating**.

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

- Read the final ciphertext off in columns to get the message that will be sent: 

```
Hijack: FF FX GA GD DD DD AG FG AD XF GG FA AA AD 
Quark:  FD GA DG AF GD GD AG FF XF GA AD FD AD XA
```

### Decrypting

To decrypt the message sent using our `ADFGX` cipher, we "simply" (LOL) reverse the steps. Of course the receiver needs keyword<sub>**1**</sub> and keyword<sub>**2**</sub> so they can build the modified Polybius square. But also piece back together the message that they received by reversing the `fractionating` process by:

  - Calculating the number of rows in the matrix based on length of keyword<sub>**2**</sub>.
  - Figuring out the number of short columns.
  - Assigning short columns to proper letters.
  - Alphabetizing the keyword<sub>**2**</sub>.
  - Read message back out from 


### Helper Code

- I know helper code isn't always helpful! It takes time to figure out what another brain is doing. 
- So I tried to comment each file with decent comments. Probably too many for some of you.
- Files: 
  
|   #   | Name                             | Description                                                                                           |
| :---: | :------------------------------- | :---------------------------------------------------------------------------------------------------- |
|   1   | [polybius.py](polybius.py)       | This is a class that builds a polybius lookup table for part 1 of encryption.                         |
|   2   | [fractionate.py](fractionate.py) | Contains function or two that use keyword2 to load another matrix and perform columnar transposition. |


### Requirements

- You are responsible for encrypting a message of size `1 - n` with almost no cap on `n`. We won't go crazy, but assume you may read a file of size many `K`.
- You can use ALL the code I put in this folder ... or NONE its up to you.
- Ultimately write a program (in language of choice) that implements the steps described in this document to implement the `ADFGX` cipher.
- Your program should include functions that implement various components of the cipher to encrypt and decrypt. Basically, organize your code into functions and / or classes.
- Any characters that are not A-Z can be ignored and filtered out. But they need to be handled and should not break your program.
- Use of external libraries is OK as long as you document thier use and as long as you still implement the actual algorithm. (e.g. a library to clean text is ok).
- Key components are:
  - ENCRYPTION (all done for you in pieces):
    - Reading parameters from command line to set up your program.
    - Building the polybius square using keyword<sub>1</sub> (really the dictionary lookup is what it is).
    - Building the *columnar transposition matrix* and fractionating the message using keyword<sub>2</sub>.
    - Pulling the message out of this second matrix and writing it to a file. 
  - DECRYPTION
    - All on you! All the programming tools you need are in this repo.


### Running your program

- This file: [skeleton.py](../../Resources/04_PythonSkeleton/skeleton.py) has helper code to deal with command line parameters.
- Your program should be invoked in one of 2 ways:
  
**Positional Parameters:**
```
                     1              2        3            4
python adfgx.py input_file_name keyword1 keyword2 [encrypt,decrypt] 
```

1. The file to be encrypted or decrypted
2. keyword to build ADFGX matrix (polybius square)
3. keyword used with transposition matrix and fractionating the message
4. whether to "encrypt" or "decrypt" the message.

**Keyword Parameters:**
```
python adfgx.py input=input_file_name key1=keyword1 key2=keyword2 op=[encrypt,decrypt] 
```

- Each key=value pair should be obvious what they are.

**Testing:**

- To test your program we will run it in class and attempt to encrypt and then decrypt a message. 
- The big test is if you can decrypt a file not encrypted by your own program.

### Deliverables

- Make sure you have an "assignments" folder on your Github repo.
- Create a folder called `A04` and place all files (source code or text) that were used in the decrypting of these messages.
- Follow the guidelines of [this](../../Resources/02-Readmees/README.md) to help you write a README.md for your assignment. (10% of grade).
- Include any and all files used to complete this project. 
- Your main program should be named `adfgx.py`
- The `README.md` is for you to assist anyone with necessary libraries and or the running of your program. 
- Any sources used should be in the description as well as a link to every file. 
- Examples of input and output would be helpful as well.


<sup>Source: http://practicalcryptography.com/ciphers/adfgx-cipher/</sup>