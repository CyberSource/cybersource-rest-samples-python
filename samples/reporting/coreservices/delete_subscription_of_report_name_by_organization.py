from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()
def delete_subscriptions_report():
    try:

        report_name="Cybersource-rest-py"
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        report_subscription_obj = ReportSubscriptionsApi(details_dict1)
        return_data, status, body =report_subscription_obj.delete_subscription(report_name)

        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    delete_subscriptions_report()
