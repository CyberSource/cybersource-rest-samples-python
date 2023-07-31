import json
import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

from CyberSource import Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierCard, \
    PostInstrumentIdentifierRequest, InstrumentIdentifierApi
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


def create_instrument_identifier_card_enroll_for_network_token():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    type = "enrollable card"
    cardNumber = "5204245750003216"
    cardExpirationMonth = "12"
    cardExpirationYear = "2025"
    card = Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierCard(
        number=cardNumber,
        expiration_month=cardExpirationMonth,
        expiration_year=cardExpirationYear
    )

    requestObj = PostInstrumentIdentifierRequest(
        type=type,
        card=card.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InstrumentIdentifierApi(client_config)
        return_data, status, body = api_instance.post_instrument_identifier(requestObj, profile_id=profileid)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling InstrumentIdentifierApi->post_instrument_identifier: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    print(os.getcwd())
    create_instrument_identifier_card_enroll_for_network_token()
