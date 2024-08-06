from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
        elif isinstance(value, list):
            for item in value:
                del_none(item)
    return d

def bin_lookup_with_tms_payment_instrument():
    paymentInformationPaymentInstrumentId = "E5427539180789D0E053A2598D0AF053"
    paymentInformationPaymentInstrument = Ptsv2paymentsPaymentInformationPaymentInstrument(
        id = paymentInformationPaymentInstrumentId
    )

    paymentInformation = Binv1binlookupPaymentInformation(
        payment_instrument = paymentInformationPaymentInstrument.__dict__
    )

    requestObj = CreateBinLookupRequest(
        payment_information = paymentInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = BinLookupApi(client_config)
        return_data, status, body = api_instance.get_account_info(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling BinLookupApi->get_account_info: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    bin_lookup_with_tms_payment_instrument()