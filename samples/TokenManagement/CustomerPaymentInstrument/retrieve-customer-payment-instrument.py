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

def retrieve_customer_payment_instrument():
    customerTokenId = "AB695DA801DD1BB6E05341588E0A3BDC"
    paymentInstrumentTokenId = "AB6A54B982A6FCB6E05341588E0A3935"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CustomerPaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.get_customer_payment_instrument(customerTokenId, paymentInstrumentTokenId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling CustomerPaymentInstrumentApi->get_customer_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    retrieve_customer_payment_instrument()
