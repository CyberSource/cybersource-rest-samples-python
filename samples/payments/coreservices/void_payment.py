from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def void_a_payment():
    try:
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment.process_a_payment(True)
        payment_id = api_payment_response.id
        # Setting the json message body
        request = VoidPaymentRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_payment_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body = void_obj.void_payment(message_body, payment_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling VoidApi->void_payment: %s\n" % e)


if __name__ == "__main__":
    void_a_payment()
