from CyberSource import *
import capture_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def refund_a_capture():
    try:
        api_capture_response = capture_payment.capture_a_payment()
        id = api_capture_response.id
        request = RefundCaptureRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference._code = "test_refund_capture"
        request.client_reference_information = client_reference.__dict__

        order_information = Ptsv2paymentsOrderInformation()
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "10"
        amount_details.currency = "USD"

        order_information.amount_details = amount_details.__dict__

        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        refund_api = RefundApi(details_dict1)
        return_data, status, body = refund_api.refund_capture(message_body, id)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    refund_a_capture()
