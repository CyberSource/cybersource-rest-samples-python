from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def payment_with_flex_transient_token(flag):

    clientReferenceInformationCode = "GABRIEL TEST"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsTotalAmount = "20.50"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )


    processingInformationCapture = False
    if flag:
        processingInformationCapture = True

    processingInformationActionList = []
    processingInformationActionList.append("TOKEN_CREATE")

    # Valid values: - customer - paymentInstrument - instrumentIdentifier - shippingAddress 
    processingInformationActionTokenTypes = []
    processingInformationActionTokenTypes.append("customer")
    processingInformationActionTokenTypes.append("paymentInstrument")
    processingInformationActionTokenTypes.append("instrumentIdentifier")
    #processingInformationActionTokenTypes.append("shippingAddress")

    processingInformationCommerceIndicator = "internet"
    processingInformation = Ptsv2paymentsProcessingInformation(
        action_list = processingInformationActionList,   
        action_token_types = processingInformationActionTokenTypes,
        capture = processingInformationCapture,
        commerce_indicator = processingInformationCommerceIndicator
    )

    paymentInformationCardExpirationMonth = "10"
    paymentInformationCardExpirationYear = "2032"  
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,

    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__
    ) 

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "4158880000"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    tokenInformationTransientTokenJwt = "eyJraWQiOiIwOEdubjhMNDBZaEI1Ymk2aFg2UzJYMkRQaFZXQ3dZYSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjp7Im51bWJlciI6IjQxMTExMVhYWFhYWDExMTEiLCJ0eXBlIjoiMDAxIn0sImlzcyI6IkZsZXgvMDgiLCJleHAiOjE1OTY3ODE2MTMsInR5cGUiOiJtZi0wLjExLjAiLCJpYXQiOjE1OTY3ODA3MTMsImp0aSI6IjFFMjVFSkg4UUY0WE4yTEE3NUNGQjI0MkswN0lBRkFaQlFSVDlGTkdQWkFOTU9EWEhQMk81RjJDRjQyRDFGRDQifQ.pHWKwcpt_es3Qn78ZaFGgcc2g5iyZXCMvPOjaVoU6z0tKgExYd2GbZaBsIB4aV80RE4B5WlTcYIleokSbRQGy-kVbD48optXY4tgh4-nYVleyqz-eZr9o3diOHZRUujHXMtjjqTW0h5mu1mMX0UzGnWuBLx3xRkZgsvv9lO7VMiMQosO2oiajDQS6Ts8UHa6727jfXUTKNcrGrPIsIuZdiRXRfWQxH3X0YJ48zn-_YV3hOBLeiRXWwfPxsYKy5IKpc4RgOnUGC0HplUC8cDkKmtUnryhVVhfPrPjRMHqvyOU5x2wuLEcmN6MLsfSDVfuK1NmSVyNHa7BNXv37OOOCQ"
    tokenInformation = Ptsv2paymentsTokenInformation(
        transient_token_jwt = tokenInformationTransientTokenJwt
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        token_information = tokenInformation.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RETURN DATA : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)
		

if __name__ == "__main__":
    payment_with_flex_transient_token(False)
