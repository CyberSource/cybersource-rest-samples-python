import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

from CyberSource import TokenApi
from create_instrument_identifier_card_enroll_for_network_token import create_instrument_identifier_card_enroll_for_network_token

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


def payment_credentials_from_network_token(token_id=None):
    profile_id = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    if token_id is None:
        token_id = create_instrument_identifier_card_enroll_for_network_token().id

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TokenApi(client_config)
        return_data, status, body = api_instance.post_token_payment_credentials(token_id, profile_id=profile_id)
        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling TokenAPI->payment-credentials API: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    payment_credentials_from_network_token()
