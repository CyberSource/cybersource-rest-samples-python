from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def setup_completion_with_card_number():
    clientReferenceInformationCode = "cybs_test"
    clientReferenceInformationPartnerDeveloperId = "7891234"
    clientReferenceInformationPartnerSolutionId = "89012345"
    clientReferenceInformationPartner = Riskv1decisionsClientReferenceInformationPartner(
        developer_id = clientReferenceInformationPartnerDeveloperId,
        solution_id = clientReferenceInformationPartnerSolutionId
    )

    clientReferenceInformation = Riskv1authenticationsetupsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__
    )

    paymentInformationCardType = "001"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2025"
    paymentInformationCardNumber = "4000000000000101"
    paymentInformationCard = Riskv1authenticationsetupsPaymentInformationCard(
        type = paymentInformationCardType,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        number = paymentInformationCardNumber
    )

    paymentInformation = Riskv1authenticationsetupsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    requestObj = PayerAuthSetupRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayerAuthenticationApi(client_config)
        return_data, status, body = api_instance.payer_auth_setup(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PayerAuthenticationApi->payer_auth_setup: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    setup_completion_with_card_number()
