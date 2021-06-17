from CyberSource import *
import json
import os

# Assigning the configuration properties in the configuration dictionary
def get_configuration():
    authentication_type ="mutual_auth"
    run_environment = "api-matest.cybersource.com"    
    enable_client_cert = True
    client_cert_dir = os.path.join(os.getcwd(), "resources")
    ssl_client_cert = ''
    private_key = ''
    # ssl_key_password = ''     #Optional Field
    client_id = ''
    client_secret = ''

    configuration_dictionary = {}
    configuration_dictionary["authentication_type"] = authentication_type
    configuration_dictionary["enable_client_cert"] = enable_client_cert
    configuration_dictionary["run_environment"] = run_environment
    configuration_dictionary["client_cert_dir"] = client_cert_dir
    configuration_dictionary["ssl_client_cert"] = ssl_client_cert
    configuration_dictionary["private_key"] = private_key
    # configuration_dictionary["ssl_key_password"] = ssl_key_password     #Optional Field
    configuration_dictionary["client_id"] = client_id
    configuration_dictionary["client_secret"] = client_secret
    return configuration_dictionary

def standalone_oauth():
    result = None
    create_using_auth_code = False
    if create_using_auth_code:
        code = ''
        grant_type = "authorization_code"
        result = post_access_token_from_auth_code(code, grant_type)
    else:
        grant_type = "refresh_token"
        refresh_token = ""
        result = post_access_token_from_refresh_token(refresh_token, grant_type)

    if result is not None: 
        refresh_token = result.refresh_token
        access_token = result.access_token

        #Call Payments SampleCode using OAuth, Set Authentication to OAuth in Sample Code Configuration
        simple_authorizationinternet(access_token, refresh_token)    

def post_access_token_from_auth_code(code, grant_type):
    config = get_configuration()    
    requestObj = CreateAccessTokenRequest(
        client_id = config['client_id'],
        client_secret = config['client_secret'],
        grant_type = grant_type,
        code = code,
    )

    requestObj = requestObj.__dict__
    requestObj = json.dumps(requestObj)

    try:
        api_instance = OAuthApi(config)
        return_data, status, body = api_instance.create_access_token(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def post_access_token_from_refresh_token(refresh_token, grant_type):
    config = get_configuration()        
    requestObj = CreateAccessTokenRequest(
        client_id = config['client_id'],
        client_secret = config['client_secret'],
        grant_type = grant_type,
        refresh_token = refresh_token
    )

    requestObj = requestObj.__dict__
    requestObj = json.dumps(requestObj)

    try:
        api_instance = OAuthApi(config)
        return_data, status, body = api_instance.create_access_token(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)




def simple_authorizationinternet(access_token, refresh_token):
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCapture = False
    
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2031"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "102.21"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
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
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )

    requestObj = requestObj.__dict__
    requestObj = json.dumps(requestObj)


    try:
        client_config = get_configuration()
        client_config["access_token"] = access_token
        client_config["refresh_token"] = refresh_token
        client_config["authentication_type"] = 'oauth'
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    standalone_oauth()
