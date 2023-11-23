from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

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

def list_batches():

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = BatchesApi(client_config)
        offset = 0
        limit = 10
        from_date = '20230101T123000Z'
        to_date = '20231001T123000Z'
        return_data, status, body = api_instance.get_batches_list(offset = offset, limit = limit, from_date = from_date, to_date = to_date)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling BatchesApi->get_batches_list: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    list_batches()
