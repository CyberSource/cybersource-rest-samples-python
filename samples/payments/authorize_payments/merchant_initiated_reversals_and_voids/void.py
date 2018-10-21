from cybersource_rest_client_python import *
import json


def void():
    try:
        request = VoidPaymentRequest()
        id = "5396026860996470103003"
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_1"
        request.client_reference_information = client_reference.__dict__

        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        void_obj.void_payment(message_body, id)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    void()
