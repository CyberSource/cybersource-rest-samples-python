from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_transaction_details_for_given_batch_id():
    id = "12345"
	
    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TransactionBatchesApi(client_config)
        return_data, status, body = api_instance.get_transaction_batch_details(id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        
        # The Report obtained is being stored in a file
        file_extension = (api_instance.api_client.last_response.urllib3_response.headers['Content-Type'])[-3:]
        f = open(os.path.join(os.getcwd(), "resources", "BatchDetailsReport." + file_extension), "a+")
        f.write(body)
        f.close()
        print("Batch Details Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources", "BatchDetailsReport." + file_extension))
    except Exception as e:
        print("Exception when calling TransactionBatchesApi->get_transaction_batch_details: %s\n" % e)


if __name__ == "__main__":
    get_transaction_details_for_given_batch_id()
