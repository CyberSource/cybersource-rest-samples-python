from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader
from uuid import UUID

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

def merchant_boarding_barclays():


    req_obj = PostRegistrationBody()

    # Organization Information
    address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
        country="US",
        address1="123456 SandMarket",
        locality="ORMOND BEACH",
        administrative_area="FL",
        postal_code="32176"
    )

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
        first_name="Stuart",
        last_name="Stuart",
        phone_number="6574567813",
        email="svc_email_bt@corpdev.visa.com"
    )

    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=address.__dict__,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=business_contact.__dict__,
        merchant_category_code="5999"
    )

    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True,
        business_information=business_info.__dict__
    )

    req_obj.organization_information = organization_info.__dict__

    # Product Information
    card_processing_subscription_info = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features={
            "cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__,
            "cardPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
        }
    )

    card_processing_processors = {
        "barclays2": CardProcessingConfigCommonProcessors(
            acquirer=CardProcessingConfigCommonAcquirer().__dict__,
            currencies={
                "AED": CardProcessingConfigCommonCurrencies1(
                    enabled=True,
                    enabled_card_present=False,
                    enabled_card_not_present=True,
                    merchant_id="1234",
                    service_enablement_number="",
                    terminal_ids=["12351245"]
                ).__dict__,
                "USD": CardProcessingConfigCommonCurrencies1(
                    enabled=True,
                    enabled_card_present=False,
                    enabled_card_not_present=True,
                    merchant_id="1234",
                    service_enablement_number="",
                    terminal_ids=["12351245"]
                ).__dict__
            },
            payment_types={
                "MASTERCARD": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
                "VISA": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__
            },
            batch_group="barclays2_16",
            quasi_cash=False,
            enhanced_data="disabled",
            merchant_id="124555",
            enable_multi_currency_processing="false"
        ).__dict__
    }

    common_config = CardProcessingConfigCommon(
        merchant_category_code="5999",
        default_auth_type_code="FINAL",
        processors=card_processing_processors
    )

    card_not_present_processors = {
        "barclays2": CardProcessingConfigFeaturesCardNotPresentProcessors(
            payouts=CardProcessingConfigFeaturesCardNotPresentPayouts(
                merchant_id="1233",
                terminal_id="1244"
            ).__dict__
        ).__dict__
    }

    features_config = CardProcessingConfigFeatures(
        card_not_present=CardProcessingConfigFeaturesCardNotPresent(
            processors=card_not_present_processors
        ).__dict__
    )

    card_processing_configuration = PaymentsProductsCardProcessingConfigurationInformation(
        configurations=CardProcessingConfig(
            common=common_config.__dict__,
            features=features_config.__dict__
        ).__dict__,
        template_id=str(UUID("0A413572-1995-483C-9F48-FCBE4D0B2E86"))
    )

    card_processing = PaymentsProductsCardProcessing(
        subscription_information=card_processing_subscription_info.__dict__,
        configuration_information=card_processing_configuration.__dict__
    )

    virtual_terminal_configuration = PaymentsProductsVirtualTerminalConfigurationInformation(
        template_id=str(UUID("E4EDB280-9DAC-4698-9EB9-9434D40FF60C"))
    )

    virtual_terminal = PaymentsProductsVirtualTerminal(
        configuration_information=virtual_terminal_configuration.__dict__
    )

    customer_invoicing = PaymentsProductsTax(
    )

    token_management_configuration = CommerceSolutionsProductsTokenManagementConfigurationInformation(
        template_id=str(UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA"))
    )

    token_management = CommerceSolutionsProductsTokenManagement(
        configuration_information=token_management_configuration.__dict__
    )

    transaction_search = PaymentsProductsTax(
    )

    reporting = PaymentsProductsTax(
    )

    value_added_services = ValueAddedServicesProducts(
        transaction_search=transaction_search.__dict__,
        reporting=reporting.__dict__
    )

    payments = PaymentsProducts(
        card_processing=card_processing.__dict__,
        virtual_terminal=virtual_terminal.__dict__,
        customer_invoicing=customer_invoicing.__dict__
    )

    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
        payments=payments.__dict__,
        risk=RiskProducts().__dict__,
        commerce_solutions=CommerceSolutionsProducts(
            token_management=token_management.__dict__
        ).__dict__,
        value_added_services=value_added_services.__dict__
    )

    product_info = Boardingv1registrationsProductInformation(
        selected_products=selected_products.__dict__
    )

    req_obj.product_information = product_info.__dict__
    

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
    merchant_boarding_barclays()
