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

def download_file_with_file_identifier():
    organizationId = "testrest"
    fileId = "Q2hhcmdlYmFja0FuZFJldHJpZXZhbFJlcG9ydC1hYWVkMWEwMS03OGNhLTU1YzgtZTA1My1hMjU4OGUwYWNhZWEuY3N2LTIwMjAtMDctMzA="

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SecureFileShareApi(client_config)
        api_instance.api_client.download_file_path = os.path.join(os.getcwd(), "resources", "download_report.csv")
        status, headers = api_instance.get_file(fileId, organization_id=organizationId)

        print("Download Status : ", status)
        print("Response Headers : ", headers)

        print("Response downloaded at the location : " + api_instance.api_client.download_file_path)
        write_log_audit(status)
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling SecureFileShareApi->get_file: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    download_file_with_file_identifier()
