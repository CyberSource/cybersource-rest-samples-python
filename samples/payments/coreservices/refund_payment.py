from CyberSource import *
import process_payment
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def refund_a_payment():
    try:
        api_payment_response=process_payment.process_a_payment(True)
        id = api_payment_response.id
        request = RefundPaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code =  "test_refund_payment"
        request.client_reference_information = client_reference.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "10"
        amount_details.currency = "USD"

        order_information.amount_details = amount_details.__dict__

        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        refund_api = RefundApi(details_dict1)
        return_data, status, body =refund_api.refund_payment(message_body, id)
        print(status)
        print(body)
        return return_data

    except Exception as e:
        print(e)



if __name__ == "__main__":
    refund_a_payment()
