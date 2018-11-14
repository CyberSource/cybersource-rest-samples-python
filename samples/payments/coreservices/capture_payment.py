from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()
def capture_a_payment():
    try:

        api_payment_response = process_payment.process_a_payment(
            False)
        id = api_payment_response.id
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
        config_obj=configuration.Configuration()
        details_dict1=config_obj.get_configuration()
        capture_obj = CaptureApi(details_dict1)
        return_data, status, body = capture_obj.capture_payment(message_body, id)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)


if __name__ == "__main__":
    capture_a_payment()
