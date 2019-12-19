from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# Following code is to handle the Sibling Package Import
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "coreservices"
import keygeneration_noenc


def tokenize_card():
    try:
        # Setting the json message body
        tokenize_card = TokenizeRequest("None")
        card_info = Flexv1tokensCardInfo("5555555555554444","03","2031","002")
        # Getting the key_id dynamically
        api_response = keygeneration_noenc.keygeneration_noenc()
        print(api_response)
        tokenize_card.key_id = api_response.key_id

        tokenize_card.card_info = card_info.__dict__
        message_body = json.dumps(tokenize_card.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        tokenize_obj = TokenizationApi(details_dict1)
        return_data, status, body = tokenize_obj.tokenize(tokenize_request=message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        token_verifier = TokenVerification()

        is_token_verified = token_verifier.verify_token(api_response.der.public_key, json.loads(body))
        print("Flex Token Verification : ", is_token_verified)

    except Exception as e:
        print("Exception when calling FlexTokenApi->tokenize: %s\n" % e)


if __name__ == "__main__":
    tokenize_card()
