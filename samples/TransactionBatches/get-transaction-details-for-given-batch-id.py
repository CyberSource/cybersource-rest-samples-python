from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def get_transaction_details_for_given_batch_id():
    id = "12345"
    uploadDate = "2019-08-30"
    status = "Rejected"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TransactionBatchesApi(client_config)
        api_instance.api_client.download_file_path = os.path.join(os.getcwd(), "resources", "download_report.csv")
        status, headers = api_instance.get_transaction_batch_details(id, upload_date=uploadDate, status=status)

        print("Download Status : ", status)
        print("Response Headers : ", headers)

        print("Response downloaded at the location : " + api_instance.api_client.download_file_path)
        write_log_audit(status)
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling TransactionBatchesApi->get_transaction_batch_details: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    get_transaction_details_for_given_batch_id()
