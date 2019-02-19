from CyberSource import *
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def download_file_with_file_identifier():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        field_id = "VFJSUmVwb3J0LTc4NTVkMTNmLTkzOTgtNTExMy1lMDUzLWEyNTg4ZTBhNzE5Mi5jc3YtMjAxOC0xMC0yMA=="
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SecureFileShareApi(details_dict1)
        response_data = search_transaction_obj.get_file(field_id, organization_id="testrest")
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        # The Report obtained is being stored in a CSV file
        f = open(os.path.join(os.getcwd(), "resources", "fileshare_report.csv"), "a+")
        f.write("\n********************** Start Of Report***********************\n")
        f.write(response_data.data)
        f.write("\n********************** End Of Report*************************\n")
        f.close()
        print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources", "fileshare_report.csv"))
    except Exception as e:
        print("\nException when calling SecureFileShareApi->get_file: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    download_file_with_file_identifier()
