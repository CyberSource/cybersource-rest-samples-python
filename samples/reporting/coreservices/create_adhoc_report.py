from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def create_adhoc_report():
    try:
        request = RequestBody1()
        request.report_definition_name = "TransactionRequestClass"
        request.timezone = "GMT"
        request.report_mime_type = "application/xml"
        request.report_name = "Cyb_587"
        request.report_start_time = "2018-09-01T12:00:00+05:00"
        request.report_end_time = "2018-09-02T12:00:00+05:00"
        request.report_filters = {
            "Application.Name": []
        }
        request.report_preferences = {"signedAmounts":"true","fieldNameConvention":"SOAPI"}
        request.report_fields = ["Request.RequestID","Request.TransactionDate","Request.MerchantID"]

        message_body = json.dumps(request.__dict__)
        config_obj =configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        report_obj = ReportsApi(details_dict1)
        return_data, status, body=report_obj.create_report(message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_adhoc_report()
