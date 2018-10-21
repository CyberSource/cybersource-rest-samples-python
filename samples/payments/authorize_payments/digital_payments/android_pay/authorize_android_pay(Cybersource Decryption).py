from cybersource_rest_client_python import *
import json


def authorize_android_pay():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC_MPOS_Paymentech_1"
        request.client_reference_information = client_reference.__dict__

        processing_information = V2paymentsProcessingInformation()
        processing_information.payment_solution = "006"
        request.processing_information = processing_information.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__

        payment_information = V2paymentsPaymentInformation()
        fluid_information = V2paymentsPaymentInformationFluidData()
        fluid_information.value = "ewoJInB1YmxpY0tleUhhc2giICAgIDogIlNKU1NSN0Q4VHZxbHBPWmcwMFhWY1pYclI1czJBUTJxYU8rK0VTVnl4clU9IiwKCSJ2ZXJzaW9uIjogIjEuMCIsCgkiZGF0YSIgOiAiZXdvSkltVnVZM0o1Y0hSbFpFMWxjM05oWjJVaU9pQWlSbFZrUjNWQlFWVlpRVWd2VXpreU1rczNXVE5QTm5VclpsWXJlbU5wUjBwamN6SkRPVVJ1Ykd0TlYyZzJZa2hVS3pCd2FsTTJjbkZJTDFoTWVYcGlSVTg1WWtsdkwyUmtUbTEzYVRGblRqbEVZV1Y2Y3pOdlpFNXVValZ0Ykd4MlIzWktNRVpYU0ZKeVRTOVRabVF6TlRZeVlqaFNObFpST1ZwS1ZUTmFNMXBDT0ZSWmFtdGpiWGhVTHpkSWQwaHdVWGgxUmpaT2JXZHNWMmwwVnk5VU0ya3dSVE5QV1dwUkswZGtWbTFZTVVOaVoxbHNlWHBRTVVOSWFrNXdUV3RxVUhvMGVrTlVibUpHTmxGc1pIWkxaVFJvYkhselpuZ3pPVzlwVEU5YVIxcG9SSGhVVDNwU2VXUXhWekl6VVQwOUlpd0tDU0psY0dobGJXVnlZV3hRZFdKc2FXTkxaWGtpT2lBaVRVWnJkMFYzV1VoTGIxcEplbW93UTBGUldVbExiMXBKZW1vd1JFRlJZMFJSWjBGRmJ6RnlUMnBGU2t4SUsxWk1VRGQwUkV4YVdHSnBia2xaWWtjeVYwOXZjMDlDZWs5TVMyVkRiMU5ZVm1KSk9XNTBjWFpHT1dKelRtRlhOWEJYUkRsbFdsUXZXSHBHZURoTGIwdEROVmhOYVRSblZXWkdRMUU5UFNJc0Nna2lkR0ZuSWpvZ0lrVkRkRFZwVW1kM1VscGxMM2hJWlRCSU1rMXJhRUpGTXpSM1dYVXllVFJKZG13ME5uUjRXSFlyVjFFOUlncDkiCn0="
        payment_information.fluid_data = fluid_information.__dict__
        request.payment_information = payment_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    authorize_android_pay()
