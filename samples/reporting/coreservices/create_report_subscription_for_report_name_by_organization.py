from CyberSource import *
import json
import os
import inspect
import delete_subscription_of_report_name_by_organization
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_report_subscription():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        request = RequestBody(report_definition_name="TransactionRequestClass",report_fields=["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"],report_name="Cybersource-rest-py")
        #request.report_definition_name = "TransactionRequestClass"
        #request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
        request.report_mime_type = "application/xml"
        request.report_frequency = "WEEKLY"
        request.timezone = "GMT"
        request.start_time = "0825"
        request.start_day = 1
        #request.report_name = "Cybersource-rest-py"
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        report_subscription_obj = ReportSubscriptionsApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = report_subscription_obj.create_subscription(message_body,report_name=request.report_name)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

        # Deleting the Report created by create_subscription method
        if response_data.status == 201:
            delete_subscription_of_report_name_by_organization.delete_subscriptions_report(request.report_name)

        return json.loads(response_data.data)
    except Exception as e:
        print("\nException when calling ReportSubscriptionsApi->create_subscription: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    create_report_subscription()
