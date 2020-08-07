from CyberSource import *
import os
import json
import time
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

tms_file_path = os.path.join(os.getcwd(), "Samples", "TokenManagement", "PaymentInstrument", "create-payment-instrument-card.py")
create_payment_instrument = SourceFileLoader("module.name", tms_file_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def retrieve_payment_instrument():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    paymentInstrumentTokenId = "888454C31FB6150CE05340588D0AA9BE"

    time.sleep(10)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.get_payment_instrument(paymentInstrumentTokenId, profile_id=profileid)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentInstrumentApi->get_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    retrieve_payment_instrument()
