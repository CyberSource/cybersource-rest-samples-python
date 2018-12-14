from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def delete_subscriptions_report(reportname):
    try:

        report_name = reportname
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_subscription_obj = ReportSubscriptionsApi(details_dict1)
        return_data, status, body = report_subscription_obj.delete_subscription(report_name)

        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling ReportSubscriptionsApi->delete_subscription: %s\n" % e)


if __name__ == "__main__":
    delete_subscriptions_report(reportname="Cybersource-rest-py")
