from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()



def download_reports():
    try:
        report_name = "ML4IDIBI"
        report_date = "2019-03-12"
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_download_obj = ReportDownloadsApi(details_dict1)
        return_data, status, body = report_download_obj.download_report(report_date, report_name,organization_id="testrest")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        # The Report obtained is being stored in a CSV file
        f = open(os.path.join(os.getcwd(), "resources", "download_report.csv"), "a+")
        f.write("\n********************** Start Of Report***********************\n")
        f.write(body)
        f.write("\n********************** End Of Report*************************\n")
        f.close()
        print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources", "download_report.csv"))

    except Exception as e:
        print("Exception when calling ReportDownloadsApi->download_report: %s\n" % e)


if __name__ == "__main__":
    download_reports()
