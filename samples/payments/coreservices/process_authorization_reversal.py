from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.payments.coreservices.process_payment
import json



def process_an_authorization_reversal():
    try:
        api_payment_response=cybersource_rest_samples_python.samples.payments.coreservices.process_payment.process_a_payment(False)
        id = api_payment_response.id
        request = AuthReversalRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code =  "test_reversal"
        request.client_reference_information = client_reference.__dict__
    
        reversal_information = V2paymentsidreversalsReversalInformation()
        reversal_information.reason = "tes"
        amount_details = V2paymentsidreversalsReversalInformationAmountDetails()
        amount_details.total_amount = "102.21"
        reversal_information.amount_details = amount_details.__dict__
    
        request.reversal_information = reversal_information.__dict__
    
        message_body = json.dumps(request.__dict__)
    
        reversal_obj = ReversalApi()
    
        reversal_obj.auth_reversal(id, message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    process_an_authorization_reversal()
