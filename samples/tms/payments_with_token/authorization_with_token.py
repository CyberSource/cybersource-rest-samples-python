from cybersource_rest_client_python import *
import json


def authorization_with_token():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_3"
        request.client_reference_information = client_reference.__dict__
    
        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "internet"
        request.processing_information = processing_info.__dict__
    
        aggregator_information = V2paymentsAggregatorInformation()
        sub_merchant_info = V2paymentsAggregatorInformationSubMerchant()
        sub_merchant_info.card_acceptor_id = "1234567890"
        sub_merchant_info.country = "US"
        sub_merchant_info.phone_number = "650-432-0000"
        sub_merchant_info.address1 = "900 Metro Center"
        sub_merchant_info.postal_code = "94404-2775"
        sub_merchant_info.locality = "Foster City"
        sub_merchant_info.name = "Visa Inc"
        sub_merchant_info.administrative_area = "CA"
        sub_merchant_info.region = "PEN"
        sub_merchant_info.email = "test@cybs.com"
        aggregator_information.name = "V-Internatio"
        aggregator_information.aggregator_id = "123456789"
        aggregator_information.sub_merchant=sub_merchant_info.__dict__
        request.aggregator_information=aggregator_information.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "22"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.phone_number = "999999999"
        bill_to.address2 = "Address 2"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.company = "Visa"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        order_information.bill_to = bill_to.__dict__
    
        payment_information = V2paymentsidrefundsPaymentInformation()
        customer_info = V2paymentsPaymentInformationCustomer()
        customer_info.customer_id = "7500BB199B4270EFE05340588D0AFCAD"
        payment_information.customer = customer_info.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        return_data, status, body =payment_obj.create_payment(message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    authorization_with_token()
