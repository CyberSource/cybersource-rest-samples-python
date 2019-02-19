from CyberSource import *
import retrieve_instrument_identifier
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def update_instrument_identifier():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
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

        message_body = json.dumps(request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier_obj = InstrumentIdentifierApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = instrument_identifier_obj.tms_v1_instrumentidentifiers_token_id_patch(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_instrument_identifier_response['id'], body=message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

    except Exception as e:
        print("\nException when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_patch: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)



if __name__ == "__main__":
    update_instrument_identifier()
