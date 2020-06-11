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

def create_payment_instrument_bank_account():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"

    bankAccountType = "savings"
    bankAccount = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount(
        type = bankAccountType
    )

    buyerInformationCompanyTaxID = "12345"
    buyerInformationCurrency = "USD"
    buyerInformationDateOfBirth = "2000-12-13"

    buyerInformationPersonalIdentification = []
    buyerInformationPersonalIdentificationIssuedBy1 = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformationIssuedBy(
        administrative_area = "CA"
    )

    buyerInformationPersonalIdentification1 = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformationPersonalIdentification(
        id = "57684432111321",
        type = "driver license",
        issued_by = buyerInformationPersonalIdentificationIssuedBy1.__dict__
    )

    buyerInformationPersonalIdentification.append(buyerInformationPersonalIdentification1.__dict__)

    buyerInformation = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation(
        company_tax_id = buyerInformationCompanyTaxID,
        currency = buyerInformationCurrency,
        date_of_birth = buyerInformationDateOfBirth,
        personal_identification = buyerInformationPersonalIdentification
    )

    billToFirstName = "John"
    billToLastName = "Smith"
    billToCompany = "Cybersource"
    billToAddress1 = "8310 Capital of Texas Highwas North"
    billToAddress2 = "Bluffstone Drive"
    billToLocality = "Austin"
    billToAdministrativeArea = "TX"
    billToPostalCode = "78731"
    billToCountry = "US"
    billToEmail = "john.smith@test.com"
    billToPhoneNumber = "+44 2890447951"
    billTo = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo(
        first_name = billToFirstName,
        last_name = billToLastName,
        company = billToCompany,
        address1 = billToAddress1,
        address2 = billToAddress2,
        locality = billToLocality,
        administrative_area = billToAdministrativeArea,
        postal_code = billToPostalCode,
        country = billToCountry,
        email = billToEmail,
        phone_number = billToPhoneNumber
    )

    processingInformationBillPaymentProgramEnabled = True
    processingInformationBankTransferOptionsSeCCode = "WEB"
    processingInformationBankTransferOptions = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions(
        sec_code = processingInformationBankTransferOptionsSeCCode
    )

    processingInformation = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation(
        bill_payment_program_enabled = processingInformationBillPaymentProgramEnabled,
        bank_transfer_options = processingInformationBankTransferOptions.__dict__
    )

    merchantInformationMerchantDescriptorAlternateName = "Branch Name"
    merchantInformationMerchantDescriptor = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformationMerchantDescriptor(
        alternate_name = merchantInformationMerchantDescriptorAlternateName
    )

    merchantInformation = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation(
        merchant_descriptor = merchantInformationMerchantDescriptor.__dict__
    )

    instrumentIdentifierBankAccountNumber = "4100"
    instrumentIdentifierBankAccountRoutingNumber = "071923284"
    instrumentIdentifierBankAccount = Tmsv1instrumentidentifiersBankAccount(
        number = instrumentIdentifierBankAccountNumber,
        routing_number = instrumentIdentifierBankAccountRoutingNumber
    )

    instrumentIdentifier = Tmsv1paymentinstrumentsInstrumentIdentifier(
        bank_account = instrumentIdentifierBankAccount.__dict__
    )

    requestObj = CreatePaymentInstrumentRequest(
        bank_account = bankAccount.__dict__,
        buyer_information = buyerInformation.__dict__,
        bill_to = billTo.__dict__,
        processing_information = processingInformation.__dict__,
        merchant_information = merchantInformation.__dict__,
        instrument_identifier = instrumentIdentifier.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.create_payment_instrument(profileid, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentInstrumentApi->create_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    create_payment_instrument_bank_account()
