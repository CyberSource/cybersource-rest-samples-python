from CyberSource import *
from CyberSource.rest import ApiException
from CyberSource import GenerateCaptureContextRequest
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
    return d

def generate_capture_context_accept_check():
    clientVersion = "v2"

    targetOrigins = []
    targetOrigins.append("https://www.test.com")
    allowedPaymentTypes = []
    allowedPaymentTypes.append("CHECK")
    requestObj = GenerateCaptureContextRequest(
        client_version = clientVersion,
        target_origins = targetOrigins,
        allowed_payment_types=allowedPaymentTypes
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = MicroformIntegrationApi(client_config)
        return_data, status, body = api_instance.generate_capture_context(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling MicroformIntegrationApi->generate_capture_context: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    generate_capture_context_accept_check()