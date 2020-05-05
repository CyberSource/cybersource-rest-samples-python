from CyberSource import *
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

def retrieve_available_reports():
    startTime = "2020-04-01T00:00:00Z"
    endTime = "2020-04-03T23:59:59Z"
    timeQueryType = "executedTime"
    reportMimeType = "application/xml"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReportsApi(client_config)
        return_data, status, body = api_instance.search_reports(startTime, endTime, timeQueryType, report_mime_type=reportMimeType)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling ReportsApi->search_reports: %s\n" % e)

if __name__ == "__main__":
    retrieve_available_reports()
