from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def process_payment_with_servicefee(flag):
    try:
        # Setting the request body
        request = CreatePaymentRequest()
		
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_payment"
		
        request.client_reference_information = client_reference.__dict__

        # Setting processing information
        processing_info = Ptsv2paymentsProcessingInformation()
        processing_info.commerce_indicator = "internet"
		
        if flag:
            processing_info.capture = "true"
			
        request.processing_information = processing_info.__dict__

        # Setting order information details and bill to information 
        order_information = Ptsv2paymentsOrderInformation()
		
        bill_to = Ptsv2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "Doe"
        bill_to.address2 = "1 Market St"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.first_name = "John"
        bill_to.phone_number = "999999999"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        bill_to.company = "ABC Company"
        bill_to.email = "test@cybs.com"

        # Setting the amount details which needs to be Authorized
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()		
        amount_details.total_amount = "2350.00"
        amount_details.currency = "USD"
        amount_details.service_fee_amount = "30.00" 
		
        order_information.amount_details = amount_details.__dict__		
        order_information.bill_to = bill_to.__dict__
		
        request.order_information = order_information.__dict__
        
        # Setting payment information and card information details
        payment_info = Ptsv2paymentsPaymentInformation()
		
        card = Ptsv2paymentsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "4111111111111111"
        card.security_code = "123"
        card.expiration_month = "12"
		
        payment_info.card = card.__dict__
		
        request.payment_information = payment_info.__dict__
        
        # Setting service fee descriptor value and assign to merchant information
        merchant_info = Ptsv2paymentsMerchantInformation()
		
        service_fee_descriptor = Ptsv2paymentsMerchantInformationServiceFeeDescriptor()
        service_fee_descriptor.name = "ABC"
        service_fee_descriptor.contact = "12345"
        service_fee_descriptor.state = "TEXAS"
		
        merchant_info.service_fee_descriptor = service_fee_descriptor.__dict__
		
        request.merchant_information = merchant_info.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        payment_obj = PaymentsApi(details_dict1)
		
        return_data, status, body = payment_obj.create_payment(message_body)
		
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    process_payment_with_servicefee(False)
