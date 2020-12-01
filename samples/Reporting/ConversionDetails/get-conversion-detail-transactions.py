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

def get_conversion_detail_transactions():
    startTime = "2020-10-21T00:00:00Z"
    endTime = "2020-10-21T23:00:00Z"
    organizationId = "testrest"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ConversionDetailsApi(client_config)
        return_data, status, body = api_instance.get_conversion_detail(startTime, endTime, organization_id=organizationId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling ConversionDetailsApi->get_conversion_detail: %s\n" % e)

if __name__ == "__main__":
    get_conversion_detail_transactions()
