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

    # Creating the main request object
    req_obj = PostRegistrationBody()

    # Organization Information
    organization_information = Boardingv1registrationsOrganizationInformation()
    organization_information.parent_organization_id = "apitester00"
    organization_information.type = "MERCHANT"
    organization_information.configurable = True

    # Business Information
    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation()
    business_information.name = "StuartWickedFastEatz"

    # Address Information
    address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress()
    address.country = "US"
    address.address1 = "123456 SandMarket"
    address.locality = "ORMOND BEACH"
    address.administrative_area = "FL"
    address.postal_code = "32176"

    # Assigning address to business information
    business_information.address = address.__dict__
    business_information.website_url = "https://www.StuartWickedEats.com"
    business_information.phone_number = "6574567813"

    # Business Contact Information
    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact()
    business_contact.first_name = "Stuart"
    business_contact.last_name = "Stuart"
    business_contact.phone_number = "6574567813"
    business_contact.email = "svc_email_bt@corpdev.visa.com"

    # Assigning business contact to business information
    business_information.business_contact = business_contact.__dict__
    business_information.merchant_category_code = "5999"

    # Assigning business information to organization information
    organization_information.business_information = business_information.__dict__

    # Assigning organization information to request object
    req_obj.organization_information = organization_information.__dict__

    # Product Information
    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    # Payments Product
    payments = PaymentsProducts()
    card_processing = PaymentsProductsCardProcessing()
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation()

    subscription_information.enabled = True
    features = {}

    # Card Processing Features
    obj1 = PaymentsProductsCardProcessingSubscriptionInformationFeatures()
    obj1.enabled = True
    features["cardNotPresent"] = obj1.__dict__
    features["cardPresent"] = obj1.__dict__

    subscription_information.features = features
    card_processing.subscription_information = subscription_information.__dict__

    # Card Processing Configuration Information
    configuration_information = PaymentsProductsCardProcessingConfigurationInformation()
    configurations = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "1799"
    processors = {}

    # Common Processors
    obj2 = CardProcessingConfigCommonProcessors()
    acquirer = CardProcessingConfigCommonAcquirer()
    acquirer.country_code = "344_hongkong"
    acquirer.institution_id = "22344"
    obj2.acquirer = acquirer.__dict__

    currencies = {}

    # Common Currencies
    obj3 = CardProcessingConfigCommonCurrencies1()
    obj3.enabled = True
    obj3.enabled_card_present = False
    obj3.enabled_card_not_present = True
    obj3.merchant_id = "112233"
    obj3.terminal_id = "11224455"
    obj3.service_enablement_number = ""
    currencies["HKD"] = obj3.__dict__
    currencies["AUD"] = obj3.__dict__
    currencies["USD"] = obj3.__dict__

    obj2.currencies = currencies

    payment_types = {}

    # Common Payment Types
    obj4 = CardProcessingConfigCommonPaymentTypes()
    obj4.enabled = True
    payment_types["CUP"] = obj4.__dict__
    obj2.payment_types = payment_types

    processors["CUP"] = obj2.__dict__
    common.processors = processors
    configurations.common = common.__dict__
    configuration_information.configurations = configurations.__dict__

    template_id = uuid.UUID("1D8BC41A-F04E-4133-87C8-D89D1806106F").__dict__
    configuration_information.template_id = template_id
    card_processing.configuration_information = configuration_information.__dict__
    payments.card_processing = card_processing.__dict__

    # Virtual Terminal
    virtual_terminal = PaymentsProductsVirtualTerminal()
    subscription_information2 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information2.enabled = True
    virtual_terminal.subscription_information = subscription_information2.__dict__

    configuration_information2 = PaymentsProductsVirtualTerminalConfigurationInformation()
    template_id2 = uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5").__dict__
    configuration_information2.template_id = template_id2
    virtual_terminal.configuration_information = configuration_information2.__dict__
    payments.virtual_terminal = virtual_terminal.__dict__

    # Customer Invoicing
    customer_invoicing = PaymentsProductsTax()
    subscription_information3 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information3.enabled = True
    customer_invoicing.subscription_information = subscription_information3.__dict__
    payments.customer_invoicing = customer_invoicing.__dict__
    selected_products.payments = payments.__dict__

    # Risk Product
    risk = RiskProducts()
    selected_products.risk = risk.__dict__

    # Commerce Solutions Product
    commerce_solutions = CommerceSolutionsProducts()
    token_management = CommerceSolutionsProductsTokenManagement()
    subscription_information4 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information4.enabled = True
    token_management.subscription_information = subscription_information4.__dict__

    configuration_information3 = CommerceSolutionsProductsTokenManagementConfigurationInformation()
    template_id3 = uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5").__dict__
    configuration_information3.template_id = template_id3
    token_management.configuration_information = configuration_information3.__dict__
    commerce_solutions.token_management = token_management.__dict__
    selected_products.commerce_solutions = commerce_solutions.__dict__

    # Value Added Services
    value_added_services = ValueAddedServicesProducts()

    transaction_search = PaymentsProductsTax()
    subscription_information5 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information5.enabled = True
    transaction_search.subscription_information = subscription_information5.__dict__
    value_added_services.transaction_search = transaction_search.__dict__

    reporting = PaymentsProductsTax()
    reporting.subscription_information = subscription_information5.__dict__
    value_added_services.reporting = reporting.__dict__

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
