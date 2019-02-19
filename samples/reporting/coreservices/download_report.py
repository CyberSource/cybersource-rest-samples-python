from CyberSource import *
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()



def download_reports():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        report_name = "Cybersource-rest-py60"
        report_date = "2018-09-02"
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        report_download_obj = ReportDownloadsApi(details_dict1)
        response_data = report_download_obj.download_report(report_date, report_name,organization_id="testrest")
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        # The Report obtained is being stored in a CSV file
        f = open(os.path.join(os.getcwd(), "resources", "download_report.csv"), "a+")
        f.write("\n********************** Start Of Report***********************\n")
        f.write(response_data.data)
        f.write("\n********************** End Of Report*************************\n")
        f.close()
        print("File Downloaded at the Location :  " + os.path.join(os.getcwd(), "resources", "download_report.csv"))

    except Exception as e:
        print("\nException when calling ReportDownloadsApi->download_report: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    download_reports()
