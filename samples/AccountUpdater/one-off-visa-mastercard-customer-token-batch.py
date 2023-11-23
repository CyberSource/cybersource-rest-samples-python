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

def one_off_visa_mastercard_customer_token_batch():
    type = "oneOff"

    includedTokens = []
    includedTokens1 = Accountupdaterv1batchesIncludedTokens(
        id = "C064DE56200B0DB0E053AF598E0A52AA"
    )

    includedTokens.append(includedTokens1.__dict__)

    includedTokens2 = Accountupdaterv1batchesIncludedTokens(
        id = "C064DE56213D0DB0E053AF598E0A52AA"
    )

    includedTokens.append(includedTokens2.__dict__)

    included = Accountupdaterv1batchesIncluded(
        tokens = includedTokens
    )

    merchantReference = "TC50171_3"
    notificationEmail = "test@cybs.com"
    requestObj = Body(
        type = type,
        included = included.__dict__,
        merchant_reference = merchantReference,
        notification_email = notificationEmail
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = BatchesApi(client_config)
        return_data, status, body = api_instance.post_batch(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling BatchesApi->post_batch: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    one_off_visa_mastercard_customer_token_batch()
