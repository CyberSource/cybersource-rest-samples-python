from cybersource_rest_client_python import *
import json


def auth_reversal():
    try:
        id = "5377974074306589303004"
        request=AuthReversalRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_1"
        request.client_reference_information = client_reference.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        reversal_info = V2paymentsidreversalsReversalInformation()
        reversal_amount_details = V2paymentsidreversalsReversalInformationAmountDetails()
        reversal_amount_details.total_amount = "102.21"
        reversal_info.amount_details = reversal_amount_details.__dict__
        request.reversal_information = reversal_info.__dict__

        message_body = json.dumps(request.__dict__)
        auth_obj = ReversalApi()
        auth_obj.auth_reversal(id, message_body)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    auth_reversal()
