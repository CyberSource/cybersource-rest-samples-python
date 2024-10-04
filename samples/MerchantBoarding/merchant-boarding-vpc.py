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

def merchant_boarding_vpc():


    

    req_obj = PostRegistrationBody()

    # Organization Information
    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    business_address = {
        "country": "US",
        "address1": "123456 SandMarket",
        "locality": "ORMOND BEACH",
        "administrative_area": "FL",
        "postal_code": "32176"
    }

    business_contact = {
        "first_name": "Stuart",
        "last_name": "Stuart",
        "phone_number": "6574567813",
        "email": "svc_email_bt@corpdev.visa.com"
    }

    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=business_address,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=business_contact,
        merchant_category_code="5999"
    )

    organization_info.business_information = business_info.__dict__
    req_obj.organization_information = organization_info.__dict__

    # Product Information
    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    # Payments
    subscription_features = {
        "cardNotPresent": {"enabled": True},
        "cardPresent": {"enabled": True}
    }

    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features=subscription_features
    )

    common_processors = {
        "VPC": CardProcessingConfigCommonProcessors(
            acquirer={
                "country_code": "840_usa",
                "file_destination_bin": "444500",
                "interbank_card_association_id": "3684",
                "institution_id": "444571"
            },
            acquirer_merchant_id="123456",
            allow_multiple_bills=False,
            batch_group="vdcvantiv_est_00",
            business_application_id="AA",
            enable_auto_auth_reversal_after_void=True,
            merchant_verification_value="123456",
            quasi_cash=False,
            enable_transaction_reference_number=True
        ).__dict__
    }

    common_config = CardProcessingConfigCommon(
        merchant_category_code="1799",
        default_auth_type_code="FINAL",
        visa_delegated_authentication_id="123457",
        domestic_merchant_id="123458",
        credit_card_refund_limit_percent="2",
        business_center_credit_card_refund_limit_percent="3",
        processors=common_processors
    )

    features_card_not_present_processors = {
        "VPC": CardProcessingConfigFeaturesCardNotPresentProcessors(
            relax_address_verification_system=True,
            relax_address_verification_system_allow_expired_card=True,
            relax_address_verification_system_allow_zip_without_country=True
        ).__dict__
    }

    features_card_not_present = CardProcessingConfigFeaturesCardNotPresent(
        processors=features_card_not_present_processors,
        ignore_address_verification_system=True
    )

    features_card_present_processors = {
        "VPC": CardProcessingConfigFeaturesCardPresentProcessors(
            default_point_of_sale_terminal_id="223344"
        ).__dict__
    }

    features_card_present = CardProcessingConfigFeaturesCardPresent(
        processors=features_card_present_processors
    )

    features_config = CardProcessingConfigFeatures(
        card_not_present=features_card_not_present.__dict__,
        card_present=features_card_present.__dict__
    )

    configurations = CardProcessingConfig(
        common=common_config.__dict__,
        features=features_config.__dict__
    )

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation(
        template_id=str(uuid.UUID("D671CE88-2F09-469C-A1B4-52C47812F792")),
        configurations=configurations.__dict__
    )

    card_processing = PaymentsProductsCardProcessing(
        subscription_information=subscription_information.__dict__,
        configuration_information=configuration_information.__dict__
    )

    payments = PaymentsProducts(
        card_processing=card_processing.__dict__,
        virtual_terminal=PaymentsProductsVirtualTerminal(
            subscription_information={"enabled": True},
            configuration_information={
                "template_id": str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))
            }
        ).__dict__,
        customer_invoicing=PaymentsProductsTax(
            subscription_information={"enabled": True}
        ).__dict__
    )

    selected_products.payments = payments.__dict__

    # Risk
    risk = RiskProducts()
    selected_products.risk = risk.__dict__

    # Commerce Solutions
    token_management = CommerceSolutionsProductsTokenManagement(
        subscription_information={"enabled": True},
        configuration_information={
            "template_id": str(uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA"))
        }
    )

    commerce_solutions = CommerceSolutionsProducts(
        token_management=token_management.__dict__
    )
    selected_products.commerce_solutions = commerce_solutions.__dict__

    # Value-Added Services
    value_added_services = ValueAddedServicesProducts(
        transaction_search=PaymentsProductsTax(
            subscription_information={"enabled": True}
        ).__dict__,
        reporting=PaymentsProductsTax(
            subscription_information={"enabled": True}
        ).__dict__
    )

    selected_products.value_added_services = value_added_services.__dict__

    product_information.selected_products = selected_products.__dict__
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
    merchant_boarding_vpc()
