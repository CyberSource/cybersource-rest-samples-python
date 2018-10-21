from cybersource_rest_client_python import *
import json


def partial_bills():
    try:
        id = "5359746706806069103005"
        request = CapturePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "1234567890"
        request.client_reference_information = client_reference.__dict__
    
        point_of_sale_info = V2paymentsPointOfSaleInformation()
        point_of_sale_info.cat_level = 6
        point_of_sale_info.card_present = "false"
        point_of_sale_info.terminal_capability = 4
        request.point_of_sale_information = point_of_sale_info.__dict__
    
        order_information = V2paymentsidcapturesOrderInformation()
        amount_details = V2paymentsidcapturesOrderInformationAmountDetails()
        amount_details.total_amount = "10.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
    
        bill_to = V2paymentsidcapturesOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.address1 = "901 Metro Center Blvd"
        bill_to.postal_code = "40500"
        bill_to.locality = "Foster City"
        bill_to.administrative_area = "CA"
        bill_to.email = "test@cybs.com"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
        capture_obj = CaptureApi()
        capture_obj.capture_payment(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    partial_bills()
