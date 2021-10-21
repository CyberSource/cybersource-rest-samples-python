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

def interchange_clearing_level_data_for_account_or_merchant():
    # QUERY PARAMETERS
    organization_id = "testrest"
    start_time = "2021-08-01T00:00:00Z"
    end_time = "2021-09-01T23:59:59Z"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InterchangeClearingLevelDetailsApi(client_config)
        return_data, status, body = api_instance.get_interchange_clearing_level_details(start_time, end_time, organization_id = organization_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling InterchangeClearingLevelDetailsApi->get_interchange_clearing_level_details: %s\n" % e)

if __name__ == "__main__":
    interchange_clearing_level_data_for_account_or_merchant()