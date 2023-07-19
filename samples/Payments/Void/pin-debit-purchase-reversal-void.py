from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

process_payment_path = os.path.join(os.getcwd(), "samples", "Payments", "Payments", "pin-debit-purchase-using-swiped-track-data-with-visa-platform-connect.py")
process_payment = SourceFileLoader("module.name", process_payment_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def pin_debit_purchase_reversal_void():
    clientReferenceInformationCode = "Pin Debit Purchase Reversal(Void)"
    clientReferenceInformation = Ptsv2paymentsidreversalsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationPaymentTypeName = "CARD"
    paymentInformationPaymentTypeSubTypeName = "DEBIT"
    paymentInformationPaymentType = Ptsv2paymentsidrefundsPaymentInformationPaymentType(
        name = paymentInformationPaymentTypeName,
        sub_type_name = paymentInformationPaymentTypeSubTypeName
    )

    paymentInformation = Ptsv2paymentsidvoidsPaymentInformation(
        payment_type = paymentInformationPaymentType.__dict__
    )

    amountDetailsTotalAmount = "202.00"
    amountDetailsCurrency = "USD"
    amountDetails = Ptsv2paymentsidreversalsReversalInformationAmountDetails(
        total_amount = amountDetailsTotalAmount,
        currency = amountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidvoidsOrderInformation(
        amount_details = amountDetails.__dict__
    )

    requestObj = VoidPaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        api_payment_pin_debit_response = process_payment.pin_debit_purchase_using_swiped_track_data_with_visa_platform_connect()
        id = api_payment_pin_debit_response.id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_alternative_configuration()
        api_instance = VoidApi(client_config)
        return_data, status, body = api_instance.void_payment(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling VoidApi->void_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    pin_debit_purchase_reversal_void()
