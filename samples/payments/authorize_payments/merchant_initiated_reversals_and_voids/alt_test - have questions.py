from cybersource_rest_client_python import *
import json


def alt_test():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_1"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.address2 = "Address 2"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.building_number = "123"
        bill_to.administrative_area = "MI"
        bill_to.email = "test2@cybs.com"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__
    
        recipient_info = V2paymentsRecipientInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.number = "4111111111111111"
        recipient_info.card = card_information.__dict__
        request.recipient_information=recipient_info.__dict__
    
        reversal_info=V2paymentsidreversalsReversalInformation()
        reversal_info_amount=V2paymentsidreversalsReversalInformationAmountDetails()
        reversal_info_amount.total_amount="3000.00"
        reversal_info.amount_details=reversal_info_amount.__dict__
        request.reversal_information=reversal_info.__dict__
    
    
    
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    alt_test()
