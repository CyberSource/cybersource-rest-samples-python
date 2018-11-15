from CyberSource import *
import process_credit
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def void_a_credit():
    try:
        api_credit_response=process_credit.process_a_credit()
        id = api_credit_response.id
        request = VoidCreditRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference._code = "test_credit_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body =void_obj.void_credit(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_credit()
