from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def generate_key():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        key_generation_obj = KeyGenerationApi(details_dict1)
        # Setting the json message body
        key_generation = GeneratePublicKeyRequest(encryption_type = "None")
        message_body = json.dumps(key_generation.__dict__)
        return_data, status, body = key_generation_obj.generate_public_key(generate_public_key_request=message_body)
        print("API RESPONSE CODE : ",status)
        print("API RESPONSE BODY : ",body)
    except Exception as e:
        print("Exception when calling KeyGenerationApi->generate_public_key: %s\n" % e)


if __name__ == "__main__":
    generate_key()
