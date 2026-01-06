from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "MLEConfiguration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def enroll_card_with_mle(flag=False):
    """
    Enroll a card using the Agentic Card Enrollment API with MLE support.
    This function demonstrates how to use the EnrollmentApi to enroll a card
    with comprehensive device information, buyer information, assurance data, and consent data.
    """
    
    try:
        # Client Reference Information
        client_correlation_id = '3e1b7943-6567-4965-a32b-5aa93d057d35'
        
        # Device Information
        device_information = Acpv1tokensDeviceInformation()
        device_information.user_agent = 'SampleUserAgent'
        device_information.application_name = 'My Magic App'
        device_information.fingerprint_session_id = 'finSessionId'
        device_information.country = 'US'
        
        # Device Data
        device_information_device_data = Acpv1tokensDeviceInformationDeviceData()
        device_information_device_data.type = 'Mobile'
        device_information_device_data.manufacturer = 'Apple'
        device_information_device_data.brand = 'Apple'
        device_information_device_data.model = 'iPhone 16 Pro Max'
        device_information.device_data = device_information_device_data.__dict__
        
        device_information.ip_address = '192.168.0.100'
        device_information.client_device_id = '000b2767814e4416999f4ee2b099491d2087'
        
        # Buyer Information
        buyer_information = Acpv1tokensBuyerInformation()
        buyer_information.language = 'en'
        buyer_information.merchant_customer_id = '3e1b7943-6567-4965-a32b-5aa93d057d35'
        
        # Personal Identification
        personal_identification = []
        personal_identification_1 = Acpv1tokensBuyerInformationPersonalIdentification()
        personal_identification_1.type = 'The identification type'
        personal_identification_1.id = '1'
        personal_identification.append(personal_identification_1.__dict__)
        
        buyer_information.personal_identification = personal_identification
        
        # Bill To Information
        bill_to = Acpv1tokensBillTo()
        bill_to.first_name = 'John'
        bill_to.last_name = 'Doe'
        bill_to.full_name = 'John Michael Doe'
        bill_to.email = 'john.doe@example.com'
        bill_to.country_calling_code = '1'
        bill_to.phone_number = '5551234567'
        bill_to.number_is_voice_only = False
        bill_to.country = 'US'
        
        # Consumer Identity
        consumer_identity = Acpv1tokensConsumerIdentity()
        consumer_identity.identity_type = 'EMAIL_ADDRESS'
        consumer_identity.identity_value = 'john.doe@example.com'
        consumer_identity.identity_provider = 'PARTNER'
        consumer_identity.identity_provider_url = 'https://identity.partner.com'
        
        # Payment Information
        payment_information = Acpv1tokensPaymentInformation()
        
        # Customer
        payment_information_customer = Acpv1tokensPaymentInformationCustomer()
        payment_information_customer.id = ''
        payment_information.customer = payment_information_customer.__dict__
        
        # Payment Instrument
        payment_information_payment_instrument = Acpv1tokensPaymentInformationPaymentInstrument()
        payment_information_payment_instrument.id = ''
        payment_information.payment_instrument = payment_information_payment_instrument.__dict__
        
        # Instrument Identifier
        payment_information_instrument_identifier = Acpv1tokensPaymentInformationInstrumentIdentifier()
        payment_information_instrument_identifier.id = '4044EB915C613A82E063AF598E0AE6EF'
        payment_information.instrument_identifier = payment_information_instrument_identifier.__dict__
        
        # Enrollment Reference Data
        enrollment_reference_data = Acpv1tokensEnrollmentReferenceData()
        enrollment_reference_data.enrollment_reference_type = 'TOKEN_REFERENCE_ID'
        enrollment_reference_data.enrollment_reference_provider = 'VTS'
        
        # Assurance Data
        assurance_data = []
        assurance_data_1 = Acpv1tokensAssuranceData()
        assurance_data_1.verification_type = 'DEVICE'
        assurance_data_1.verification_entity = '10'
        
        verification_events = []
        verification_events.append("01")
        assurance_data_1.verification_events = verification_events
        
        assurance_data_1.verification_method = '02'
        assurance_data_1.verification_results = '01'
        assurance_data_1.verification_timestamp = '1735690745'
        
        # Authentication Context
        authentication_context_1 = Acpv1tokensAuthenticationContext()
        authentication_context_1.action = 'AUTHENTICATE'
        assurance_data_1.authentication_context = authentication_context_1.__dict__
        
        # Authenticated Identities
        authenticated_identities_1 = Acpv1tokensAuthenticatedIdentities()
        authenticated_identities_1.data = 'authenticatedData'
        authenticated_identities_1.provider = 'VISA_PAYMENT_PASSKEY'
        authenticated_identities_1.id = 'f48ac10b-58cc-4372-a567-0e02b2c3d489'
        assurance_data_1.authenticated_identities = authenticated_identities_1.__dict__
        
        assurance_data_1.additional_data = ''
        assurance_data.append(assurance_data_1.__dict__)
        
        # Consent Data
        consent_data = []
        consent_data_1 = Acpv1tokensConsentData()
        consent_data_1.id = '550e8400-e29b-41d4-a716-446655440000'
        consent_data_1.type = 'PERSONALIZATION'
        consent_data_1.source = 'CLIENT'
        consent_data_1.accepted_time = '1719169800'
        consent_data_1.effective_until = '1750705800'
        consent_data.append(consent_data_1.__dict__)
        
        # Create the main request object
        request_obj = AgenticCardEnrollmentRequest()
        request_obj.client_correlation_id = client_correlation_id
        request_obj.device_information = device_information.__dict__
        request_obj.buyer_information = buyer_information.__dict__
        request_obj.bill_to = bill_to.__dict__
        request_obj.consumer_identity = consumer_identity.__dict__
        request_obj.payment_information = payment_information.__dict__
        request_obj.enrollment_reference_data = enrollment_reference_data.__dict__
        request_obj.assurance_data = assurance_data
        request_obj.consent_data = consent_data
        
        # Remove None values and convert to JSON
        request_obj = del_none(request_obj.__dict__)
        request_obj = json.dumps(request_obj)
        
        # Configure MLE
        config_obj = configuration.MLEConfiguration()
        
        # Use MLE configuration type 1 (globally enabled MLE for all supported APIs)
        # You can change this to get_configuration_with_mle_Type2() or get_configuration_with_mle_Type3()
        # depending on your MLE requirements
        client_config = config_obj.get_configuration_with_request_and_response_mle_Type2()
        
        # Create API instance and make the call
        api_instance = EnrollmentApi(client_config)
        return_data, status, body = api_instance.enroll_card(request_obj)
        
        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        
        write_log_audit(status)
        return return_data
        
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling EnrollmentApi->enroll_card: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    enroll_card_with_mle(False)
