from cybersource_rest_client_python import *
import json


def cybersource_payment_tokenization():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC_MPOS_Paymentech_3"
        request.client_reference_information = client_reference.__dict__
    
        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "internet"
        request.processing_information = processing_info.__dict__
    
        order_information = V2paymentsOrderInformation()
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.phone_number = "6504327113"
        bill_to.address1 = "901 Metro Center Blvd"
        bill_to.postal_code = "94404"
        bill_to.locality = "Foster City"
        bill_to.administrative_area = "CA"
        bill_to.email = "test@cybs.com"
    
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "2719"
        amount_details.currency = "USD"
        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__
    
        payment_info = V2paymentsPaymentInformation()
        tokenized_card = V2paymentsPaymentInformationTokenizedCard()
        tokenized_card.expiration_year = "2031"
        tokenized_card.number = "4111111111111111"
        tokenized_card.expiration_month = "12"
        tokenized_card.transaction_type = "1"
        fluid_data = V2paymentsPaymentInformationFluidData()
        fluid_data.value = "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"
    
        payment_info.tokenized_card = tokenized_card.__dict__
        payment_info.fluid_data = fluid_data.__dict__
        request.payment_information = payment_info.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cybersource_payment_tokenization()
