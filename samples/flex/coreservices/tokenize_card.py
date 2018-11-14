from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.getcwd() + "\\data\\Configuration.py"

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
        tokenize_card = TokenizeRequest()
        card_info = Flexv1tokensCardInfo()
        api_response = keygeneration_noenc.keygeneration_noenc()
        tokenize_card.key_id = api_response.key_id

        card_info.card_expiration_year = "2031"
        card_info.card_number = "5555555555554444"
        card_info.card_type = "002"
        card_info.card_expiration_month = "03"
        tokenize_card.card_info = card_info.__dict__

        message_body = json.dumps(tokenize_card.__dict__)
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        tokenize_obj = FlexTokenApi(details_dict1)
        return_data, status, body = tokenize_obj.tokenize(tokenize_request=message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)






if __name__ == "__main__":
    tokenize_card()
