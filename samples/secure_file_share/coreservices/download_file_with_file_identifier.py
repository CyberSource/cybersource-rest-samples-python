from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def download_file_with_file_identifier():
    try:
        field_id = "QmF0Y2hGaWxlc0RldGFpbFJlcG9ydC5jc3YtMjAxOC0xMC0zMA=="
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SecureFileShareApi(details_dict1)
        return_data, status, body = search_transaction_obj.get_file(field_id, organization_id="testrest")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        # The Report obtained is being stored in a CSV file
        file_extension = (search_transaction_obj.api_client.last_response.urllib3_response.headers['Content-Type'])[-3:]
        f = open(os.path.join(os.getcwd(), "resources", "fileshare_report." + file_extension), "a+")
        f.write(body)
        f.close()
        print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources", "fileshare_report.csv"))
    except Exception as e:
        print("Exception when calling SecureFileShareApi->get_file: %s\n" % e)


if __name__ == "__main__":
    download_file_with_file_identifier()
