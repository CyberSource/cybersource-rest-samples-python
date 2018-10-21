from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.tms.coreservices.create_instrument_identifier
import json

def update_instrument_identifier():
    try:
        api_instrument_identifier_response=cybersource_rest_samples_python.samples.tms.coreservices.create_instrument_identifier.create_instrument_identifier()
        request = Body1()

        processing_info = InstrumentidentifiersProcessingInformation()
        authorize_options_info = InstrumentidentifiersProcessingInformationAuthorizationOptions()
        initiator = InstrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
        merchant_initiated_info = InstrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()
        merchant_initiated_info.previous_transaction_id = "123456789012345"
        initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
        authorize_options_info.initiator = initiator.__dict__
        processing_info.authorization_options = authorize_options_info.__dict__
        request.processing_information = processing_info.__dict__
        message_body = json.dumps(request.__dict__)
        instrument_identifier_obj = InstrumentIdentifierApi()
        instrument_identifier_obj.instrumentidentifiers_token_id_patch("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_instrument_identifier_response.id,body=message_body)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    update_instrument_identifier()
