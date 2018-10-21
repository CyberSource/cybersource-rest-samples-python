from cybersource_rest_client_python import *
import json


def authorize_apple_pay():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "33557799"
        request.client_reference_information = client_reference.__dict__
    
        point_of_sale_information = V2paymentsPointOfSaleInformation()
        emv_info = V2paymentsPointOfSaleInformationEmv()
        point_of_sale_information.terminal_id = "terminal"
        point_of_sale_information.card_present = "Y"
        point_of_sale_information.entry_mode = "QRCode"
        point_of_sale_information.terminal_capability = 4
        emv_info.card_sequence_number = "123"
        emv_info.tags = "9C01019A031207109F33036040209F1A0207849F370482766E409F3602001F82025C009F2608EF7753429A5D16B19F100706010A03A00000950580000400009F02060000000700009F6E0482766E409F5B04123456789F2701809F3403AB12349F0902AB129F4104AB1234AB9F0702AB129F0610123456789012345678901234567890AB9F030200005F2A0207849F7C031234569F350123"
        point_of_sale_information.emv = emv_info.__dict__
        request.point_of_sale_information = point_of_sale_information.__dict__
    
        processing_information = V2paymentsProcessingInformation()
        processing_information.commerce_indicator = "retail"
        processing_information.payment_solution = "001"
        request.processing_information = processing_information.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.address2 = "test"
        bill_to.administrative_area = "MI"
        bill_to.phone_number = "999999999"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"
        bill_to.locality = "Ann Arbor"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__
    
        payment_information = V2paymentsPaymentInformation()
        tokenized_card = V2paymentsPaymentInformationTokenizedCard()
        tokenized_card.transaction_type = "1"
        tokenized_card.requestor_id = "12345678901"
        payment_information.tokenized_card = tokenized_card.__dict__
    
        card_info = V2paymentsPaymentInformationCard()
        card_info.type = "001"
        card_info.track_data = ";4111111111111111=21121019761186800000?"
        payment_information.card = card_info.__dict__
        request.payment_information = payment_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)




if __name__ == "__main__":
    authorize_apple_pay()
