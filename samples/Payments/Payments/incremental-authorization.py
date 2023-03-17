from CyberSource import *
from pathlib import Path
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
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsidClientReferenceInformation(
        code = clientReferenceInformationCode
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

    orderInformationAmountDetailsAdditionalAmount = "22.49"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidOrderInformationAmountDetails(
        additional_amount = orderInformationAmountDetailsAdditionalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantInformationTransactionLocalDateTime = "20191002080000"
    merchantInformation = Ptsv2paymentsidMerchantInformation(
        transaction_local_date_time = merchantInformationTransactionLocalDateTime
    )

    travelInformationDuration = "4"
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PaymentsApi->increment_auth: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    incremental_authorization()
