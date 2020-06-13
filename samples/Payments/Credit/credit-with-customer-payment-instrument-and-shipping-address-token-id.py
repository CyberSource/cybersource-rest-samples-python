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

def credit_with_customer_payment_instrument_and_shipping_address_token_id():
    clientReferenceInformationCode = "12345678"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationCustomerId = "7500BB199B4270EFE05340588D0AFCAD"
    paymentInformationCustomer = Ptsv2paymentsPaymentInformationCustomer(
        id = paymentInformationCustomerId
    )

    paymentInformationPaymentInstrumentId = "7500BB199B4270EFE05340588D0AFCPI"
    paymentInformationPaymentInstrument = Ptsv2paymentsPaymentInformationPaymentInstrument(
        id = paymentInformationPaymentInstrumentId
    )

    paymentInformationShippingAddressId = "7500BB199B4270EFE05340588D0AFCSA"
    paymentInformationShippingAddress = Ptsv2paymentsPaymentInformationShippingAddress(
        id = paymentInformationShippingAddressId
    )

    paymentInformation = Ptsv2paymentsidrefundsPaymentInformation(
        customer = paymentInformationCustomer.__dict__,
        payment_instrument = paymentInformationPaymentInstrument.__dict__,
        shipping_address = paymentInformationShippingAddress.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "200"
    orderInformationAmountDetailsCurrency = "usd"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidrefundsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = CreateCreditRequest(
        client_reference_information = clientReferenceInformation.__dict__,
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

        return return_data
    except Exception as e:
        print("\nException when calling CreditApi->create_credit: %s\n" % e)

if __name__ == "__main__":
    credit_with_customer_payment_instrument_and_shipping_address_token_id()
