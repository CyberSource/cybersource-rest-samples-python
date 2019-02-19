from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# Following code is to handle the Sibling Package Import
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "coreservices"
import keygeneration_noenc
import flex_signature_verification


def tokenize_card():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        tokenize_card = TokenizeRequest()
        card_info = Flexv1tokensCardInfo()
        # Getting the key_id dynamically
        api_response = keygeneration_noenc.keygeneration_noenc()
        tokenize_card.key_id = api_response['keyId']

        card_info.card_expiration_year = "2031"
        card_info.card_number = "5555555555554444"
        card_info.card_type = "002"
        card_info.card_expiration_month = "03"
        tokenize_card.card_info = card_info.__dict__
        message_body = json.dumps(tokenize_card.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        tokenize_obj = FlexTokenApi(details_dict1)
        # Calling api_client variable in Configuration file 
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = tokenize_obj.tokenize(tokenize_request=message_body)
        # Calling api_client variable in Configuration file to access the request_headers
        request_headers = config.api_client.request_headers

        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

        flex_signature_verification.verify(api_response['der']['publicKey'],json.loads(response_data.data))
    except Exception as e:
        print("\nException when calling FlexTokenApi->tokenize: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    tokenize_card()
