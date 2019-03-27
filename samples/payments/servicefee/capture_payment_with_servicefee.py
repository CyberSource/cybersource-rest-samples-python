from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

#Following code is to handle the Sibling Package Import
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "servicefee"
import process_payment_with_servicefee

def capture_payment_with_servicefee():
    try:
        # Getting the payment_id dynamically using process_a_payment method
        api_payment_response = process_payment_with_servicefee.process_payment_with_servicefee(False)
		
        payment_id = api_payment_response.id
		
        # Setting the request body
        request = CapturePaymentRequest()
		
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_capture"
		
        request.client_reference_information = client_reference.__dict__

        # This is the secion to set processing information
        processing_information = Ptsv2paymentsProcessingInformation()		
        processing_information.commerce_indicator = "internet"
		
        request.processing_information = processing_information.__dict__

        # Setting order information details and amount which needs to be captured
        order_information = Ptsv2paymentsOrderInformation()
		
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"
        amount_details.service_fee_amount = "30.00";
		
        order_information.amount_details = amount_details.__dict__
		
        request.order_information = order_information.__dict__

        # Setting merchant information details
        merchant_info = Ptsv2paymentsMerchantInformation()
		
        service_fee_descriptor = Ptsv2paymentsMerchantInformationServiceFeeDescriptor()
        service_fee_descriptor.name = "CyberSource"
        service_fee_descriptor.contact = "800999999"
        service_fee_descriptor.state = "CA"

        merchant_info.service_fee_descriptor = service_fee_descriptor.__dict__
		
        request.merchant_information = merchant_info.__dict__

        message_body = (json.dumps(request.__dict__))
		
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        capture_obj = CaptureApi(details_dict1)
		
        return_data, status, body = capture_obj.capture_payment(message_body, payment_id)
		
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data
    except Exception as e:
        print("Exception when calling CaptureApi->capture_payment: %s\n" % e)

if __name__ == "__main__":
    capture_payment_with_servicefee()
