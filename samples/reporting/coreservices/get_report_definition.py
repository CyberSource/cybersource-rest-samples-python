from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_all_report_definitions():
    try:
        report_definition_name="AcquirerExceptionDetailClass"
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_definition_obj = ReportDefinitionsApi(details_dict1)
        return_data, status, body =report_definition_obj.get_resource_info_by_report_definition(report_definition_name)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_all_report_definitions()
