from cybersource_rest_client_python import *
import json


def refund_payment():
    try:
        id = "5362159058876742904002"
        request = RefundPaymentRequest()
        processing_information = V2paymentsProcessingInformation()
        processing_information.capture = "true"
        request.processing_information = processing_information.__dict__
        order_information = V2paymentsOrderInformation()
    
        order_info_line_items = V2paymentsidrefundsOrderInformationLineItems()
        order_info_line_items.unit_price = "100.00"
        order_info_line_items.discount_rate = "0.013"
        order_info_line_items.quantity = 2
        order_info_line_items.unit_of_measure = "inch"
        order_info_line_items.discount_amount = "10"
        order_info_line_items.tax_applied_after_discount = "8"
        order_info_line_items.amount_includes_tax = "y"
        order_info_line_items.discount_applied = "y"
        order_info_line_items.product_name = "PName0"
        order_info_line_items.tax_rate = "0.082"
        order_info_line_items.total_amount = "1100"
        order_info_line_items.product_sku = "testdl"
        order_info_line_items.product_code = "clothing"
        order_info_line_items.commodity_code = "987654321012"
        order_info_line_items.tax_amount = "20.00"
        order_information.line_items = order_info_line_items.__dict__
    
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100.00"
        amount_details.currency = "usd"
        amount_details.exchange_rate = "0.5"
        amount_details.exchange_rate_time_stamp = "2.01304E+13"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "John"
        bill_to.last_name = "Test"
        bill_to.phone_number = "9999999"
        bill_to.address2 = "test2"
        bill_to.address1 = "test"
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.company = "Visa"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        order_information.bill_to = bill_to.__dict__
    
        ship_to = V2paymentsOrderInformationShipTo()
        ship_to.country = "US"
        ship_to.address2 = "test2"
        ship_to.address1 = "test"
        ship_to.postal_code = "48104-2202"
        ship_to.administrative_area = "MI"
        order_information.ship_to = ship_to.__dict__
    
        shipping_details = V2paymentsOrderInformationShippingDetails()
        shipping_details.ship_from_postal_code = "47404"
        order_information.shipping_details = shipping_details.__dict__
    
        payment_information = V2paymentsidrefundsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.type = "002"
        card_information.number = "5555555555554444"
        card_information.security_code = "123"
        payment_information.card = card_information.__dict__
        request.payment_information=payment_information.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        refund_obj=RefundApi()
        refund_obj.refund_payment(message_body,id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    refund_payment()
