from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64decode

def verify_sign(public_key_loc, signature, data):
    """
    Verifies with a public key from whom the data came that it was indeed
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise.
    """
    pub_key =  b64decode(public_key_loc )

    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA512.new()
    digest.update(data.encode('utf-8'))

    if signer.verify(digest, b64decode(signature)):
        return True
    else:
        return False