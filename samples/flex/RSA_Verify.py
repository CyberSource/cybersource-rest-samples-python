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
    pub_key = "-----BEGIN PUBLIC KEY-----\n" + public_key_loc + "\n-----END PUBLIC KEY-----"
    # print(pub_key)

    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    # print(signer)
    digest = SHA512.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(b64decode(data))
    # print(digest)
    if signer.verify(digest, b64decode(signature)):
        return True
    else:
        return False
