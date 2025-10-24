from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "ConfigurationForBankAccountValidation.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def bank_account_validation(flag):
    clientReferenceInformationCode = "TC50171_100";
    clientReferenceInformation = Bavsv1accountvalidationsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationValidationLevel = 1
    processingInformation = Bavsv1accountvalidationsProcessingInformation(
        validation_level = processingInformationValidationLevel
    )

    paymentInformationBankAccountNumber = "99970"
    paymentInformationBankAccount = Bavsv1accountvalidationsPaymentInformationBankAccount(
        number = paymentInformationBankAccountNumber
    )
    paymentInformationBankRoutingNumber = "041210163"
    paymentInformationBank = Bavsv1accountvalidationsPaymentInformationBank(
        routing_number = paymentInformationBankRoutingNumber,
        account = paymentInformationBankAccount.__dict__
    )

    paymentInformation = Bavsv1accountvalidationsPaymentInformation(
        bank = paymentInformationBank.__dict__
    )

    requestObj = AccountValidationsRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        #The BAV API mandates Request MLE, and JWT is the only supported authentication type for this feature. By default SDK sends encrypted requests for the APIs having mandatory Request MLE.
        config_obj = configuration.ConfigurationForBankAccountValidation()
        client_config = config_obj.get_configuration_for_bav()
        api_instance = BankAccountValidationApi(client_config)
        return_data, status, body = api_instance.bank_account_validation_request(requestObj)
        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    bank_account_validation(False)
