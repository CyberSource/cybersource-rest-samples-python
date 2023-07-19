from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

process_credit_path = os.path.join(os.getcwd(), "samples", "Payments", "Credit", "ebt-merchandise-return-credit-voucher-from-snap.py")
process_credit = SourceFileLoader("module.name", process_credit_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def ebt_reversal_of_purchase_from_snap_account():
    clientReferenceInformationCode = "Reversal of Purchase from SNAP Account"
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

    orderInformationAmountDetailsTotalAmount = "204.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidreversalsReversalInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidvoidsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = VoidPaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        api_credit_response = process_credit.ebt_merchandise_return_credit_voucher_from_snap()
        id = api_credit_response.id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_alternative_configuration()
        api_instance = VoidApi(client_config)
        return_data, status, body = api_instance.void_payment(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling VoidApi->void_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    ebt_reversal_of_purchase_from_snap_account()