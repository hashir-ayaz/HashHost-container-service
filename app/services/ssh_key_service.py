from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os


def generate_private_key():
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,  
    backend=default_backend()
    )
    # Serialize the private key in PEM format
    pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # Use BestAvailableEncryption(b'mypassword') for an encrypted key
    )
    
    return pem_private, private_key

def generate_public_key(private_key):
    # generate public key from the private key
    public_key = private_key.public_key()
    
    # serialize the public key in OpenSSH format
    pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.OpenSSH,
    format=serialization.PublicFormat.OpenSSH
    )
    
    return pem_public
    
def save_keys_to_files(private_key, public_key):
    DIRECTORY = '~/hashhost/ssh_keys'
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Save the private key to a file
    with open('', 'wb') as f:
        f.write(private_key)
        
    # Save the public key to a file
    with open('public_key.pub', 'wb') as f:
        f.write(public_key)
        
    return True