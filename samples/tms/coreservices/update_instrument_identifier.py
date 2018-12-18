from CyberSource import *
import retrieve_instrument_identifier
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def update_instrument_identifier():
    try:
        # Getting the api_instrument_identifier_response-id dynamically using retrieve_instrument_identifier method
        api_instrument_identifier_response = retrieve_instrument_identifier.retrieve_instrument_identifier()
        # Setting the json message body
        request = Body1()
        processing_info = Tmsv1instrumentidentifiersProcessingInformation()
        authorize_options_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptions()
        initiator = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiator()
        merchant_initiated_info = Tmsv1instrumentidentifiersProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction()

        merchant_initiated_info.previous_transaction_id = "123456789012345"
        initiator.merchant_initiated_transaction = merchant_initiated_info.__dict__
        authorize_options_info.initiator = initiator.__dict__
        processing_info.authorization_options = authorize_options_info.__dict__
        request.processing_information = processing_info.__dict__
        message_body = del_none(request.__dict__)
        message_body = json.dumps(message_body)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier_obj = InstrumentIdentifierApi(details_dict1)
        return_data, status, body = instrument_identifier_obj.tms_v1_instrumentidentifiers_token_id_patch(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_instrument_identifier_response.id, body=message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

    except Exception as e:
        print("Exception when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_patch: %s\n" % e)

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


if __name__ == "__main__":
    update_instrument_identifier()
