from CyberSource import *
from pathlib import Path
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

def update_instrument_identifier_previoustransactionid():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    instrumentIdentifierTokenId = "7010000000016241111"

    processingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransactionPreviousTransactionId = "123456789012345"
    processingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction = Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction(
        previous_transaction_id = processingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransactionPreviousTransactionId
    )

    processingInformationAuthorizationOptionsInitiator = Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptionsInitiator(
        merchant_initiated_transaction = processingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.__dict__
    )

    processingInformationAuthorizationOptions = Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformationAuthorizationOptions(
        initiator = processingInformationAuthorizationOptionsInitiator.__dict__
    )

    processingInformation = Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierProcessingInformation(
        authorization_options = processingInformationAuthorizationOptions.__dict__
    )

    requestObj = PatchInstrumentIdentifierRequest(
        processing_information = processingInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InstrumentIdentifierApi(client_config)
        return_data, status, body = api_instance.patch_instrument_identifier(instrumentIdentifierTokenId, requestObj, profile_id=profileid)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling InstrumentIdentifierApi->patch_instrument_identifier: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    update_instrument_identifier_previoustransactionid()
