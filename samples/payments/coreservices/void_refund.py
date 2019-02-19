from CyberSource import *
import refund_payment
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def void_a_refund():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Getting the refund_id dynamically using refund_a_payment method
        api_refund_rsponse = refund_payment.refund_a_payment()
        refund_id = api_refund_rsponse['id']
        # Setting the json message body
        request = VoidRefundRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference._code = "test_refund_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = void_obj.void_refund(message_body, refund_id)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
    except Exception as e:
        print("\nException when calling VoidApi->void_refund: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    void_a_refund()
