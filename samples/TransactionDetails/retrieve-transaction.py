from CyberSource import *
import os
import json
import time
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

process_payment_path = os.path.join(os.getcwd(), "samples", "Payments", "Payments", "simple-authorizationinternet.py")
process_payment = SourceFileLoader("module.name", process_payment_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def retrieve_transaction():
    api_payment_response = process_payment.simple_authorizationinternet(False)
    id = api_payment_response.id

    time.sleep(10)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TransactionDetailsApi(client_config)
        return_data, status, body = api_instance.get_transaction(id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling TransactionDetailsApi->get_transaction: %s\n" % e)

if __name__ == "__main__":
    retrieve_transaction()
