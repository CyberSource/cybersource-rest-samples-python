from cybersource_rest_client_python import *
import json


def recurring_billing():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC45572-1"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "5432"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
    
        payment_information = V2paymentsPaymentInformation()
        customer = V2paymentsPaymentInformationCustomer()
        customer.customer_id = "5303162577043192705841"
        payment_information.customer = customer.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    recurring_billing()
