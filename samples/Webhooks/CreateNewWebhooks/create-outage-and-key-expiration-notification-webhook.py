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

def create_outage_and_key_expiration_notification_webhook():
    name = "My Custom Webhook"
    description = "Sample Webhook from Developer Center"
    organizationId = "<INSERT ORGANIZATION ID HERE>"
    productId = "cns"

    eventTypes = []
    eventTypes.append("cns.outage.notify.freeform")
    eventTypes.append("cns.report.keyExpiration.detail")
    webhookUrl = "https://MyWebhookServer.com:8443/simulateClient"
    healthCheckUrl = "https://MyWebhookServer.com:8443/simulateClientHealthCheck"
    notificationScope = "SELF"
    retryPolicyAlgorithm = "ARITHMETIC"
    retryPolicyFirstRetry = 1
    retryPolicyInterval = 1
    retryPolicyNumberOfRetries = 3
    retryPolicyDeactivateFlag = "false"
    retryPolicyRepeatSequenceCount = 0
    retryPolicyRepeatSequenceWaitTime = 0
    retryPolicy = Notificationsubscriptionsv1webhooksRetryPolicy(
        algorithm = retryPolicyAlgorithm,
        first_retry = retryPolicyFirstRetry,
        interval = retryPolicyInterval,
        number_of_retries = retryPolicyNumberOfRetries,
        deactivate_flag = retryPolicyDeactivateFlag,
        repeat_sequence_count = retryPolicyRepeatSequenceCount,
        repeat_sequence_wait_time = retryPolicyRepeatSequenceWaitTime
    )

    securityPolicySecurityType = "KEY"
    securityPolicyProxyType = "external"
    securityPolicy = Notificationsubscriptionsv1webhooksSecurityPolicy1(
        security_type = securityPolicySecurityType,
        proxy_type = securityPolicyProxyType
    )

    requestObj = CreateWebhookRequest(
        name = name,
        description = description,
        organization_id = organizationId,
        product_id = productId,
        event_types = eventTypes,
        webhook_url = webhookUrl,
        health_check_url = healthCheckUrl,
        notification_scope = notificationScope,
        retry_policy = retryPolicy.__dict__,
        security_policy = securityPolicy.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CreateNewWebhooksApi(client_config)
        return_data, status, body = api_instance.create_webhook_subscription(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling CreateNewWebhooksApi->create_webhook_subscription: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    create_outage_and_key_expiration_notification_webhook()