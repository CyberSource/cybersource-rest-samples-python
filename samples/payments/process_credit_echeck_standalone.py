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

def process_credit_echeck_standalone():
    clientReferenceInformationCode = "TC46125-1"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCommerceIndicator = "internet"
    processingInformation = Ptsv2creditsProcessingInformation(
        commerce_indicator = processingInformationCommerceIndicator
    )

    paymentInformationBankAccountType = "C"
    paymentInformationBankAccountNumber = "4100"
    paymentInformationBankAccountCheckNumber = "123456"
    paymentInformationBankAccount = Ptsv2paymentsPaymentInformationBankAccount(
        type = paymentInformationBankAccountType,
        number = paymentInformationBankAccountNumber,
        check_number = paymentInformationBankAccountCheckNumber
    )

    paymentInformationBankRoutingNumber = "071923284"
    paymentInformationBank = Ptsv2paymentsPaymentInformationBank(
        account = paymentInformationBankAccount.__dict__,
        routing_number = paymentInformationBankRoutingNumber
    )

    paymentInformation = Ptsv2paymentsidrefundsPaymentInformation(
        bank = paymentInformationBank.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "100"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
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
    orderInformationBillTo = Ptsv2paymentsidcapturesOrderInformationBillTo(
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

    orderInformation = Ptsv2paymentsidrefundsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    requestObj = CreateCreditRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CreditApi(client_config)
        return_data, status, body = api_instance.create_credit(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling CreditApi->create_credit: %s\n" % e)

if __name__ == "__main__":
    process_credit_echeck_standalone()
