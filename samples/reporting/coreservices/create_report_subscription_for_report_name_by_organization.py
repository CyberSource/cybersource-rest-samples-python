from CyberSource import *
import json
import os
import delete_subscription_of_report_name_by_organization
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_report_subscription():
    try:
        request = RequestBody()
        request.report_definition_name = "TransactionRequestClass"
        request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
        request.report_mime_type = "application/xml"
        request.report_frequency = "WEEKLY"
        request.timezone = "GMT"
        request.start_time = "0547"
        request.start_day = 1
        request.report_name="Cybersource-rest-py"

        message_body = json.dumps(request.__dict__)
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_subscription_obj = ReportSubscriptionsApi(details_dict1)
        return_data, status, body = report_subscription_obj.create_subscription(message_body)
        print(status)
        print(body)
        if status==201:
            delete_subscription_of_report_name_by_organization.delete_subscriptions_report(request.report_name)

        return return_data
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_report_subscription()
