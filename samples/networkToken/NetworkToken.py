import os
from importlib.machinery import SourceFileLoader

from CyberSource.utilities.JWEResponse.JWEUtility import JWEUtility
from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration

from create_instrument_identifier_card_enroll_for_network_token import \
    create_instrument_identifier_card_enroll_for_network_token
from payment_credentials_from_network_token import payment_credentials_from_network_token

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def network_token():
    config_obj = configuration.Configuration()
    client_config = config_obj.get_configuration()
    merchant_config = MerchantConfiguration()
    merchant_config.set_merchantconfig(client_config)
    try:
        #Step-I
        instrument_identifier_for_network_token = create_instrument_identifier_card_enroll_for_network_token()
        token_id = instrument_identifier_for_network_token.id

        #Step-II
        encoded_response = payment_credentials_from_network_token(token_id)

        #Step-III
        decoded_response = JWEUtility.decrypt_jwe_response(encoded_response, merchant_config)

        print("Decoded Response")
        print(decoded_response)

    except Exception as e:
        print("\nException when running the sample code of networkToken: %s\n" % e)

if __name__ == "__main__":
    network_token()
