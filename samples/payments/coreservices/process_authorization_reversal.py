from CyberSource import *
import process_payment
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def process_an_authorization_reversal():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment.process_a_payment(False)
        payment_id = api_payment_response['id']
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
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        reversal_obj = ReversalApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data= reversal_obj.auth_reversal(payment_id, message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
    except Exception as e:
        print("\nException when calling ReversalApi->auth_reversal: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    process_an_authorization_reversal()
