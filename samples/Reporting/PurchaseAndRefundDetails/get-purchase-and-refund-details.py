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

def get_purchase_and_refund_details():
    startTime = "2021-10-01T12:00:00Z"
    endTime = "2021-10-30T12:00:00Z"
    organizationId = "testrest"
    paymentSubtype = "VI"
    viewBy = "requestDate"
    groupName = "groupName"
    offset = 20
    limit = 2000

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PurchaseAndRefundDetailsApi(client_config)
        return_data, status, body = api_instance.get_purchase_and_refund_details(startTime, endTime, organization_id=organizationId, payment_subtype=paymentSubtype, view_by=viewBy, group_name=groupName, offset=offset, limit=limit)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PurchaseAndRefundDetailsApi->get_purchase_and_refund_details: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    get_purchase_and_refund_details()
