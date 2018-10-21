from cybersource_rest_client_python import *
import json


def master_card():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_12"
        request.client_reference_information = client_reference.__dict__
    
        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "internet"
        request.processing_information = processing_info.__dict__
    
        aggregator_details = V2paymentsAggregatorInformation()
        sub_merchant_information = V2paymentsAggregatorInformationSubMerchant()
        sub_merchant_information.card_acceptor_id = "1234567890"
        sub_merchant_information.country = "US"
        sub_merchant_information.phone_number = "650-432-0000"
        sub_merchant_information.address1 = "900 Metro Center"
        sub_merchant_information.postal_code = "94404-2775"
        sub_merchant_information.locality = "Foster City"
        sub_merchant_information.name = "Visa Inc"
        sub_merchant_information.administrative_area = "CA"
        sub_merchant_information.region = "PEN"
        sub_merchant_information.email = "test@cybs.com"
        aggregator_details.name = "V-Internatio"
        aggregator_details.aggregator_id = "123456789"
        aggregator_details.sub_merchant = sub_merchant_information.__dict__
        request.aggregator_information = aggregator_details.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "112.00"
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
    
        invoice_details = V2paymentsOrderInformationInvoiceDetails()
        invoice_details.purchase_order_number = "LevelIII Auth Po"
        order_information.invoice_details = invoice_details.__dict__
    
        payment_information = V2paymentsidrefundsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.type = "002"
        card_information.number = "5555555555554444"
        card_information.security_code = "123"
        payment_information.card = card_information.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    master_card()
