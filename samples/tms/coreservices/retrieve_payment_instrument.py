from CyberSource import *
import create_payment_instrument
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def retrieve_payment_instrument():
    try:
        # Getting the api_payment_response-id dynamically using create_payment_instrument method
        api_payment_response = create_payment_instrument.create_payment_instrument()
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        payment_instruments = PaymentInstrumentsApi(details_dict1)
        return_data, status, body = payment_instruments.tms_v1_paymentinstruments_token_id_get(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data
    except Exception as e:
        print("Exception when calling PaymentInstrumentsApi->tms_v1_paymentinstruments_token_id_get: %s\n" % e)


if __name__ == "__main__":
    retrieve_payment_instrument()
