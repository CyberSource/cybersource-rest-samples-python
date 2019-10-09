from CyberSource import *
import json
import os
import delete_subscription_of_report_name_by_organization
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_report_subscription():
    try:
        # Setting the json message body
        request = CreateReportSubscriptionRequest(report_definition_name="TransactionRequestClass",
                               report_fields=["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"],
                               report_mime_type="application/xml", report_frequency="WEEKLY",
                               report_name="Cybersource-rest-py", timezone="GMT", start_time="0847")
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_subscription_obj = ReportSubscriptionsApi(details_dict1)
        return_data, status, body = report_subscription_obj.create_subscription(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        # Deleting the Report created by create_subscription method
        if status == 201:
            delete_subscription_of_report_name_by_organization.delete_subscriptions_report(request.report_name)

        return return_data
    except Exception as e:
        print("Exception when calling ReportSubscriptionsApi->create_subscription: %s\n" % e)


if __name__ == "__main__":
    create_report_subscription()
