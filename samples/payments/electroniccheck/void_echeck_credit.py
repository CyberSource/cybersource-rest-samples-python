from CyberSource import *
import process_echeck_credit
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def void_echeck_credit():
    try:
        # Getting the credit_id dynamically using process_a_credit method
        api_credit_response = process_echeck_credit.process_echeck_credit("false")
        credit_id = api_credit_response.id
        # Setting the json message body
        request = VoidCreditRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference._code = "test_credit_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body = void_obj.void_credit(message_body, credit_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling VoidApi->void_credit: %s\n" % e)


if __name__ == "__main__":
    void_echeck_credit()
