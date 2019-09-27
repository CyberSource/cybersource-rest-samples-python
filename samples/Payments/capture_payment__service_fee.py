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

def capture_payment__service_fee(id):
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsTotalAmount = "2325.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsServiceFeeAmount = "30.0"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency,
        service_fee_amount = orderInformationAmountDetailsServiceFeeAmount
    )

    orderInformation = Ptsv2paymentsidcapturesOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantInformationServiceFeeDescriptorName = "Vacations Service Fee"
    merchantInformationServiceFeeDescriptorContact = "8009999999"
    merchantInformationServiceFeeDescriptorState = "CA"
    merchantInformationServiceFeeDescriptor = Ptsv2paymentsMerchantInformationServiceFeeDescriptor(
        name = merchantInformationServiceFeeDescriptorName,
        contact = merchantInformationServiceFeeDescriptorContact,
        state = merchantInformationServiceFeeDescriptorState
    )

    merchantInformation = Ptsv2paymentsidcapturesMerchantInformation(
        service_fee_descriptor = merchantInformationServiceFeeDescriptor.__dict__
    )

    requestObj = CapturePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CaptureApi(client_config)
        return_data, status, body = api_instance.capture_payment(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling CaptureApi->capture_payment: %s\n" % e)

if __name__ == "__main__":
    print("\nInput missing path parameter <id>:")
    id = input()

    capture_payment__service_fee(id)
