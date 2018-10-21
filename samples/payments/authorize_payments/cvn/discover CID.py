from cybersource_rest_client_python import *
import json


def discover_CID():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "1234567890"
        request.client_reference_information = client_reference.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "2839.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.phone_number = "6504327113"
        bill_to.address2 = "Desk M3-5573"
        bill_to.address1 = "901 Metro Center Blvd"
        bill_to.postal_code = "94404"
        bill_to.locality = "Foster City"
        bill_to.company = "Visa"
        bill_to.administrative_area = "CA"
        bill_to.email = "test@cybs.com"
        order_information.bill_to = bill_to.__dict__

        payment_information = V2paymentsidrefundsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.number = "6011111111111117"
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
    discover_CID()
