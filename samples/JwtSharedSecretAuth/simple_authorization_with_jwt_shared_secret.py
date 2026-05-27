"""
Simple Authorization using JWT authentication with Shared Secret (HS256).

This sample demonstrates a drop-in replacement for HTTP Signature authentication.
It uses the **same** merchantKeyId and merchantsecretKey credentials you already
use for HTTP Signature, but authenticates via JWT instead.

Migration from HTTP Signature
------------------------------
HTTP Signature authentication is being deprecated. To migrate:

1. Change authentication_type from 'http_signature' to 'jwt'
2. Add jwt_key_type = 'SHARED_SECRET'
3. Keep your existing merchantKeyId and merchantsecretKey as-is

See data.JwtSharedSecretConfiguration.get_merchant_details() for the
full configuration.
"""

from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

# Load configuration module dynamically
config_file = os.path.join(os.getcwd(), "data", "JwtSharedSecretConfiguration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def del_none(d):
    """Remove None values from dictionary."""
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


def simple_authorization_with_jwt_shared_secret():
    """
    Execute a simple payment authorization using JWT with Shared Secret.
    
    Returns:
        PtsV2PaymentsPost201Response: API response object
    """
    
    # Build request object
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code=clientReferenceInformationCode
    )

    processingInformationCapture = False
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture=processingInformationCapture
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2031"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number=paymentInformationCardNumber,
        expiration_month=paymentInformationCardExpirationMonth,
        expiration_year=paymentInformationCardExpirationYear
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card=paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "102.21"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount=orderInformationAmountDetailsTotalAmount,
        currency=orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "4158880000"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name=orderInformationBillToFirstName,
        last_name=orderInformationBillToLastName,
        address1=orderInformationBillToAddress1,
        locality=orderInformationBillToLocality,
        administrative_area=orderInformationBillToAdministrativeArea,
        postal_code=orderInformationBillToPostalCode,
        country=orderInformationBillToCountry,
        email=orderInformationBillToEmail,
        phone_number=orderInformationBillToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details=orderInformationAmountDetails.__dict__,
        bill_to=orderInformationBillTo.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information=clientReferenceInformation.__dict__,
        processing_information=processingInformation.__dict__,
        payment_information=paymentInformation.__dict__,
        order_information=orderInformation.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        # Load JWT + Shared Secret configuration
        config_obj = configuration.JwtSharedSecretConfiguration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data

    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)


def write_log_audit(status):
    """Log test execution status."""
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    simple_authorization_with_jwt_shared_secret()
