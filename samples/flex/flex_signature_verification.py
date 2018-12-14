import rsa_verify
import Flex_Security_Exception


def verify(key, postparams):
    signed_list = []

    if postparams is None:
        raise Flex_Security_Exception("A valid Dictionary must be supplied")
    signature = postparams.get("signature")
    if signature is None:
        raise Flex_Security_Exception("Missing required field: signature")
    signed_fields = postparams.get("signedFields")
    if signed_fields is None:
        raise Flex_Security_Exception("Missing required field: signedFields")

    signed_field = (signed_fields.split(","))
    #print(signed_field)

    for i in signed_field:
        signed_list.append(",")
        signed_list.append(str(postparams.get("" + i)))

    signed_string = "".join(signed_list)
    signed_string = signed_string[1:]
    #print(signed_string)

    #print("Flex Signature Verification: ",rsa_verify.verify_sign(key, signature, signed_string))
