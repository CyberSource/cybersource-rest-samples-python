from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
        elif isinstance(value, list):
            for item in value:
                del_none(item)
    return d

def replay_failed_transactions_by_set_start_and_end_time(webhook_id):
    byDeliveryStatusStatus = "FAILED"
    byDeliveryStatusStartTime = "2021-01-01T15:05:52.284+05:30"
    byDeliveryStatusEndTime = "2021-01-02T03:05:52.284+05:30"
    byDeliveryStatusProductId = "tokenManagement"
    byDeliveryStatusEventType = "tms.token.created"
    byDeliveryStatus = Nrtfv1webhookswebhookIdreplaysByDeliveryStatus(
        status = byDeliveryStatusStatus,
        start_time = byDeliveryStatusStartTime,
        end_time = byDeliveryStatusEndTime,
        product_id = byDeliveryStatusProductId,
        event_type = byDeliveryStatusEventType
    )

    requestObj = ReplayWebhooks(
        by_delivery_status = byDeliveryStatus.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        return_data, status, body = api_instance.replay_previous_webhook(webhook_id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->replay_previous_webhook: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    replay_failed_transactions_by_set_start_and_end_time(webhook_id)