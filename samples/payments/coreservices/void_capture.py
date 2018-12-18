from CyberSource import *
import capture_payment
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def void_a_capture():
    try:
        # Getting the capture_id dynamically using capture_a_payment method
        api_capture_response = capture_payment.capture_a_payment()
        capture_id = api_capture_response.id
        # Setting the json message body
        request = VoidCaptureRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_capture_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body = void_obj.void_capture(message_body, capture_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling VoidApi->void_capture: %s\n" % e)


if __name__ == "__main__":
    void_a_capture()
