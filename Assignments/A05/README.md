## Assignment 5 - Vigenere Cracking
#### Due: 09-29-2020 (Tuesday @ 3:30 p.m.)

<sup>Good Source: http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/</sup>

You will be given 1 or more encrypted files. You know the files were encrypted using the Vigenère method. You also know that the key used is an english dictionary word with a length 2-16 inclusive.

Write a python program that will 1) discover the size of that dictionary word (keylength) and then determine which word was used to encrypt your file(s).

To find the keylength you can use the `Index of Coincidence (I.C.)` described breifly below, but more thoroughly at the link provided.

### Incidence of Coincidence
<sup>Source: http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/</sup>

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/ic.png" width="200">

- Where ***c=26***, 
- ***n***<sub>***i***</sub> is the frequency of each letter, 
- and ***N*** is the length of the text.

### Dictionary Attack

Using the dictionary provided [here](../../Resources/dictionary.json) and your newly discovered keylength, find all words in the dictionary of same length and proceed to brute force your way into decrypting the ciphertext. How will you know when you have achieved your decryption? Maybe this will help: https://www.python-course.eu/naive_bayes_classifier_introduction.php. You don't 
have to use the bayes classifier but it will make life easier. You could simply write your own probability function that assigns a value between 0,1 based on how many words you find in the dictionary .... expensive!

### Requirements

- You will be given one or more file(s) with an encrypted message in the file. 
- Process each file and:
  - print the key-length first
  - print the keyword when found
  - print the first 50 words of the message after decryption
- You must run your program like the following:

```
python break_vig.py input_file=input 
```

**Example OutPut**
```
Name: First Last

Keylength: 7
Keyword:   bruiser
Decrypted Text:

For score and seven years ago, there was an extremely cool dude with an awesome hat. Etc. Etc.
```


### Deliverables

- Create a folder called `A05` in assignments folder and place all files (source code or text) that were used.
- Follow the guidelines of [this](../../Resources/02-Readmees/README.md) to help you write a README.md for your assignment. (10% of grade).
- Include any and all files used to complete this project. 
- Your main program should be named `break_vig.py`
- The `README.md` is for you to assist anyone with necessary libraries and or the running of your program. 
- Any sources used should be in the description as well as a link to every file. 
- Examples of input and output would be helpful as well.


