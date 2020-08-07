from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def list_payment_instruments_for_instrument_identifier():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    instrumentIdentifierTokenId = "7010000000016241111"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InstrumentIdentifierApi(client_config)
        return_data, status, body = api_instance.get_instrument_identifier_payment_instruments_list(instrumentIdentifierTokenId, profile_id=profileid)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling InstrumentIdentifierApi->get_instrument_identifier_payment_instruments_list: %s\n" % e)

if __name__ == "__main__":
    list_payment_instruments_for_instrument_identifier()
