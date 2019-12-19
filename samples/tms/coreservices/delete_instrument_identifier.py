from CyberSource import *
import retrieve_instrument_identifier
import os, time
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def remove_instrument_identifiers():
    try:
        # Getting the api_instrument_response-id dynamically using retrieve_instrument_identifier method
        api_instrument_response = retrieve_instrument_identifier.retrieve_instrument_identifier()
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier_obj = InstrumentIdentifierApi(details_dict1)
        return_data, status, body = instrument_identifier_obj.delete_instrument_identifier(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_instrument_response.id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

    except Exception as e:
        print("Exception when calling InstrumentIdentifierApi->delete_instrument_identifier: %s\n" % e)


if __name__ == "__main__":
    remove_instrument_identifiers()
