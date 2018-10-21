from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.payments.coreservices.refund_payment
import json


def void_a_refund():
    try:
        api_refund_rsponse=cybersource_rest_samples_python.samples.payments.coreservices.refund_payment.refund_a_payment()
        id = api_refund_rsponse.id
        request = VoidRefundRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "test_refund_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        void_obj.void_refund(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_refund()
