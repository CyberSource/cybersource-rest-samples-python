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

def merchant_boarding_cup():


    # Create main request object
    req_obj = PostRegistrationBody()

    # Organization Information
    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    # Business Information
    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation(
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

    organization_info.business_information = business_info.__dict__
    req_obj.organization_information = organization_info.__dict__

    # Product Information
    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    # Payments Product
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features={
            "cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__,
            "cardPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
        }
    )

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation(
        configurations=CardProcessingConfig(
            common=CardProcessingConfigCommon(
                merchant_category_code="1799",
                processors={
                    "CUP": CardProcessingConfigCommonProcessors(
                        acquirer=CardProcessingConfigCommonAcquirer(
                            country_code="344_hongkong",
                            institution_id="22344"
                        ).__dict__,
                        currencies={
                            "HKD": CardProcessingConfigCommonCurrencies1(
                                enabled=True,
                                enabled_card_present=False,
                                enabled_card_not_present=True,
                                merchant_id="112233",
                                terminal_id="11224455",
                                service_enablement_number=""
                            ).__dict__,
                            "AUD": CardProcessingConfigCommonCurrencies1(
                                enabled=True,
                                enabled_card_present=False,
                                enabled_card_not_present=True,
                                merchant_id="112233",
                                terminal_id="11224455",
                                service_enablement_number=""
                            ).__dict__,
                            "USD": CardProcessingConfigCommonCurrencies1(
                                enabled=True,
                                enabled_card_present=False,
                                enabled_card_not_present=True,
                                merchant_id="112233",
                                terminal_id="11224455",
                                service_enablement_number=""
                            ).__dict__,
                        },
                        payment_types={
                            "CUP": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__
                        }
                    ).__dict__,
                }
            ).__dict__,
        ).__dict__,
        template_id=str(uuid.UUID("1D8BC41A-F04E-4133-87C8-D89D1806106F"))
    )

    card_processing = PaymentsProductsCardProcessing(
        subscription_information=subscription_information.__dict__,
        configuration_information=configuration_information.__dict__
    )

    virtual_terminal = PaymentsProductsVirtualTerminal(
        subscription_information=PaymentsProductsPayerAuthenticationSubscriptionInformation(enabled=True).__dict__,
        configuration_information=PaymentsProductsVirtualTerminalConfigurationInformation(
            template_id=str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))
        ).__dict__
    )

    customer_invoicing = PaymentsProductsTax(
        subscription_information=PaymentsProductsPayerAuthenticationSubscriptionInformation(enabled=True).__dict__
    )

    payments = PaymentsProducts(
        card_processing=card_processing.__dict__,
        virtual_terminal=virtual_terminal.__dict__,
        customer_invoicing=customer_invoicing.__dict__
    )

    selected_products.payments = payments.__dict__

    # Risk Product
    risk = RiskProducts()
    selected_products.risk = risk.__dict__

    # Commerce Solutions Product
    token_management = CommerceSolutionsProductsTokenManagement(
        subscription_information=PaymentsProductsPayerAuthenticationSubscriptionInformation(enabled=True).__dict__,
        configuration_information=CommerceSolutionsProductsTokenManagementConfigurationInformation(
            template_id=str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))
        ).__dict__
    )

    commerce_solutions = CommerceSolutionsProducts(
        token_management=token_management.__dict__
    )

    selected_products.commerce_solutions = commerce_solutions.__dict__

    # Value Added Services
    transaction_search = PaymentsProductsTax(
        subscription_information=PaymentsProductsPayerAuthenticationSubscriptionInformation(enabled=True).__dict__
    )

    reporting = PaymentsProductsTax(
        subscription_information=PaymentsProductsPayerAuthenticationSubscriptionInformation(enabled=True).__dict__
    )

    value_added_services = ValueAddedServicesProducts(
        transaction_search=transaction_search.__dict__,
        reporting=reporting.__dict__
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
    merchant_boarding_cup()
