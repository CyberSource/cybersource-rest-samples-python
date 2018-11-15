from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def download_file_with_file_identifier():
    try:
        field_id="VFJSUmVwb3J0LTc4NTVkMTNmLTkzOTgtNTExMy1lMDUzLWEyNTg4ZTBhNzE5Mi5jc3YtMjAxOC0xMC0yMA=="
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SecureFileShareApi(details_dict1)
        return_data, status, body =search_transaction_obj.get_file(field_id,organization_id="testrest")
        print(status)
        print(body)
        f = open(os.path.join(os.getcwd(),"resources","report_download.csv"), "a+")
        f.write("\n********************** Start Of Report***********************\n")
        f.write(body)
        f.write("\n********************** End Of Report*************************\n")
        f.close()
        print("File Downloaded at the Location :  " + os.path.join(os.getcwd(),"resources","report_download.csv"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    download_file_with_file_identifier()
