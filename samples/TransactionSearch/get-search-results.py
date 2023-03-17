from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

search_path = os.path.join(os.getcwd(), "samples", "TransactionSearch", "create-search-request.py")
create_search = SourceFileLoader("module.name", search_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def get_search_results():
    api_search_response = create_search.create_search_request()
    searchId = api_search_response.search_id

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SearchTransactionsApi(client_config)
        return_data, status, body = api_instance.get_search(searchId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling SearchTransactionsApi->get_search: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    get_search_results()
