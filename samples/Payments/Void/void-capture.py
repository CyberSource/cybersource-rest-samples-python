from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

capture_payment_path = os.path.join(os.getcwd(), "samples", "Payments", "Capture", "capture-payment.py")
capture_payment = SourceFileLoader("module.name", capture_payment_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def void_capture():
    

    clientReferenceInformationCode = "test_void"
    clientReferenceInformation = Ptsv2paymentsidreversalsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    requestObj = VoidCaptureRequest(
        client_reference_information = clientReferenceInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        api_capture_response = capture_payment.capture_payment()
        id = api_capture_response.id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = VoidApi(client_config)
        return_data, status, body = api_instance.void_capture(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling VoidApi->void_capture: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    void_capture()
