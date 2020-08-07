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

def authorization_with_customer_payment_instrument_and_shipping_address_token_id():
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationCustomerId = "AB695DA801DD1BB6E05341588E0A3BDC"
    paymentInformationCustomer = Ptsv2paymentsPaymentInformationCustomer(
        id = paymentInformationCustomerId
    )

    paymentInformationPaymentInstrumentId = "AB6A54B982A6FCB6E05341588E0A3935"
    paymentInformationPaymentInstrument = Ptsv2paymentsPaymentInformationPaymentInstrument(
        id = paymentInformationPaymentInstrumentId
    )

    paymentInformationShippingAddressId = "AB6A54B97C00FCB6E05341588E0A3935"
    paymentInformationShippingAddress = Ptsv2paymentsPaymentInformationShippingAddress(
        id = paymentInformationShippingAddressId
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        customer = paymentInformationCustomer.__dict__,
        payment_instrument = paymentInformationPaymentInstrument.__dict__,
        shipping_address = paymentInformationShippingAddress.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "102.21"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
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

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    authorization_with_customer_payment_instrument_and_shipping_address_token_id()
