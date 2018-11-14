from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()



def available_reports():
    try:
        start_time="2018-10-01T00:00:00.0Z"
        end_time="2018-10-30T23:59:59.0Z"
        time_query_type="executedTime"
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_obj=ReportsApi(details_dict1)
        return_data, status, body =report_obj.search_reports(start_time,end_time,time_query_type)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    available_reports()
