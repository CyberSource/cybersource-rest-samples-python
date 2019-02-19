from CyberSource import *
import create_instrument_identifier
import os
import json
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def retrieve_instrument_identifier():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Getting the api_instrument_identifier_response-id dynamically using create_instrument_identifier method
        api_instrument_identifier_response = create_instrument_identifier.create_instrument_identifier()
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier = InstrumentIdentifierApi(details_dict1)
        response_data = instrument_identifier.tms_v1_instrumentidentifiers_token_id_get(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_instrument_identifier_response['id'])
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        return json.loads(response_data.data)
    except Exception as e:
        print("\nException when calling InstrumentIdentifierApi->tms_v1_instrumentidentifiers_token_id_get: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    retrieve_instrument_identifier()
