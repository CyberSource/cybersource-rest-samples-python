from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()



def process_an_authorization_reversal():
    try:
        api_payment_response=process_payment.process_a_payment(False)
        id = api_payment_response.id
        request = AuthReversalRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_reversal"
        request.client_reference_information = client_reference.__dict__

        reversal_information = Ptsv2paymentsidreversalsReversalInformation()
        reversal_information.reason = "testing"
        amount_details = Ptsv2paymentsidreversalsReversalInformationAmountDetails()
        amount_details.total_amount = "102.21"
        reversal_information.amount_details = amount_details.__dict__

        request.reversal_information = reversal_information.__dict__

        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        reversal_obj = ReversalApi(details_dict1)

        return_data, status, body = reversal_obj.auth_reversal(id, message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    process_an_authorization_reversal()
