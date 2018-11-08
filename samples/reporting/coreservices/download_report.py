from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def download_reports():
    try:
        report_name="testrest_v2"
        report_date="2018-09-02"
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        report_download_obj=ReportDownloadsApi(details_dict1)
        return_data, status, body =report_download_obj.download_report(report_date,report_name)
        print(status)
        print(body)
        f = open(os.getcwd()+"\\report.csv", "a+")
        f.write("*************** Start Of Report*****************\n")
        f.write(body)
        f.write("*************** End Of Report*****************\n")
        f.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    download_reports()
