from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def process_an_authorization_reversal():
    try:
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment.process_a_payment(False)
        payment_id = api_payment_response.id
        # Setting the json message body
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
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        reversal_obj = ReversalApi(details_dict1)
        return_data, status, body = reversal_obj.auth_reversal(payment_id, message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling ReversalApi->auth_reversal: %s\n" % e)


if __name__ == "__main__":
    process_an_authorization_reversal()
