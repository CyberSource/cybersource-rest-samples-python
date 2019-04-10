from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

#* This is the method to get net funding information for merchant information user should pass starttime, end time
def get_netfunding_information_for_account_or_merchant():
    try:
        start_time="2019-03-21T00:00:00.0Z"
        end_time="2019-03-21T23:00:00.0Z"
        group_name="groupName"
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        get_netFundings_obj = NetFundingsApi(details_dict1)
        return_data, status, body = get_netFundings_obj.get_net_funding_info(start_time,end_time, organization_id="testrest")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report_by_report_id: %s\n" % e)


if __name__ == "__main__":
    get_netfunding_information_for_account_or_merchant()
