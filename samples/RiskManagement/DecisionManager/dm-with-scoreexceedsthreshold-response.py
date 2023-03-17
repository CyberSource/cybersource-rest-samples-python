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

def dm_with_scoreexceedsthreshold_response():
    clientReferenceInformationCode = "54323007"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationCardNumber = "4444444444444448"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2020"
    paymentInformationCard = Riskv1decisionsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformation = Riskv1decisionsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsTotalAmount = "144.14"
    orderInformationAmountDetails = Riskv1decisionsOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        total_amount = orderInformationAmountDetailsTotalAmount
    )

    orderInformationShipToAddress1 = "96, powers street"
    orderInformationShipToAddress2 = ""
    orderInformationShipToAdministrativeArea = "KA"
    orderInformationShipToCountry = "IN"
    orderInformationShipToLocality = "Clearwater milford"
    orderInformationShipToFirstName = "James"
    orderInformationShipToLastName = "Smith"
    orderInformationShipToPhoneNumber = "7606160717"
    orderInformationShipToPostalCode = "560056"
    orderInformationShipTo = Riskv1decisionsOrderInformationShipTo(
        address1 = orderInformationShipToAddress1,
        address2 = orderInformationShipToAddress2,
        administrative_area = orderInformationShipToAdministrativeArea,
        country = orderInformationShipToCountry,
        locality = orderInformationShipToLocality,
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName,
        phone_number = orderInformationShipToPhoneNumber,
        postal_code = orderInformationShipToPostalCode
    )

    orderInformationBillToAddress1 = "96, powers street"
    orderInformationBillToAdministrativeArea = "NH"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "Clearwater milford"
    orderInformationBillToFirstName = "James"
    orderInformationBillToLastName = "Smith"
    orderInformationBillToPhoneNumber = "7606160717"
    orderInformationBillToEmail = "test@visa.com"
    orderInformationBillToPostalCode = "03055"
    orderInformationBillTo = Riskv1decisionsOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        phone_number = orderInformationBillToPhoneNumber,
        email = orderInformationBillToEmail,
        postal_code = orderInformationBillToPostalCode
    )

    orderInformation = Riskv1decisionsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        ship_to = orderInformationShipTo.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    requestObj = CreateBundledDecisionManagerCaseRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = DecisionManagerApi(client_config)
        return_data, status, body = api_instance.create_bundled_decision_manager_case(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling DecisionManagerApi->create_bundled_decision_manager_case: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    dm_with_scoreexceedsthreshold_response()
