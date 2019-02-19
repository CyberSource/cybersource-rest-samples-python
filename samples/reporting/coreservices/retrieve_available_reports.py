from CyberSource import *
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def available_reports():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        start_time = "2018-10-01T00:00:00.0Z"
        end_time = "2018-10-30T23:59:59.0Z"
        time_query_type = "executedTime"
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        report_obj = ReportsApi(details_dict1)
        response_data = report_obj.search_reports(start_time, end_time, time_query_type)
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
    except Exception as e:
        print("\nException when calling ReportsApi->search_reports: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    available_reports()
