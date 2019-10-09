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
        id_input = "ba5d64bb-36a2-424a-a93a-376565f8d1b4"
        return_data, status, body = search_transaction_obj.get_search(id_input)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling SearchTransactionsApi->get_search: %s\n" % e)


if __name__ == "__main__":
    get_search_results()
