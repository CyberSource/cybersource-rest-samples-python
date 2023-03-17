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

def add_duplicate_information(type):
    orderInformationAddressAddress1 = "1234 Sample St."
    orderInformationAddressAddress2 = "Mountain View"
    orderInformationAddressLocality = "California"
    orderInformationAddressCountry = "US"
    orderInformationAddressAdministrativeArea = "CA"
    orderInformationAddressPostalCode = "94043"
    orderInformationAddress = Riskv1liststypeentriesOrderInformationAddress(
        address1 = orderInformationAddressAddress1,
        address2 = orderInformationAddressAddress2,
        locality = orderInformationAddressLocality,
        country = orderInformationAddressCountry,
        administrative_area = orderInformationAddressAdministrativeArea,
        postal_code = orderInformationAddressPostalCode
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToEmail = "nobody@example.com"
    orderInformationBillTo = Riskv1liststypeentriesOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        email = orderInformationBillToEmail
    )

    orderInformation = Riskv1liststypeentriesOrderInformation(
        address = orderInformationAddress.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    paymentInformation = Riskv1liststypeentriesPaymentInformation(
    )

    clientReferenceInformationCode = "54323007"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    riskInformationMarkingDetailsAction = "add"
    riskInformationMarkingDetails = Riskv1liststypeentriesRiskInformationMarkingDetails(
        action = riskInformationMarkingDetailsAction
    )

    riskInformation = Riskv1liststypeentriesRiskInformation(
        marking_details = riskInformationMarkingDetails.__dict__
    )

    requestObj = AddNegativeListRequest(
        order_information = orderInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        client_reference_information = clientReferenceInformation.__dict__,
        risk_information = riskInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = DecisionManagerApi(client_config)
        return_data, status, body = api_instance.add_negative(type, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling DecisionManagerApi->add_negative: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    type = "positive"

    add_duplicate_information(type)
