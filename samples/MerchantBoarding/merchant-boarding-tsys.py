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

    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    payments = PaymentsProducts()
    card_processing = PaymentsProductsCardProcessing()
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation()

    subscription_information.enabled = True
    features = {}

    obj1 = PaymentsProductsCardProcessingSubscriptionInformationFeatures()
    obj1.enabled = True
    features["cardNotPresent"] = obj1.__dict__
    features["cardPresent"] = obj1.__dict__
    subscription_information.features = features
    card_processing.subscription_information = subscription_information.__dict__

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation()

    configurations = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "5999"
    common.process_level3_data = "ignored"
    common.default_auth_type_code = "FINAL"
    common.enable_partial_auth = False
    common.amex_vendor_code = "2233"

    merchant_descriptor_information = CardProcessingConfigCommonMerchantDescriptorInformation()

    merchant_descriptor_information.city = "cupertino"
    merchant_descriptor_information.country = "USA"
    merchant_descriptor_information.name = "kumar"
    merchant_descriptor_information.state = "CA"
    merchant_descriptor_information.phone = "888555333"
    merchant_descriptor_information.zip = "94043"
    merchant_descriptor_information.street = "steet1"

    common.merchant_descriptor_information = merchant_descriptor_information.__dict__

    processors = {}
    obj5 = CardProcessingConfigCommonProcessors()
    acquirer = CardProcessingConfigCommonAcquirer()

    obj5.acquirer = acquirer.__dict__

    currencies = {}

    obj6 = CardProcessingConfigCommonCurrencies1()
    obj6.enabled = True
    obj6.enabled_card_present = True
    obj6.enabled_card_not_present = True
    obj6.terminal_id = "1234"
    obj6.service_enablement_number = ""

    currencies["CAD"] = obj6.__dict__

    obj5.currencies = currencies

    payment_types = {}
    obj7 = CardProcessingConfigCommonPaymentTypes()
    obj7.enabled = True

    payment_types["MASTERCARD"] = obj7.__dict__
    payment_types["VISA"] = obj7.__dict__

    obj5.payment_types = payment_types

    obj5.bank_number = "234576"
    obj5.chain_number = "223344"
    obj5.batch_group = "vital_1130"
    obj5.enhanced_data = "disabled"
    obj5.industry_code = "D"
    obj5.merchant_bin_number = "765576"
    obj5.merchant_id = "834215123456"
    obj5.merchant_location_number = "00001"
    obj5.store_id = "2563"
    obj5.vital_number = "71234567"
    obj5.quasi_cash = False
    obj5.send_amex_level2_data = None
    obj5.soft_descriptor_type = "1 - trans_ref_no"
    obj5.travel_agency_code = "2356"
    obj5.travel_agency_name = "Agent"

    processors["tsys"] = obj5.__dict__

    common.processors = processors

    configurations.common = common.__dict__

    features2 = CardProcessingConfigFeatures()

    card_not_present = CardProcessingConfigFeaturesCardNotPresent()

    card_not_present.visa_straight_through_processing_only = False
    card_not_present.amex_transaction_advice_addendum1 = None

    features2.card_not_present = card_not_present.__dict__

    configurations.features = features2.__dict__
    configuration_information.configurations = configurations.__dict__
    template_id = uuid.UUID("818048AD-2860-4D2D-BC39-2447654628A1").__dict__
    configuration_information.template_id = template_id

    card_processing.configuration_information = configuration_information.__dict__
    payments.card_processing = card_processing.__dict__

    virtual_terminal = PaymentsProductsVirtualTerminal()
    subscription_information5 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information5.enabled = True
    virtual_terminal.subscription_information = subscription_information5.__dict__

    configuration_information5 = PaymentsProductsVirtualTerminalConfigurationInformation()
    template_id2 = uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5").__dict__
    configuration_information5.template_id = template_id2
    virtual_terminal.configuration_information = configuration_information5.__dict__

    payments.virtual_terminal = virtual_terminal.__dict__

    customer_invoicing = PaymentsProductsTax()

    subscription_information6 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information6.enabled = True
    customer_invoicing.subscription_information = subscription_information6.__dict__
    payments.customer_invoicing = customer_invoicing.__dict__

    selected_products.payments = payments.__dict__

    risk = RiskProducts()

    selected_products.risk = risk.__dict__

    commerce_solutions = CommerceSolutionsProducts()

    token_management = CommerceSolutionsProductsTokenManagement()

    subscription_information7 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information7.enabled = True
    token_management.subscription_information = subscription_information7.__dict__

    configuration_information7 = CommerceSolutionsProductsTokenManagementConfigurationInformation()

    template_id3 = uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA").__dict__
    configuration_information7.template_id = template_id3
    token_management.configuration_information = configuration_information7.__dict__

    commerce_solutions.token_management = token_management.__dict__
    selected_products.commerce_solutions = commerce_solutions.__dict__

    value_added_services = ValueAddedServicesProducts()

    transaction_search = PaymentsProductsTax()

    subscription_information9 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information9.enabled = True
    transaction_search.subscription_information = subscription_information9.__dict__
    value_added_services.transaction_search = transaction_search.__dict__

    reporting = PaymentsProductsTax()
    subscription_information3 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information3.enabled = True
    reporting.subscription_information = subscription_information3.__dict__
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
    merchant_boarding_tsys()
