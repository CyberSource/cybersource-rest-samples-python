from CyberSource import *
import create_instrument_identifier
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def retrieve_all_payments():
    try:
        # Getting the api_instrument_identifier_response-id dynamically using create_instrument_identifier method
        api_instrument_identifier_response = create_instrument_identifier.create_instrument_identifier()
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier = InstrumentIdentifierApi(details_dict1)
        return_data, status, body = instrument_identifier.get_all_payment_instruments(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_instrument_identifier_response.id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)


    except Exception as e:
        print(
            "Exception when calling InstrumentIdentifierApi->get_all_payment_instruments: %s\n" % e)


if __name__ == "__main__":
    retrieve_all_payments()
