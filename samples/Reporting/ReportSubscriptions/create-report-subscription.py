from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def create_report_subscription():
    reportDefinitionName = "TransactionRequestClass"

    reportFields = []
    reportFields.append("Request.RequestID")
    reportFields.append("Request.TransactionDate")
    reportFields.append("Request.MerchantID")
    reportMimeType = "application/xml"
    reportFrequency = "WEEKLY"
    reportName = "testrest_subcription_v1"
    timezone = "GMT"
    startTime = "0900"
    startDay = 1
    requestObj = CreateReportSubscriptionRequest(
        report_definition_name = reportDefinitionName,
        report_fields = reportFields,
        report_mime_type = reportMimeType,
        report_frequency = reportFrequency,
        report_name = reportName,
        timezone = timezone,
        start_time = startTime,
        start_day = startDay
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReportSubscriptionsApi(client_config)
        return_data, status, body = api_instance.create_subscription(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling ReportSubscriptionsApi->create_subscription: %s\n" % e)

if __name__ == "__main__":
    create_report_subscription()
