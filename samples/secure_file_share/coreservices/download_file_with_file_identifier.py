from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def download_file_with_file_identifier():
    field_id="VFJSUmVwb3J0LTc4NTVkMTNmLTkzOTgtNTExMy1lMDUzLWEyNTg4ZTBhNzE5Mi5jc3YtMjAxOC0xMC0yMA=="
    config_obj = configaration.Configaration()
    details_dict1 = config_obj.get_configaration()
    search_transaction_obj = SecureFileShareApi(details_dict1)
    return_data, status, body =search_transaction_obj.get_file(field_id,organization_id="testrest")
    print(status)
    print(body)
    f = open(os.getcwd() + "\\report.csv", "a+")
    f.write("*************** Start Of Report*****************\n")
    f.write(body)
    f.write("*************** End Of Report*****************\n")
    f.close()


if __name__ == "__main__":
    download_file_with_file_identifier()
