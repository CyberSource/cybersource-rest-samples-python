from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

key_generation_path = os.path.join(os.getcwd(), "samples", "Flex", "KeyGeneration", "generate-key.py")
generate_key = SourceFileLoader("module.name", key_generation_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def flex_tokenize_card():
    api_response = generate_key.generate_key()
    keyId = api_response.key_id

    cardInfoCardNumber = "4111111111111111"
    cardInfoCardExpirationMonth = "12"
    cardInfoCardExpirationYear = "2031"
    cardInfoCardType = "001"
    cardInfo = Flexv1tokensCardInfo(
        card_number = cardInfoCardNumber,
        card_expiration_month = cardInfoCardExpirationMonth,
        card_expiration_year = cardInfoCardExpirationYear,
        card_type = cardInfoCardType
    )

    requestObj = TokenizeRequest(
        key_id = keyId,
        card_info = cardInfo.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TokenizationApi(client_config)
        return_data, status, body = api_instance.tokenize(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        token_verifier = TokenVerification()

        is_token_verified = token_verifier.verify_token(api_response.der.public_key, json.loads(body))
        print("Flex Token Verification : ", is_token_verified)

        return return_data
    except Exception as e:
        print("\nException when calling TokenizationApi->tokenize: %s\n" % e)

if __name__ == "__main__":
    flex_tokenize_card()
