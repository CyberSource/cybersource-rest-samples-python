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

def authentication_with_new_account():
    clientReferenceInformationCode = "New Account"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsTotalAmount = "10.99"
    orderInformationAmountDetails = Riskv1authenticationsOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        total_amount = orderInformationAmountDetailsTotalAmount
    )

    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToAddress2 = "Address 2"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToPhoneNumber = "4158880000"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillTo = Riskv1authenticationsOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        phone_number = orderInformationBillToPhoneNumber,
        email = orderInformationBillToEmail,
        postal_code = orderInformationBillToPostalCode
    )

    orderInformation = Riskv1authenticationsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    paymentInformationCardType = "001"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2025"
    paymentInformationCardNumber = "4000990000000004"
    paymentInformationCard = Riskv1authenticationsPaymentInformationCard(
        type = paymentInformationCardType,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        number = paymentInformationCardNumber
    )

    paymentInformation = Riskv1authenticationsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    consumerAuthenticationInformationTransactionMode = "MOTO"
    consumerAuthenticationInformation = Riskv1decisionsConsumerAuthenticationInformation(
        transaction_mode = consumerAuthenticationInformationTransactionMode
    )

    riskInformationBuyerHistoryCustomerAccountCreationHistory = "NEW_ACCOUNT"
    riskInformationBuyerHistoryCustomerAccount = Ptsv2paymentsRiskInformationBuyerHistoryCustomerAccount(
        creation_history = riskInformationBuyerHistoryCustomerAccountCreationHistory
    )

    riskInformationBuyerHistoryAccountHistoryFirstUseOfShippingAddress = False
    riskInformationBuyerHistoryAccountHistory = Ptsv2paymentsRiskInformationBuyerHistoryAccountHistory(
        first_use_of_shipping_address = riskInformationBuyerHistoryAccountHistoryFirstUseOfShippingAddress
    )

    riskInformationBuyerHistory = Ptsv2paymentsRiskInformationBuyerHistory(
        customer_account = riskInformationBuyerHistoryCustomerAccount.__dict__,
        account_history = riskInformationBuyerHistoryAccountHistory.__dict__
    )

    riskInformation = Riskv1authenticationsRiskInformation(
        buyer_history = riskInformationBuyerHistory.__dict__
    )

    requestObj = CheckPayerAuthEnrollmentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        consumer_authentication_information = consumerAuthenticationInformation.__dict__,
        risk_information = riskInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayerAuthenticationApi(client_config)
        return_data, status, body = api_instance.check_payer_auth_enrollment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PayerAuthenticationApi->check_payer_auth_enrollment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    authentication_with_new_account()
