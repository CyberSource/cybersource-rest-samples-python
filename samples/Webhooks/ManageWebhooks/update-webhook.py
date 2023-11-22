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

def update_webhook(webhook_id):
    name = "My Sample Webhook"
    description = "Update to my sample webhook"
    organizationId = "testOrgId"
    productId = "terminalManagement"

    eventTypes = []
    eventTypes.append("terminalManagement.assignment.update")
    eventTypes.append("terminalManagement.status.update")
    webhookUrl = "https://MyWebhookServer.com:8443:/simulateClient"
    healthCheckUrl = "https://MyWebhookServer.com:8443:/simulateClientHealthCheck"
    status = "INACTIVE"
    requestObj = UpdateWebhook(
        name = name,
        description = description,
        organization_id = organizationId,
        product_id = productId,
        event_types = eventTypes,
        webhook_url = webhookUrl,
        health_check_url = healthCheckUrl,
        status = status
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        return_data, status, body = api_instance.update_webhook_subscription(webhook_id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->update_webhook_subscription: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    update_webhook(webhook_id)