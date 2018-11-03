from CyberSource import *
import samples.payments.coreservices.process_credit
import json
from data.Configaration import *

def void_a_credit():
    try:
        api_credit_response=samples.payments.coreservices.process_credit.process_a_credit()
        id = api_credit_response.id
        request = VoidCreditRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "test_credit_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        config_obj = Configaration()
        details_dict1 = config_obj.get_configaration()
        void_obj = VoidApi(details_dict1)
        return_data, status, body =void_obj.void_credit(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_credit()
