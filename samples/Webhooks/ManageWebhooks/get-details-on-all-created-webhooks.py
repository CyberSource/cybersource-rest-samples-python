from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    if isinstance(d, str):
        return d
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
        elif isinstance(value, list):
            for item in value:
                del_none(item)
    return d

def get_details_on_all_created_webhooks():
    // QUERY PARAMETERS
    organization_id = "testrest"
    product_id = "testProductId"
    event_type = "testEventType"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        return_data, status, body = api_instance.get_webhook_subscriptions_by_org(organization_id, product_id, event_type)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->get_webhook_subscriptions_by_org: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    get_details_on_all_created_webhooks()