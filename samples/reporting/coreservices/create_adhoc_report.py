from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_adhoc_report():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        request = RequestBody1()
        request.report_definition_name = "TransactionRequestClass"
        request.timezone = "GMT"
        request.report_mime_type = "application/xml"
        request.report_name = "Cybersource-rest-py098"
        request.report_start_time = "2018-09-01T12:00:00+05:00"
        request.report_end_time = "2018-09-02T12:00:00+05:00"
        request.report_filters = {
            "Application.Name": []
        }
        request.report_preferences = {"signedAmounts": "true", "fieldNameConvention": "SOAPI"}
        request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        report_obj = ReportsApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = report_obj.create_report(message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
    except Exception as e:
        print("\nException when calling ReportsApi->create_report: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    create_adhoc_report()
