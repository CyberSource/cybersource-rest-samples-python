from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def generate_key():
    try:
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        key_generation_obj = KeyGenerationApi(details_dict1)
        # key_generation = KeyParameters()
        key_generation = GeneratePublicKeyRequest()
        key_generation.encryption_type = "RsaOaep256"

        message_body = json.dumps(key_generation.__dict__)
        return_data, status, body =key_generation_obj.generate_public_key(message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    generate_key()
