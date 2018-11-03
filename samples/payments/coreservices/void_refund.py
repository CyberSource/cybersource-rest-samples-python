from CyberSource import *
import refund_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def void_a_refund():
    try:
        api_refund_rsponse=refund_payment.refund_a_payment()
        id = api_refund_rsponse.id
        request = VoidRefundRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "test_refund_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body =void_obj.void_refund(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_refund()
