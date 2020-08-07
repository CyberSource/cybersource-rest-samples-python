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

def list_shipping_addresses_for_customer():
    customerTokenId = "AB695DA801DD1BB6E05341588E0A3BDC"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CustomerShippingAddressApi(client_config)
        return_data, status, body = api_instance.get_customer_shipping_addresses_list(customerTokenId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling CustomerShippingAddressApi->get_customer_shipping_addresses_list: %s\n" % e)

if __name__ == "__main__":
    list_shipping_addresses_for_customer()
