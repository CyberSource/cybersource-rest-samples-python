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

def merchant_boarding_eftpos():


    # Create main request object
    req_obj = PostRegistrationBody()

    # Organization Information
    organization_information = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    # Business Information
    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
            country="US",
            address1="123456 SandMarket",
            locality="ORMOND BEACH",
            administrative_area="FL",
            postal_code="32176"
        ).__dict__,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
            first_name="Stuart",
            last_name="Stuart",
            phone_number="6574567813",
            email="svc_email_bt@corpdev.visa.com"
        ).__dict__,
        merchant_category_code="5999"
    )

    organization_information.business_information = business_information.__dict__

    req_obj.organization_information = organization_information.__dict__

    # Subscription Information Features
    features = {
        "cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__,
        "cardPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=False).__dict__
    }

    # Subscription Information
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features=features
    )

    # Acquirer Information
    acquirer = CardProcessingConfigCommonAcquirer(
        country_code="344_hongkong",
        institution_id="22344"
    )

    # Currencies Information
    currencies = {
        "AUD": CardProcessingConfigCommonCurrencies1(
            enabled=True,
            merchant_id="12345612344",
            terminal_id="12121212"
        ).__dict__
    }

    # Payment Types Information
    payment_types = {
        "EFTPOS": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__
    }

    # Processors Information
    processors = {
        "EFTPOS": CardProcessingConfigCommonProcessors(
            acquirer=acquirer.__dict__,
            currencies=currencies,
            payment_types=payment_types,
            enable_cvv_response_indicator=True,
            enable_least_cost_routing=True,
            merchant_tier="000"
        ).__dict__
    }

    # Common Configuration
    common = CardProcessingConfigCommon(
        merchant_category_code="5999",
        prefer_cobadged_secondary_brand=True,
        processors=processors
    )

    # Configuration Information
    configuration_information = PaymentsProductsCardProcessingConfigurationInformation(
        configurations=CardProcessingConfig(
            common=common.__dict__,
            features=CardProcessingConfigFeatures().__dict__
        ).__dict__,
        template_id=str(uuid.UUID("1F9B7F6E-F0DB-44C8-BF8E-5013E34C0F87"))
    )

    # Card Processing
    card_processing = PaymentsProductsCardProcessing(
        subscription_information=subscription_information.__dict__,
        configuration_information=configuration_information.__dict__
    )

    # Payments
    payments = PaymentsProducts(
        card_processing=card_processing.__dict__
    )

    # Selected Products
    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
        payments=payments.__dict__
    )

    # Product Information
    product_information = Boardingv1registrationsProductInformation(
        selected_products=selected_products.__dict__
    )

    req_obj.product_information = product_information.__dict__
        

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
    merchant_boarding_eftpos()
