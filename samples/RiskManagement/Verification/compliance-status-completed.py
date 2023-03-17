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

def compliance_status_completed():
    clientReferenceInformationCode = "verification example"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationBillToAddress1 = "901 Metro Centre Blvd"
    orderInformationBillToAddress2 = "2"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "Foster City"
    orderInformationBillToPostalCode = "94404"
    orderInformationBillToFirstName = "Suman"
    orderInformationBillToLastName = "Kumar"
    orderInformationBillToEmail = "donewithhorizon@test.com"
    orderInformationBillTo = Riskv1exportcomplianceinquiriesOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        postal_code = orderInformationBillToPostalCode,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        email = orderInformationBillToEmail
    )

    orderInformationShipToCountry = "be"
    orderInformationShipToFirstName = "DumbelDore"
    orderInformationShipToLastName = "Albus"
    orderInformationShipTo = Riskv1exportcomplianceinquiriesOrderInformationShipTo(
        country = orderInformationShipToCountry,
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Riskv1exportcomplianceinquiriesOrderInformationLineItems(
        unit_price = "19.00"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Riskv1exportcomplianceinquiriesOrderInformation(
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__,
        line_items = orderInformationLineItems
    )

    buyerInformationMerchantCustomerId = "87789"
    buyerInformation = Riskv1addressverificationsBuyerInformation(
        merchant_customer_id = buyerInformationMerchantCustomerId
    )

    exportComplianceInformationAddressOperator = "and"
    exportComplianceInformationWeightsAddress = "abc"
    exportComplianceInformationWeightsCompany = "def"
    exportComplianceInformationWeightsName = "adb"
    exportComplianceInformationWeights = Riskv1exportcomplianceinquiriesExportComplianceInformationWeights(
        address = exportComplianceInformationWeightsAddress,
        company = exportComplianceInformationWeightsCompany,
        name = exportComplianceInformationWeightsName
    )


    exportComplianceInformationSanctionLists = []
    exportComplianceInformationSanctionLists.append("abc")
    exportComplianceInformationSanctionLists.append("acc")
    exportComplianceInformationSanctionLists.append("bac")
    exportComplianceInformation = Riskv1exportcomplianceinquiriesExportComplianceInformation(
        address_operator = exportComplianceInformationAddressOperator,
        weights = exportComplianceInformationWeights.__dict__,
        sanction_lists = exportComplianceInformationSanctionLists
    )

    requestObj = ValidateExportComplianceRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        buyer_information = buyerInformation.__dict__,
        export_compliance_information = exportComplianceInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = VerificationApi(client_config)
        return_data, status, body = api_instance.validate_export_compliance(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling VerificationApi->validate_export_compliance: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    compliance_status_completed()
