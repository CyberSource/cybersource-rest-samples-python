from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_report_by_reportid():

        report_id = "79642c43-2368-0cd5-e053-a2588e0a7b3c"

        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        get_report_obj = ReportsApi(details_dict1)
        return_data, status, body = get_report_obj.get_report_by_report_id(report_id,organization_id="testrest")
        print(status)
        print(body)



if __name__ == "__main__":
    get_report_by_reportid()
