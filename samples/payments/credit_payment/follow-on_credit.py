from cybersource_rest_client_python import *
import json


def follow_on_credit():
    try:
        id = "5360519587146625203004"
        request = RefundCaptureRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC12345"
        request.client_reference_information = client_reference.__dict__
    
        buyer_details = V2paymentsBuyerInformation()
        buyer_details.merchant_customer_id = "123456abcd"
        request.buyer_information = buyer_details.__dict__
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
        amount_details.total_amount = "100"
        amount_details.currency = "usd"
        amount_details.exchange_rate = "0.5"
        amount_details.exchange_rate_time_stamp = "2.01304E+13"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "John"
        bill_to.last_name = "Test"
        bill_to.phone_number = "9999999"
        bill_to.address2 = "test2credit"
        bill_to.address1 = "testcredit"
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.company = "Visa"
        bill_to.administrative_area = "MI"
        bill_to.email = "test2@cybs.com"
        order_information.bill_to = bill_to.__dict__
    
        invoice_information = V2paymentsOrderInformationInvoiceDetails()
        invoice_information.purchase_order_date = "20111231"
        invoice_information.purchase_order_number = "CREDIT US"
        order_information.invoice_details = invoice_information.__dict__
    
        merchant_details = V2paymentsMerchantInformation()
        merchant_details.category_code = 1234
        request.merchant_information = merchant_details.__dict__
    
        shipping_details = V2paymentsOrderInformationShippingDetails()
        shipping_details.ship_from_postal_code = "47404"
        order_information.shipping_details = shipping_details.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        refund_obj = RefundApi()
        refund_obj.refund_capture(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    follow_on_credit()
