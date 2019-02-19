from CyberSource import *
import process_payment
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def capture_a_payment():

    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment.process_a_payment(
            False)
        payment_id = api_payment_response['id']
        # Setting the json message body
        request = CapturePaymentRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_capture"
        request.client_reference_information = client_reference.__dict__

        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"
        order_information = Ptsv2paymentsOrderInformation()
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        message_body = (json.dumps(request.__dict__))

        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        capture_obj = CaptureApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = capture_obj.capture_payment(message_body, payment_id)
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        return json.loads(response_data.data)
    except Exception as e:
        print("\nException when calling CaptureApi->capture_payment: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)



if __name__ == "__main__":
    capture_a_payment()
