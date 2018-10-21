from cybersource_rest_client_python import *
import json


def keygeneration_noenc():
    try:
        key_generation_obj = KeyGenerationApi()
        #key_generation = KeyParameters()
        key_generation = GeneratePublicKeyRequest()
        key_generation.encryption_type = "None"

        message_body = json.dumps(key_generation.__dict__)
        return key_generation_obj.generate_public_key(message_body)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    keygeneration_noenc()
