from cybersource_rest_client_python import *
import json


def create_instrument_identifier():
    try:
        request = Body()
    
        card_info = InstrumentidentifiersCard()
        card_info.number = "1234567890987"
        request.card = card_info.__dict__
    
        processing_info = InstrumentidentifiersProcessingInformation()
        authorize_options_info = InstrumentidentifiersProcessingInformationAuthorizationOptions()
        initiator = InstrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
        merchant_initiated_info = InstrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()
        merchant_initiated_info.previous_transaction_id = "123456789012345"
        initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
        authorize_options_info.initiator = initiator.__dict__
        processing_info.authorization_options = authorize_options_info.__dict__
        request.processing_information = processing_info.__dict__
    
        message_body =del_none(request.__dict__)
        
        message_body=json.dumps(message_body)
        instrument_identifier_obj = InstrumentIdentifierApi()
        return_data, status, body =instrument_identifier_obj.instrumentidentifiers_post("93B32398-AD51-4CC2-A682-EA3E93614EB1", body=message_body)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

if __name__ == "__main__":
    create_instrument_identifier()
