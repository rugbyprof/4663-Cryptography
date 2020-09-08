## Python - Starter Skeleton
#### Due: None


This is a starter file for projects. This starter gives you the tools necessary to process command line arguments when running your python programs. Passing in arguments at the time your program is called, is preferred over other alternatives like hard coding values or prompting the user.

### Preferred Method

```bash
python caesar_cipher.py input_file="plaintext.txt" output_file="encrypted.txt" method=encrypting shift_value=5
```
### Not Good 

```python

input_file="plaintext.txt"  # what if I want to run a different file? Change source code I guess.
output_file="encrypted.txt" # wait, what if I'm decrypting? Create another variable "output_decrypt_file" and then 
                            # we can add more variables like "input_cipher_text" or "output_plaintext" etc etc etc.
method="encrypting"         # to decrypt: edit file and change this line! Also rename all your variables for in and 
                            # out files so they make sense. 
shift_value=3               # you see the point yet?
```

### Worst Method

```txt

python caesar_cipher.py

What is the name of your input file: (enter text here)
What is the name of your output file: (again type stuff here)
Enter 1=encrypting 2=decrypting: (dear lord are we in CS 1?)
What is your shift value? (shoot me now cause I have to run this 30 more times for testing)
```



### Files

|   #   | File                       | Description                         |
| :---: | -------------------------- | ----------------------------------- |
|   1   | [skeleton.py](skeleton.py) | A python starter file for projects. |