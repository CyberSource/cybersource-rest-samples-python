from CyberSource import *
import samples.payments.coreservices.process_payment
import samples.payments.coreservices.capture_payment
import json
from data.Configaration import *

def void_a_capture():
    try:
        api_capture_response=samples.payments.coreservices.capture_payment.capture_a_payment()
        id = api_capture_response.id
        request = VoidCaptureRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code ="test_capture_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        config_obj = Configaration()
        details_dict1 = config_obj.get_configaration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body =void_obj.void_capture(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_capture()
