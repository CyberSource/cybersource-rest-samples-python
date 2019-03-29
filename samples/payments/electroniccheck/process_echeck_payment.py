from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def process_echeck_payment(flag):
    try:
        # Setting the request body
        request = CreatePaymentRequest()
		
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "TC46181-6"
		
        request.client_reference_information = client_reference.__dict__

        # Setting processing information
        processing_information = Ptsv2paymentsProcessingInformation()
        processing_information.commerce_indicator = "internet"
		
        request.processing_information = processing_information.__dict__

        processing_info = Ptsv2paymentsProcessingInformation()

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

        # Setting the amount details which needs to be authorized
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100"
        amount_details.currency = "USD"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        # Setting payment information and bank information details
        payment_info = Ptsv2paymentsPaymentInformation()
		
        payment_info_bank = Ptsv2paymentsPaymentInformationBank()
        payment_info_bank_account_info = Ptsv2paymentsPaymentInformationBankAccount();
        payment_info_bank_account_info.number = "4100"
        payment_info_bank_account_info.type = "C"
        payment_info_bank.account = payment_info_bank_account_info.__dict__
        payment_info_bank.routing_number = "071923284";
        payment_info.bank = payment_info_bank.__dict__;

        request.payment_information = payment_info.__dict__
        request.order_information = order_information.__dict__
		
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
    process_echeck_payment(False)
