from cybersource_rest_client_python import *
import json


def authorize_google_pay():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "33557799"
        request.client_reference_information = client_reference.__dict__

        processing_information = V2paymentsProcessingInformation()
        processing_information.payment_solution = "012"
        request.processing_information = processing_information.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "115.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "CYBS"
        bill_to.last_name = "TEST"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        order_information.bill_to = bill_to.__dict__
        request.order_information = order_information.__dict__

        payment_information = V2paymentsPaymentInformation()
        fluid_information = V2paymentsPaymentInformationFluidData()
        fluid_information.value = "eyJzaWduYXR1cmUiOiJNRVVDSVFEaFR4aEhxd1k4cFhCOWhwWXhhU0s1akZnc3FwRzJFMXJYNzdRWHNzSzh0QUlnVUJ2WVlBSS9ibkJTOFQvVGZ4bm0yQUY5ODFNdjV5MHBIeUdleE01ZE1Ka1x1MDAzZCIsInByb3RvY29sVmVyc2lvbiI6IkVDdjEiLCJzaWduZWRNZXNzYWdlIjoie1wiZW5jcnlwdGVkTWVzc2FnZVwiOlwib2R5VUdHQTdCK2JsbGV0WWNKYlM0M0FRVUZRSnBXRUZDTjRVdVVFeFE1TFgwXC9YY0x3S0VsWGNCOTVuTW5tUE85bE0yS0dwMTNGWXNMNzY4Y2NDekFqQkdMWUYrZnVnY0pUY3ZrclVoY05TeVhyN2h3ZjEyQkVzcndlcUpNNkk3VnM1bGZyUEF1a1JKZUxEUUc0RnhtVExXNDlReVA4dklaQyt0ejJjK1ozem96ekk1b0I5akU4ZkEyZG9sRmExM0N1NmdYcWRLSFwvSUhSaDdVbmlMVXVUeSswRzVGUVYycHdTVDJ1QlNOTmtaaGI4V1lKREhieEJqejBVZWJWUCtPYm1UNWNjOEFLVTVkZ0hSZGZyNEdLcEVaNEVCekI5MEJQeExxWUhwb3ByaUo2bGJGZ0ZWc1FRNlwvOEhCcVE3SW1JTUg1eTdHOHA4cUFGa1duQjc4WmNMMEZoNUJqWG9qa3hHb0ZwMmdqQXNyaGh0dEhBRmJlM1dRQnVQa3dKdTA5XC82XC9NeUpwQ1NycE1IRm91RlwvZGowU1lqUSt4STA5N2xDSFplYzdqUXJBaElTTFdaOURaa3VNdkdLUFdwdTBDS24yWHFUWFE9XCIsXCJlcGhlbWVyYWxQdWJsaWNLZXlcIjpcIk1Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRW5uNHlqeTBONnhsWE84XC84ajdcLzRqdm1MSkNZQXFnWEx3UDFGaGp1VGdJTTlvQ3RQaWpaZkk5c28yUUVPczJablZwM0QwZGwzSllJRFZlKzM5NktrQVE9PVwiLFwidGFnXCI6XCJEUnBjYytZUTMzUk5nc1RjeHp0bkpiTUpuaXJiVTVEVzNkU3RqZmhGaXdjPVwifSJ9"
        payment_information.fluid_data = fluid_information.__dict__
        request.payment_information = payment_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    authorize_google_pay()
