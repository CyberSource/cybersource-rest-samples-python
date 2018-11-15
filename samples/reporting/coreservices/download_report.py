from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def download_reports():
    try:
        report_name="testrest_v2"
        report_date="2018-09-02"
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_download_obj=ReportDownloadsApi(details_dict1)
        return_data, status, body =report_download_obj.download_report(report_date,report_name)
        print(status)
        print(body)
        f = open(os.path.join(os.getcwd(),"resources","report_download.csv"), "a+")
        f.write("\n********************** Start Of Report***********************\n")
        f.write(body)
        f.write("\n********************** End Of Report*************************\n")
        f.close()
        print("File Downloaded at the Location :  "+os.path.join(os.getcwd(),"resources","report_download.csv"))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    download_reports()
