from CyberSource import *
from pathlib import Path
import os
import json
import uuid
from importlib.machinery import SourceFileLoader


config_file = os.path.join(os.getcwd(), "data", "MerchantBoardingConfiguration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def merchant_boarding_tsys():

        
    req_obj = PostRegistrationBody()

    business_address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
        country="US",
        address1="123456 SandMarket",
        locality="ORMOND BEACH",
        administrative_area="FL",
        postal_code="32176"
    ).__dict__

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
        first_name="Stuart",
        last_name="Stuart",
        phone_number="6574567813",
        email="svc_email_bt@corpdev.visa.com"
    ).__dict__

    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=business_address,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=business_contact,
        merchant_category_code="5999"
    ).__dict__

    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True,
        business_information=business_information
    ).__dict__

    req_obj.organization_information = organization_info

    card_not_present = PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
    card_present = PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
    features = {
        "cardNotPresent": card_not_present,
        "cardPresent": card_present
    }

    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features=features
    ).__dict__

    merchant_descriptor_information = CardProcessingConfigCommonMerchantDescriptorInformation(
        city="cupertino",
        country="USA",
        name="kumar",
        state="CA",
        phone="888555333",
        zip="94043",
        street="steet1"
    ).__dict__

    currencies = {
        "CAD": CardProcessingConfigCommonCurrencies1(
            enabled=True,
            enabled_card_present=True,
            enabled_card_not_present=True,
            terminal_id="1234",
            service_enablement_number=""
        ).__dict__
    }

    payment_types = {
        "MASTERCARD": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "VISA": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__
    }

    tsys_processor = CardProcessingConfigCommonProcessors(
        acquirer=CardProcessingConfigCommonAcquirer().__dict__,
        currencies=currencies,
        payment_types=payment_types,
        bank_number="234576",
        chain_number="223344",
        batch_group="vital_1130",
        enhanced_data="disabled",
        industry_code="D",
        merchant_bin_number="765576",
        merchant_id="834215123456",
        merchant_location_number="00001",
        store_id="2563",
        vital_number="71234567",
        quasi_cash=False,
        send_amex_level2_data=None,
        soft_descriptor_type="1 - trans_ref_no",
        travel_agency_code="2356",
        travel_agency_name="Agent"
    ).__dict__

    processors = {"tsys": tsys_processor}

    common = CardProcessingConfigCommon(
        merchant_category_code="5999",
        process_level3_data="ignored",
        default_auth_type_code="FINAL",
        enable_partial_auth=False,
        amex_vendor_code="2233",
        merchant_descriptor_information=merchant_descriptor_information,
        processors=processors
    ).__dict__

    card_not_present_feature = CardProcessingConfigFeaturesCardNotPresent(
        visa_straight_through_processing_only=False,
        amex_transaction_advice_addendum1=None
    ).__dict__

    features2 = CardProcessingConfigFeatures(
        card_not_present=card_not_present_feature
    ).__dict__

    configurations = CardProcessingConfig(
        common=common,
        features=features2
    ).__dict__

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation(
        configurations=configurations,
        template_id=str(uuid.UUID("818048AD-2860-4D2D-BC39-2447654628A1"))
    ).__dict__

    card_processing = PaymentsProductsCardProcessing(
        subscription_information=subscription_information,
        configuration_information=configuration_information
    ).__dict__

    virtual_terminal_configuration = PaymentsProductsVirtualTerminalConfigurationInformation(
        template_id=str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))
    ).__dict__

    virtual_terminal = PaymentsProductsVirtualTerminal(
        configuration_information=virtual_terminal_configuration
    ).__dict__

    customer_invoicing = PaymentsProductsTax(
    ).__dict__

    payments = PaymentsProducts(
        card_processing=card_processing,
        virtual_terminal=virtual_terminal,
        customer_invoicing=customer_invoicing
    ).__dict__

    risk = RiskProducts().__dict__


    token_management_configuration = CommerceSolutionsProductsTokenManagementConfigurationInformation(
        template_id=str(uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA"))
    ).__dict__

    token_management = CommerceSolutionsProductsTokenManagement(
        configuration_information=token_management_configuration
    ).__dict__

    commerce_solutions = CommerceSolutionsProducts(
        token_management=token_management
    ).__dict__

    transaction_search = PaymentsProductsTax(
    ).__dict__

    reporting = PaymentsProductsTax(
    ).__dict__

    value_added_services = ValueAddedServicesProducts(
        transaction_search=transaction_search,
        reporting=reporting
    ).__dict__

    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
        payments=payments,
        risk=risk,
        commerce_solutions=commerce_solutions,
        value_added_services=value_added_services
    ).__dict__

    product_information = Boardingv1registrationsProductInformation(
        selected_products=selected_products
    ).__dict__

    req_obj.product_information = product_information
    
    

    req_obj = del_none(req_obj.__dict__)
    req_obj = json.dumps(req_obj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_merchant_boarding_configuration()
        api_instance = MerchantBoardingApi(client_config)
        return_data, status, body = api_instance.post_registration(req_obj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling MerchantBoardingApi->post_registration: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    merchant_boarding_tsys()
