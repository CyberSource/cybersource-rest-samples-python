from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_list_of_batch_files():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        start_time = "2019-09-25T20:34:24.000Z"
        end_time = "2019-10-03T23:27:25.000Z"
        transction_api_obj = TransactionBatchesApi(details_dict1)
        return_data, status, body = transction_api_obj.get_transaction_batches(start_time, end_time)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling TransactionBatchesApi->get_transaction_batches: %s\n" % e)


if __name__ == "__main__":
    get_list_of_batch_files()
