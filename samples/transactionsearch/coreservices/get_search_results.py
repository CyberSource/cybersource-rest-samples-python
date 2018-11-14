from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_search_results():
    try:
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SearchTransactionsApi(details_dict1)
        #create_search_request_body=samples.transaction_search.coreservices.create_search_request.create_search_request()
        id_input="5f6b1f07-0190-460b-852e-6766252fbb18"
        return_data, status, body=search_transaction_obj.get_search(id_input)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_search_results()
