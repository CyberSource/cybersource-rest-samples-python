from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

authorization_path = os.path.join(os.getcwd(), "samples", "Payments", "Payments", "authorization-for-incremental-authorization-flow.py")
authorization = SourceFileLoader("module.name", authorization_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def incremental_authorization():
    id = authorization.authorization_for_incremental_authorization_flow().id
    clientReferenceInformationPartnerOriginalTransactionId = "12345"
    clientReferenceInformationPartnerDeveloperId = "12345"
    clientReferenceInformationPartnerSolutionId = "12345"
    clientReferenceInformationPartner = Ptsv2paymentsidClientReferenceInformationPartner(
        original_transaction_id = clientReferenceInformationPartnerOriginalTransactionId,
        developer_id = clientReferenceInformationPartnerDeveloperId,
        solution_id = clientReferenceInformationPartnerSolutionId
    )

    clientReferenceInformation = Ptsv2paymentsidClientReferenceInformation(
        partner = clientReferenceInformationPartner.__dict__
    )

    processingInformationAuthorizationOptionsInitiatorStoredCredentialUsed = True
    processingInformationAuthorizationOptionsInitiator = Ptsv2paymentsidProcessingInformationAuthorizationOptionsInitiator(
        stored_credential_used = processingInformationAuthorizationOptionsInitiatorStoredCredentialUsed
    )

    processingInformationAuthorizationOptions = Ptsv2paymentsidProcessingInformationAuthorizationOptions(
        initiator = processingInformationAuthorizationOptionsInitiator.__dict__
    )

    processingInformation = Ptsv2paymentsidProcessingInformation(
        authorization_options = processingInformationAuthorizationOptions.__dict__
    )

    orderInformationAmountDetailsAdditionalAmount = "100"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidOrderInformationAmountDetails(
        additional_amount = orderInformationAmountDetailsAdditionalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantDescriptorContact = "965-6000"

    merchantInformationMerchantDescriptor = Ptsv2paymentsMerchantInformationMerchantDescriptor(
        contact = merchantDescriptorContact
    )

    merchantInformation = Ptsv2paymentsMerchantInformation(
        merchant_descriptor = merchantInformationMerchantDescriptor.__dict__
    )

    travelInformationDuration = "3"
    travelInformation = Ptsv2paymentsidTravelInformation(
        duration = travelInformationDuration
    )

    requestObj = IncrementAuthRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__,
        travel_information = travelInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_alternative_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.increment_auth(id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->increment_auth: %s\n" % e)

if __name__ == "__main__":
    incremental_authorization()
