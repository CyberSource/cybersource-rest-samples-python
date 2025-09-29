from CyberSource import *  # Import all classes
from pathlib import Path
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def upload_transaction_batch():
     # Specify the file path to be uploaded
    file_path = os.path.join(os.getcwd(), "resources", "batchapiTest.csv")

    try:
        # Open the file in read mode and pass it to the API
        with open(file_path, "r") as file:
            config_obj = configuration.Configuration()
            client_config = config_obj.get_configuration_for_batchUploadSample()
            api_instance = TransactionBatchesApi(client_config)
            return_data, status, body = api_instance.upload_transaction_batch(file)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling TransactionBatchesApi->upload_transaction_batch: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    upload_transaction_batch()
