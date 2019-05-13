from CyberSource import *
import retrieve_payment_instrument
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def remove_payment_instruments():
    try:
        # Getting the api_payment_response-id dynamically using retrieve_payment_instrument method
        api_payment_response = retrieve_payment_instrument.retrieve_payment_instrument()
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        payment_instrument_obj = PaymentInstrumentApi(details_dict1)
        return_data, status, body = payment_instrument_obj.delete_payment_instrument(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

    except Exception as e:
        print("Exception when calling PaymentInstrumentApi->delete_payment_instrument: %s\n" % e)


if __name__ == "__main__":
    remove_payment_instruments()
