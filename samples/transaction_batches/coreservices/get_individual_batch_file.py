from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_individual_batch_file():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        transction_api_obj = TransactionBatchesApi(details_dict1)
        batch_file_id = "20190110"
        return_data, status, body = transction_api_obj.get_transaction_batch_id(batch_file_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling TransactionBatchApi->get_transaction_batch_id: %s\n" % e)


if __name__ == "__main__":
    get_individual_batch_file()
