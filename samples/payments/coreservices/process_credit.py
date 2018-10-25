from cybersource_rest_client_python import *
import json


def process_a_credit():
    try:

        request = CreateCreditRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code = "test_credits"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "200"
        amount_details.currency = "usd"
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "John"
        bill_to.last_name = "Doe"
        bill_to.address1 = "1 Market St"
        bill_to.phone_number = "9999999999"
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        order_information.amount_details = amount_details.__dict__
        order_information.bill_to = bill_to.__dict__
    
        payment_information = V2paymentsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "03"
        card_information.expiration_year = "2031"
        card_information.type = "001"
        card_information.number = "4111111111111111"
        payment_information.card = card_information.__dict__
        request.order_information = order_information.__dict__
        request.payment_information=payment_information.__dict__
        message_body = json.dumps(request.__dict__)
    
        credit_obj=CreditApi()
        return_data, status, body =credit_obj.create_credit(message_body)
        print(status)
        print(body)
        return return_data

    except Exception as e:
        print(e)

if __name__ == "__main__":
    process_a_credit()
