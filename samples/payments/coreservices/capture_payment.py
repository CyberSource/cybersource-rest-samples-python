from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.payments.coreservices.process_payment

import json


def capture_a_payment():
    try:
        api_payment_response = cybersource_rest_samples_python.samples.payments.coreservices.process_payment.process_a_payment(False)
        id = api_payment_response.id
        request = CapturePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code = "test_capture"
        request.client_reference_information = client_reference.__dict__

        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"
        order_information = V2paymentsOrderInformation()
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        message_body = (json.dumps(request.__dict__))

        capture_obj = CaptureApi()
        return_data, status, body = capture_obj.capture_payment(message_body, id)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)


if __name__ == "__main__":
    capture_a_payment()
