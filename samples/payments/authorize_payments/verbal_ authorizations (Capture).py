from cybersource_rest_client_python import *
import json


def verbal_authorizations():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "1234567890"
        request.client_reference_information = client_reference.__dict__

        processing_information = V2paymentsProcessingInformation()
        processing_information.capture = "true"
        authorize_options = V2paymentsProcessingInformationAuthorizationOptions()
        authorize_options.auth_type = "verbal"
        authorize_options.verbal_auth_code = "potato"
        processing_information.authorization_options = authorize_options.__dict__
        request.processing_information = processing_information.__dict__
        order_information = V2paymentsOrderInformation()

        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.address1 = "901 Metro Center Blvd"
        bill_to.postal_code = "94404"
        bill_to.locality = "Foster City"
        bill_to.administrative_area = "CA"
        bill_to.email = "test@cybs.com"
        order_information.bill_to = bill_to.__dict__

        payment_information = V2paymentsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.number = "4111111111111111"
        payment_information.card = card_information.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    verbal_authorizations()
