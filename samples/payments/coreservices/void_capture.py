from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.payments.coreservices.process_payment
import cybersource_rest_samples_python.samples.payments.coreservices.capture_payment
import json


def void_a_capture():
    try:
        api_capture_response=cybersource_rest_samples_python.samples.payments.coreservices.capture_payment.capture_a_payment()
        id = api_capture_response.id
        request = VoidCaptureRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code ="test_capture_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        return_data, status, body =void_obj.void_capture(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_capture()
