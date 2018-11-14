from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_list_of_files():
    try:
        start_date="2018-10-20"
        end_date="2018-10-30"
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj =SecureFileShareApi(details_dict1)
        return_data, status, body =search_transaction_obj.get_file_details(start_date,end_date,organization_id="testrest")
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_list_of_files()
