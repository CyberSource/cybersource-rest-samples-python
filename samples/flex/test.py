from samples.flex.Flex_Security_Exception import *
import samples.flex.RSA_Verify


def verify(key, postparams):
    signed_list = []

    if postparams is None:
        raise FlexSecurityException("A valid Dictionary must be supplied")
    signature = postparams.get("signature")
    if signature is None:
        raise FlexSecurityException("Missing required field: signature")
    signedFields = postparams.get("signedFields")
    if signedFields is None:
        raise FlexSecurityException("Missing required field: signedFields")

    signed_field = (signedFields.split(","))

    for i in signed_field:
        signed_list.append(",")
        signed_list.append(str(postparams.get("" + i)))

    signed_string = "".join(signed_list)
    signed_string = signed_string[1:]

    print(samples.flex.RSA_Verify.verify_sign(key, signature, signed_string))


if __name__ == "__main__":
    try:
        key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqkweEHkg6fl5+XvjSBxh48SPWxR2u8TZ7+T0l8CG6PUC6F9XysPWVRJKEHyqXSqc4tLfY39eIl7nPR/a+e2HSqn+fGsR2LRwBkoMbTqnC/L0BICpbbtdk6i3m3iMrnrDvgOZhBbAhoP9zBGmFga8wb1HD4ZikY5N7l/IT17L+etqQ9QRMuclm/kXiboGvunSXVwrpm2o3I1KJkrDXwYwEj/BZDlAWQiud6DApXOnl1AMpAV+wfYQjlS+GRgOehC58eNcwsonyuLp6NsuCbqmkSwZT9SBU1zAbFAdL1E+fPpEJs4NIvFnLiA6tnOLdczvxbT5q6YPGjucJMW1qh2pBwIDAQAB"
        public_key="-----BEGIN PUBLIC KEY-----\n"+key+"\n-----END PUBLIC KEY-----"
        postparams ={"keyId":"073mAPQxysmv277FH9HvrKNOeziUcheF","token":"77F010242896BF86E05341588E0A1A95","maskedPan":"555555XXXXXX4444","cardType":"002","timestamp":1539244019692,"signedFields":"token,cardType,maskedPan,timestamp","signature":"bzsrLT5FLlhaLgRNIogP/QPyKwNKNIXRB9GoZ2ZwkTAoC4D14SfuoGyuQOqRofPr2hP6lLJcG4/G6cgNbuGXMkTSeTUpK1ruLqR/998897YGl9qHojEiJigrKd8KC2QBxVgMyoGx4SaUw6HiPM83omZDXUXsc/Wo7r5yUNGmb6P4CdsFxbbBCrei/NFE8RnjTuoD4AVye3xqPf4qB663+kg3KEKVxi6jIXPbtMivJ9AY03dM0LhjkDHzovZWd54/hszwP6kJ09V2A0QYjzMZKsWZt0m0t4/33WIskPR2mCvSgaO71qGHXGrK//qYqB9oCEAEQ8NR4I3Z8nRh3perWA==","discoverableServices":{},"_embedded":{"icsReply":{"requestId":"5392440193856785703001","instrumentIdentifier":{"id":"7020000000002394444","new":"N","state":"ACTIVE"},"_links":{"self":{"href":"/cybersource/flex/search/v1/logs/tokenProvider/5392440193856785703001"}}}}}
        verify(public_key, postparams)
    except FlexSecurityException as e:
        print(e)
