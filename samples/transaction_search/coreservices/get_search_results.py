from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_search_results():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SearchTransactionsApi(details_dict1)
        id_input = "49df9838-b120-4b37-9ce6-7e6197270d91"
        return_data, status, body = search_transaction_obj.get_search(id_input)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling SearchTransactionsApi->get_search: %s\n" % e)


if __name__ == "__main__":
    get_search_results()
