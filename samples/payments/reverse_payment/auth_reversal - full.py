from cybersource_rest_client_python import *
import json



def auth_reversal():
    try:
        id = "5378548266906856003003"
        request = AuthReversalRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_1"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details_order = V2paymentsOrderInformationAmountDetails()
        amount_details_reversal = V2paymentsidreversalsReversalInformationAmountDetails()
        amount_details_order.currency = "USD"
        order_information.amount_details = amount_details_order.__dict__
    
        reversal_information = V2paymentsidreversalsReversalInformation()
        amount_details_reversal.total_amount = "102.21"
        reversal_information.amount_details = amount_details_reversal.__dict__
        request.order_information = order_information.__dict__
        request.reversal_information = reversal_information.__dict__
        
        message_body = json.dumps(request.__dict__)
        reversal_obj = ReversalApi()
        reversal_obj.auth_reversal(id, message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    auth_reversal()
