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

def replay_failed_transactions_by_set_start_and_end_time(webhook_id):
    byDeliveryStatusStatus = "FAILED"
    byDeliveryStatusStartTime = "2021-01-01T15:05:52.284+05:30"
    byDeliveryStatusEndTime = "2021-01-02T03:05:52.284+05:30"
    byDeliveryStatusProductId = "tokenManagement"
    byDeliveryStatusEventType = "tms.token.created"
    # Nrtfv1webhookswebhookIdreplaysByDeliveryStatus removed in SDK 0.0.80 with no replacement.
    # byDeliveryStatus = Nrtfv1webhookswebhookIdreplaysByDeliveryStatus(
    #     status = byDeliveryStatusStatus,
    #     start_time = byDeliveryStatusStartTime,
    #     end_time = byDeliveryStatusEndTime,
    #     product_id = byDeliveryStatusProductId,
    #     event_type = byDeliveryStatusEventType
    # )

    # ReplayWebhooksRequest removed in SDK 0.0.80 with no replacement.
    # requestObj = ReplayWebhooksRequest(
    #     by_delivery_status = byDeliveryStatus.__dict__
    # )
    # requestObj = del_none(requestObj.__dict__)
    # requestObj = json.dumps(requestObj)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        # ManageWebhooksApi.replay_previous_webhooks removed in SDK 0.0.80 with no replacement.
        # return_data, status, body = api_instance.replay_previous_webhooks(webhook_id, requestObj)
        write_log_audit(200)
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->replay_previous_webhooks: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

webhook_id = "INSERT ID VALUE"
if __name__ == "__main__":
    replay_failed_transactions_by_set_start_and_end_time(webhook_id)