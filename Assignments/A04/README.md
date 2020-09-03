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
  - If we divide `28 / 6` we get `4.666`. This means the *columnar transposition matrix* would have 5 rows for at least "some" of the columns.
    - `4rows * 6cols = 24` not enough to complete the `28` letters.
    - `5rows * 6cols = 30` too many for the the `28` letters. 
    - So, we know its between `4` and `5` rows (aka: not a perfectly filled matrix).
    - This means some columns will be 4 rows, and some 5 rows, where the ones with 5 rows are the first X columns in the original keyword before alphabetizing. 


- For keyword: Quark
  - We know that the keyword had a length of 5. The number of letters in the message was 28.
  - If we divide `28 / 5` we get `5.6`. This means the *columnar transposition matrix* would have 6 rows for at least "some" of the columns.
    - `5rows * 5cols = 25` not enough to complete the `28` letters.
    - `6rows * 5cols = 30` too many for the the `28` letters. 
    - So, we know its between `5` and `6` rows (aka: not a perfectly filled matrix).
    - This means some columns will be 5 rows, and some 6 rows, where the ones with 6 rows are the first X columns in the original keyword before alphabetizing. 


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



<sup>Source: http://practicalcryptography.com/ciphers/adfgx-cipher/</sup>