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

def get_purchase_and_refund_details():
    startTime = "2018-05-01T12:00:00-05:00"
    endTime = "2018-05-30T12:00:00-05:00"
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
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling PurchaseAndRefundDetailsApi->get_purchase_and_refund_details: %s\n" % e)

if __name__ == "__main__":
    get_purchase_and_refund_details()
