from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

#This is the sample code to get conversion details 
#Merchant must pass start tiem and endtime 
def get_conversion_detail_transactions():
    try:
        start_time="2019-03-21T00:00:00.0Z"
        end_time="2019-03-21T23:00:00.0Z"
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        get_conversion_details_obj = ConversionDetailsApi(details_dict1)
        return_data, status, body = get_conversion_details_obj.get_conversion_detail(start_time,end_time, organization_id="testrest")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report_by_report_id: %s\n" % e)


if __name__ == "__main__":
    get_conversion_detail_transactions()
