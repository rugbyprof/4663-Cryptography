## Assignment 8 - Public Key Encryption
#### Due: 11-10-2020 ( Tuesday @ 3:30 p.m.)

### Overview

This project will use an existing python library called [cryptography](https://cryptography.io/en/latest/index.html) (appropriately named) to use public key encryption to encrypt and decrypt messages sent between to clients. The clients will be Flask servers running (for now) locally listening to a specific port for requests. A request really boils down to a function call that will be directed by your Flask app. Typical requests will be:


- Get public key : request clients public key
- Post public key : send public key to requestor 
- 

pip install flask
pip install flask_cors

