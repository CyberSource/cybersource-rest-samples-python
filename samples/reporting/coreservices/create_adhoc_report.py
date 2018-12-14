from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_adhoc_report():
    try:
        # Setting the json message body
        request = RequestBody1()
        request.report_definition_name = "TransactionRequestClass"
        request.timezone = "GMT"
        request.report_mime_type = "application/xml"
        request.report_name = "cybersource-dec-17"
        request.report_start_time = "2018-09-01T12:00:00+05:00"
        request.report_end_time = "2018-09-02T12:00:00+05:00"
        request.report_filters = {
            "Application.Name": []
        }
        request.report_preferences = {"signedAmounts": "true", "fieldNameConvention": "SOAPI"}
        request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        report_obj = ReportsApi(details_dict1)
        return_data, status, body = report_obj.create_report(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling ReportsApi->create_report: %s\n" % e)


if __name__ == "__main__":
    create_adhoc_report()
