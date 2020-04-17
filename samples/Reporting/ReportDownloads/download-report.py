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


def download_report():
    organizationId = "testrest"
    reportDate = "2020-03-03"
    reportName = "testrest_subcription_v2989"
    reportTime = "00:00:00Z"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReportDownloadsApi(client_config)
        api_instance.api_client.download_file_path = os.path.join(os.getcwd(), "resources", "download_report.csv")
        status, headers = api_instance.download_report(reportDate, reportName, organization_id=organizationId, report_time=reportTime)

        print("Download Status : ", status)
        print("Response Headers : ", headers)

        print("Response downloaded at the location : " + api_instance.api_client.download_file_path) 
    except Exception as e:
        print("\nException when calling ReportDownloadsApi->download_report: %s\n" % e)

if __name__ == "__main__":
    download_report()
