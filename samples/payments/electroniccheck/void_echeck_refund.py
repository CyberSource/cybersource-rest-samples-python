from CyberSource import *
import refund_echeck_payment
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def void_echeck_refund():
    try:
        # Getting the refund_id dynamically using refund_echeck_payment method
        api_refund_rsponse = refund_echeck_payment.refund_echeck_payment()
        refund_id = api_refund_rsponse.id
        # Setting the json message body
        request = VoidRefundRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference._code = "test_refund_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body = void_obj.void_refund(message_body, refund_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling VoidApi->void_refund: %s\n" % e)


if __name__ == "__main__":
    void_echeck_refund()
