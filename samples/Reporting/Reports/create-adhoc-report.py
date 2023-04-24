from CyberSource import *
from pathlib import Path
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

def create_adhoc_report():
    reportDefinitionName = "TransactionRequestClass"

    reportFields = []
    reportFields.append("Request.RequestID")
    reportFields.append("Request.TransactionDate")
    reportFields.append("Request.MerchantID")
    reportMimeType = "application/xml"
    reportName = "testrest_v2"
    timezone = "GMT"
    reportStartTime = "2021-03-01T17:30:00.000+05:30"
    reportEndTime = "2021-03-02T17:30:00.000+05:30"
    reportPreferencesSignedAmounts = True
    reportPreferencesFieldNameConvention = "SOAPI"
    reportPreferences = Reportingv3reportsReportPreferences(
        signed_amounts = reportPreferencesSignedAmounts,
        field_name_convention = reportPreferencesFieldNameConvention
    )

    requestObj = CreateAdhocReportRequest(
        report_definition_name = reportDefinitionName,
        report_fields = reportFields,
        report_mime_type = reportMimeType,
        report_name = reportName,
        timezone = timezone,
        report_start_time = reportStartTime,
        report_end_time = reportEndTime,
        report_preferences = reportPreferences.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    organizationId = "testrest"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReportsApi(client_config)
        return_data, status, body = api_instance.create_report(requestObj, organization_id=organizationId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling ReportsApi->create_report: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    create_adhoc_report()
