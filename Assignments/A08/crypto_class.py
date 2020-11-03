#pip install cryptography
import cryptography
# Used to Generate Keys
# from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

#Used to Store Keys and Read in Keys
from cryptography.hazmat.primitives import serialization

#Used to do Encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Crypto:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.file_prefix = 'key'
        self.private_key_file = "key.private.pem"
        self.public_key_file = "key.public.pem"

    def generate_keys(self,exp=65537,ksize=2048):
        """
        public_exponent (int) – The public exponent of the new key. Often 
                        one of the small Fermat primes 3, 5, 17, 257 or 65537.
        key_size (int) – The length in bits of the modulus. Should be at least 2048.
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=exp,
            key_size=ksize
            # backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def store_keys(self):
        # Storing  Private Keys
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(self.private_key_file, 'wb') as f:
            f.write(pem)

        # Storing Public Key
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(self.public_key_file, 'wb') as f:
            f.write(pem)

    def load_keys(self):
        # Reading the Private Key
        with open(self.private_key_file, "rb") as key_file:
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None
                # backend=default_backend()
            )

        # Reading the Public Key
        with open(self.public_key_file, "rb") as key_file:
            self.public_key = serialization.load_pem_public_key(
                key_file.read()
                # backend=default_backend()
            )

    def encrypt(self,plaintext):
        # Encrypting With Public Key

        # make sure the text is "bytes"
        # this is typically shown like this: b'message' (see the b before the quotes?)
        plaintext = str.encode(plaintext)

        encrypted = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    def decrypt(self,encrypted):
        
        # Decrypting Using Private Key
        original_message = self.private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return original_message

if __name__ == '__main__':
    C = Crypto()
    C.generate_keys()
    #C.store_keys()   # write keys to file

    encrypted = C.encrypt('This is my plaintext.')

    decrypted = C.decrypt(encrypted)

    print(decrypted)
