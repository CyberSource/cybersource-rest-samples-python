from CyberSource import *
import samples.payments.coreservices.process_payment
import json


def void_a_payment():
    try:
        api_payment_response=samples.payments.coreservices.process_payment.process_a_payment(True)
        id = api_payment_response.id
        request = VoidPaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code =  "test_payment_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        return_data, status, body =void_obj.void_payment(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    void_a_payment()
