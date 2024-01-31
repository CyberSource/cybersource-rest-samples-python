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

def replay_specific_list_of_transactions(webhook_id):

    byTransactionTraceIdentifiers = []
    byTransactionTraceIdentifiers.append("1f1d0bf4-9299-418d-99d8-faa3313829f1")
    byTransactionTraceIdentifiers.append("d19fb205-20e5-43a2-867e-bd0f574b771e")
    byTransactionTraceIdentifiers.append("2f2461a3-457c-40e9-867f-aced89662bbb")
    byTransactionTraceIdentifiers.append("e23ddc19-93d5-4f1f-8482-d7cafbb3ed9b")
    byTransactionTraceIdentifiers.append("eb9fc4a9-b31f-48d5-81a9-b1d773fd76d8")
    requestObj = ReplayWebhooksRequest(
        by_transaction_trace_identifiers = byTransactionTraceIdentifiers
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        return_data, status, body = api_instance.replay_previous_webhooks(webhook_id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->replay_previous_webhooks: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    replay_specific_list_of_transactions(webhook_id)