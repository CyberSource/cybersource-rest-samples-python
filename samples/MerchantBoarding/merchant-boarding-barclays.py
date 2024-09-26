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

    organization_info = Boardingv1registrationsOrganizationInformation()
    organization_info.parent_organization_id = "apitester00"
    organization_info.type = "MERCHANT"
    organization_info.configurable = True

    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation()
    business_info.name = "StuartWickedFastEatz"

    address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress()
    address.country = "US"
    address.address1 = "123456 SandMarket"
    address.locality = "ORMOND BEACH"
    address.administrative_area = "FL"
    address.postal_code = "32176"
    business_info.address = address.__dict__
    business_info.website_url = "https://www.StuartWickedEats.com"
    business_info.phone_number = "6574567813"

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact()
    business_contact.first_name = "Stuart"
    business_contact.last_name = "Stuart"
    business_contact.phone_number = "6574567813"
    business_contact.email = "svc_email_bt@corpdev.visa.com"
    business_info.business_contact = business_contact.__dict__
    business_info.merchant_category_code = "5999"
    organization_info.business_information = business_info.__dict__

    req_obj.organization_information = organization_info.__dict__

    product_info = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    payments = PaymentsProducts()
    card_processing = PaymentsProductsCardProcessing()
    subscription_info = PaymentsProductsCardProcessingSubscriptionInformation()
    subscription_info.enabled = True

    features = {
        "cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__,
        "cardPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
    }
    subscription_info.features = features
    card_processing.subscription_information = subscription_info.__dict__

    configuration_info = PaymentsProductsCardProcessingConfigurationInformation()
    configurations = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "5999"
    common.default_auth_type_code = "FINAL"

    processors = {
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
    common.processors = processors
    configurations.common = common.__dict__
    features3 = CardProcessingConfigFeatures()
    card_not_present = CardProcessingConfigFeaturesCardNotPresent()
    processors4 = {
        "barclays2": CardProcessingConfigFeaturesCardNotPresentProcessors(
            payouts=CardProcessingConfigFeaturesCardNotPresentPayouts(
                merchant_id="1233",
                terminal_id="1244"
            ).__dict__
        ).__dict__
    }
    card_not_present.processors = processors4
    features3.card_not_present = card_not_present.__dict__
    configurations.features = features3.__dict__
    configuration_info.configurations = configurations.__dict__
    configuration_info.template_id = UUID("0A413572-1995-483C-9F48-FCBE4D0B2E86").__dict__
    card_processing.configuration_information = configuration_info.__dict__
    payments.card_processing = card_processing.__dict__

    virtual_terminal = PaymentsProductsVirtualTerminal()
    subscription_info2 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_info2.enabled = True
    virtual_terminal.subscription_information = subscription_info2.__dict__
    configuration_info2 = PaymentsProductsVirtualTerminalConfigurationInformation()
    configuration_info2.template_id = UUID("E4EDB280-9DAC-4698-9EB9-9434D40FF60C").__dict__
    virtual_terminal.configuration_information = configuration_info2.__dict__
    payments.virtual_terminal = virtual_terminal.__dict__

    customer_invoicing = PaymentsProductsTax()
    subscription_info3 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_info3.enabled = True
    customer_invoicing.subscription_information = subscription_info3.__dict__
    payments.customer_invoicing = customer_invoicing.__dict__

    selected_products.payments = payments.__dict__

    risk2 = RiskProducts()
    selected_products.risk = risk2.__dict__

    commerce_solutions = CommerceSolutionsProducts()
    token_management = CommerceSolutionsProductsTokenManagement()
    subscription_info5 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_info5.enabled = True
    token_management.subscription_information = subscription_info5.__dict__
    configuration_info5 = CommerceSolutionsProductsTokenManagementConfigurationInformation()
    configuration_info5.template_id = UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA").__dict__
    token_management.configuration_information = configuration_info5.__dict__
    commerce_solutions.token_management = token_management.__dict__
    selected_products.commerce_solutions = commerce_solutions.__dict__

    value_added_services = ValueAddedServicesProducts()
    transaction_search = PaymentsProductsTax()
    subscription_info6 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_info6.enabled = True
    transaction_search.subscription_information = subscription_info6.__dict__
    value_added_services.transaction_search = transaction_search.__dict__

    reporting = PaymentsProductsTax()
    subscription_info7 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_info7.enabled = True
    reporting.subscription_information = subscription_info7.__dict__
    value_added_services.reporting = reporting.__dict__
    selected_products.value_added_services = value_added_services.__dict__

    product_info.selected_products = selected_products.__dict__
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
