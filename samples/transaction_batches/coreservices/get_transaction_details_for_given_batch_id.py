from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_transaction_details_for_given_batch_id():
    uploadDate = "2019-05-01T12:00:00Z"
    status = "REJECTED"
    id = "12345"
	
    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TransactionBatchesApi(client_config)
        return_data, status, body = api_instance.get_transaction_batch_details(id, upload_date=uploadDate, status=status)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        print("API RESPONSE BODY : ", return_data)
        return return_data
    except Exception as e:
        print("Exception when calling TransactionBatchesApi->get_transaction_batch_details: %s\n" % e)


if __name__ == "__main__":
    get_transaction_details_for_given_batch_id()
