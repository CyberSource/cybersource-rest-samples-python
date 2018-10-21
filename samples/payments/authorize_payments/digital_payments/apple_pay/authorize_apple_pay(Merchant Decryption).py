from cybersource_rest_client_python import *
import json


def authorize_apple_pay():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC_MPOS_Paymentech_2"
        request.client_reference_information = client_reference.__dict__

        processing_information = V2paymentsProcessingInformation()
        processing_information.payment_solution = "001"
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
        bill_to.company = "Visa"
        bill_to.administrative_area = "CA"
        bill_to.email = "test@cybs.com"
        bill_to.phone_number = "6504327113"
        bill_to.address2 = "Desk M3-5573"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__

        payment_information = V2paymentsPaymentInformation()
        tokenized_card = V2paymentsPaymentInformationTokenizedCard()
        tokenized_card.expiration_year = "2031"
        tokenized_card.number = "4111111111111111"
        tokenized_card.expiration_month = "12"
        tokenized_card.transaction_type = "1"
        tokenized_card.cryptogram = "AceY+igABPs3jdwNaDg3MAACAAA="
        payment_information.tokenized_card = tokenized_card.__dict__
        request.payment_information = payment_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    authorize_apple_pay()
