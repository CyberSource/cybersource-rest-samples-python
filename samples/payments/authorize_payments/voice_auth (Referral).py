from cybersource_rest_client_python import *
import json


def voice_auth():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC1102345"
        request.client_reference_information = client_reference.__dict__
    
        device_info = V2paymentsDeviceInformation()
        device_info.host_name = "cybersource.com"
        device_info.ip_address = "66.185.179.2"
        request.device_information = device_info.__dict__
    
        buyer_information = V2paymentsBuyerInformation()
        personal_info = V2paymentsBuyerInformationPersonalIdentification()
        personal_info.id = "123* 4"
        buyer_information.personal_identification = personal_info.__dict__
        request.buyer_information = buyer_information.__dict__
    
        processing_info = V2paymentsProcessingInformation()
        authorize_options = V2paymentsProcessingInformationAuthorizationOptions()
        authorize_options.ignore_avs_result = "Y"
        authorize_options.ignore_cv_result = "N"
        processing_info.authorization_options = authorize_options.__dict__
        request.processing_information = processing_info.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "2401"
        amount_details.currency = "usd"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.phone_number = "999999999"
        bill_to.address2 = "test"
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
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.type = "003"
        card_information.number = "372425119311008"
        card_information.security_code = "1111"
        card_information.security_code_indicator = "1"
        payment_information.card = card_information.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    voice_auth()
