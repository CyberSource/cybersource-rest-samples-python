from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.payments.coreservices.process_credit
import json


def void_a_credit():
    try:
        api_credit_response=cybersource_rest_samples_python.samples.payments.coreservices.process_credit.process_a_credit()
        id = api_credit_response.id
        request = VoidCreditRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "test_credit_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        return_data, status, body =void_obj.void_credit(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_credit()
