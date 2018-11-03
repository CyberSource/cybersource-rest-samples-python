from CyberSource import *
import create_payment_instrument
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def retrieve_payment_instrument():
    try:
        api_payment_response=create_payment_instrument.create_payment_instrument()
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        payment_instruments = PaymentInstrumentApi(details_dict1)
        return_data, status, body =payment_instruments.paymentinstruments_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_payment_instrument()
