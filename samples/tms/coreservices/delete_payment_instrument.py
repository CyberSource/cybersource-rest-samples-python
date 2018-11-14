from CyberSource import *
import retrieve_payment_instrument
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()

def remove_payment_instruments():
    try:
        api_payment_response=retrieve_payment_instrument.retrieve_payment_instrument()
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        payment_instrument_obj = PaymentInstrumentsApi(details_dict1)
        return_data, status, body =payment_instrument_obj.tms_v1_paymentinstruments_token_id_delete("93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
        print(status)
        print(body)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    remove_payment_instruments()
