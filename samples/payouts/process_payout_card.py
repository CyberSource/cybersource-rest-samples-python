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

def process_payout_card():
    clientReferenceInformationCode = "33557799"
    clientReferenceInformation = Ptsv2payoutsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsTotalAmount = "100.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2payoutsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2payoutsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantInformationMerchantDescriptorName = "Sending Company Name"
    merchantInformationMerchantDescriptorLocality = "FC"
    merchantInformationMerchantDescriptorCountry = "US"
    merchantInformationMerchantDescriptorAdministrativeArea = "CA"
    merchantInformationMerchantDescriptorPostalCode = "94440"
    merchantInformationMerchantDescriptor = Ptsv2payoutsMerchantInformationMerchantDescriptor(
        name = merchantInformationMerchantDescriptorName,
        locality = merchantInformationMerchantDescriptorLocality,
        country = merchantInformationMerchantDescriptorCountry,
        administrative_area = merchantInformationMerchantDescriptorAdministrativeArea,
        postal_code = merchantInformationMerchantDescriptorPostalCode
    )

    merchantInformation = Ptsv2payoutsMerchantInformation(
        merchant_descriptor = merchantInformationMerchantDescriptor.__dict__
    )

    recipientInformationFirstName = "John"
    recipientInformationLastName = "Doe"
    recipientInformationAddress1 = "Paseo Padre Boulevard"
    recipientInformationLocality = "Foster City"
    recipientInformationAdministrativeArea = "CA"
    recipientInformationCountry = "US"
    recipientInformationPostalCode = "94400"
    recipientInformationPhoneNumber = "6504320556"
    recipientInformation = Ptsv2payoutsRecipientInformation(
        first_name = recipientInformationFirstName,
        last_name = recipientInformationLastName,
        address1 = recipientInformationAddress1,
        locality = recipientInformationLocality,
        administrative_area = recipientInformationAdministrativeArea,
        country = recipientInformationCountry,
        postal_code = recipientInformationPostalCode,
        phone_number = recipientInformationPhoneNumber
    )

    senderInformationReferenceNumber = "1234567890"
    senderInformationAccountFundsSource = "05"
    senderInformationAccount = Ptsv2payoutsSenderInformationAccount(
        funds_source = senderInformationAccountFundsSource
    )

    senderInformationName = "Company Name"
    senderInformationAddress1 = "900 Metro Center Blvd.900"
    senderInformationLocality = "Foster City"
    senderInformationAdministrativeArea = "CA"
    senderInformationCountryCode = "US"
    senderInformation = Ptsv2payoutsSenderInformation(
        reference_number = senderInformationReferenceNumber,
        account = senderInformationAccount.__dict__,
        name = senderInformationName,
        address1 = senderInformationAddress1,
        locality = senderInformationLocality,
        administrative_area = senderInformationAdministrativeArea,
        country_code = senderInformationCountryCode
    )

    processingInformationBusinessApplicationId = "FD"
    processingInformationNetworkRoutingOrder = "V8"
    processingInformationCommerceIndicator = "internet"
    processingInformation = Ptsv2payoutsProcessingInformation(
        business_application_id = processingInformationBusinessApplicationId,
        network_routing_order = processingInformationNetworkRoutingOrder,
        commerce_indicator = processingInformationCommerceIndicator
    )

    paymentInformationCardType = "001"
    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2025"
    paymentInformationCard = Ptsv2payoutsPaymentInformationCard(
        type = paymentInformationCardType,
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformation = Ptsv2payoutsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    requestObj = OctCreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__,
        recipient_information = recipientInformation.__dict__,
        sender_information = senderInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayoutsApi(client_config)
        return_data, status, body = api_instance.oct_create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling PayoutsApi->oct_create_payment: %s\n" % e)

if __name__ == "__main__":
    process_payout_card()
