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

def get_report_based_on_report_id():
    organizationId = "testrest"

    try:
        reportId = "79642c43-2368-0cd5-e053-a2588e0a7b3c"
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReportsApi(client_config)
        return_data, status, body = api_instance.get_report_by_report_id(reportId, organization_id=organizationId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ReportsApi->get_report_by_report_id: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    get_report_based_on_report_id()
