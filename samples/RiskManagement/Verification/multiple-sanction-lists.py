from CyberSource import *
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

def multiple_sanction_lists():
    clientReferenceInformationCode = "verification example"
    clientReferenceInformationComments = "All fields"
    clientReferenceInformation = Riskv1addressverificationsClientReferenceInformation(
        code = clientReferenceInformationCode,
        comments = clientReferenceInformationComments
    )

    orderInformationBillToAddress1 = "901 Metro Centre Blvd"
    orderInformationBillToAddress2 = " "
    orderInformationBillToAddress3 = ""
    orderInformationBillToAddress4 = "Foster City"
    orderInformationBillToAdministrativeArea = "NH"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "CA"
    orderInformationBillToPostalCode = "03055"
    orderInformationBillToCompanyName = "A & C International Trade, Inc."
    orderInformationBillToCompany = Riskv1exportcomplianceinquiriesOrderInformationBillToCompany(
        name = orderInformationBillToCompanyName
    )

    orderInformationBillToFirstName = "Suman"
    orderInformationBillToLastName = "Kumar"
    orderInformationBillToEmail = "test@domain.com"
    orderInformationBillTo = Riskv1exportcomplianceinquiriesOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        address3 = orderInformationBillToAddress3,
        address4 = orderInformationBillToAddress4,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        postal_code = orderInformationBillToPostalCode,
        company = orderInformationBillToCompany.__dict__,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        email = orderInformationBillToEmail
    )

    orderInformationShipToCountry = "IN"
    orderInformationShipToFirstName = "DumbelDore"
    orderInformationShipToLastName = "Albus"
    orderInformationShipTo = Riskv1exportcomplianceinquiriesOrderInformationShipTo(
        country = orderInformationShipToCountry,
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Riskv1exportcomplianceinquiriesOrderInformationLineItems(
        unit_price = "120.50",
        quantity = 3,
        product_sku = "610009",
        product_name = "Xer",
        product_code = "physical_software"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Riskv1exportcomplianceinquiriesOrderInformation(
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__,
        line_items = orderInformationLineItems
    )

    buyerInformationMerchantCustomerId = "Export1"
    buyerInformation = Riskv1addressverificationsBuyerInformation(
        merchant_customer_id = buyerInformationMerchantCustomerId
    )

    deviceInformationIpAddress = "127.0.0.1"
    deviceInformationHostName = "www.cybersource.ir"
    deviceInformation = Riskv1exportcomplianceinquiriesDeviceInformation(
        ip_address = deviceInformationIpAddress,
        host_name = deviceInformationHostName
    )

    exportComplianceInformationAddressOperator = "and"
    exportComplianceInformationWeightsAddress = "low"
    exportComplianceInformationWeightsCompany = "exact"
    exportComplianceInformationWeightsName = "exact"
    exportComplianceInformationWeights = Riskv1exportcomplianceinquiriesExportComplianceInformationWeights(
        address = exportComplianceInformationWeightsAddress,
        company = exportComplianceInformationWeightsCompany,
        name = exportComplianceInformationWeightsName
    )


    exportComplianceInformationSanctionLists = []
    exportComplianceInformationSanctionLists.append("Bureau Of Industry and Security")
    exportComplianceInformationSanctionLists.append("DOS_DTC")
    exportComplianceInformationSanctionLists.append("AUSTRALIA")
    exportComplianceInformation = Riskv1exportcomplianceinquiriesExportComplianceInformation(
        address_operator = exportComplianceInformationAddressOperator,
        weights = exportComplianceInformationWeights.__dict__,
        sanction_lists = exportComplianceInformationSanctionLists
    )

    requestObj = ValidateExportComplianceRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        buyer_information = buyerInformation.__dict__,
        device_information = deviceInformation.__dict__,
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

        return return_data
    except Exception as e:
        print("\nException when calling VerificationApi->validate_export_compliance: %s\n" % e)

if __name__ == "__main__":
    multiple_sanction_lists()
