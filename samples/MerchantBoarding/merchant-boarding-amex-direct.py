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

def merchant_boarding_amex_direct():
    

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
        common.merchant_category_code = "1799"
        merchant_descriptor_information = CardProcessingConfigCommonMerchantDescriptorInformation()
        merchant_descriptor_information.city = "Cupertino"
        merchant_descriptor_information.country = "USA"
        merchant_descriptor_information.name = "Mer name"
        merchant_descriptor_information.phone = "8885554444"
        merchant_descriptor_information.zip = "94043"
        merchant_descriptor_information.state = "CA"
        merchant_descriptor_information.street = "mer street"
        merchant_descriptor_information.url = "www.test.com"

        common.merchant_descriptor_information = merchant_descriptor_information.__dict__

        common.sub_merchant_id = "123457"
        common.sub_merchant_business_name = "bus name"

        processors = {}
        obj2 = CardProcessingConfigCommonProcessors()
        acquirer = CardProcessingConfigCommonAcquirer()

        obj2.acquirer = acquirer.__dict__
        currencies = {}
        obj3 = CardProcessingConfigCommonCurrencies1()
        obj3.enabled = True
        obj3.enabled_card_present = False
        obj3.enabled_card_present = True
        obj3.terminal_id = ""
        obj3.service_enablement_number = "1234567890"
        currencies["AED"] = obj3.__dict__
        currencies["FJD"] = obj3.__dict__
        currencies["USD"] = obj3.__dict__

        obj2.currencies = currencies

        payment_types = {}
        obj4 = CardProcessingConfigCommonPaymentTypes()
        obj4.enabled = True
        payment_types["AMERICAN_EXPRESS"] = obj4.__dict__

        obj2.payment_types = payment_types
        obj2.allow_multiple_bills = False
        obj2.avs_format = "basic"
        obj2.batch_group = "amexdirect_vme_default"
        obj2.enable_auto_auth_reversal_after_void = False
        obj2.enhanced_data = "disabled"
        obj2.enable_level2 = False
        obj2.amex_transaction_advice_addendum1 = "amex123"
        processors["acquirer"] = obj2.__dict__

        common.processors = processors
        configurations.common = common.__dict__

        features2 = CardProcessingConfigFeatures()
        card_not_present = CardProcessingConfigFeaturesCardNotPresent()

        processors3 = {}
        obj5 = CardProcessingConfigFeaturesCardNotPresentProcessors()
        obj5.relax_address_verification_system = True
        obj5.relax_address_verification_system_allow_expired_card = True
        obj5.relax_address_verification_system_allow_zip_without_country = False
        processors3["amexdirect"] = obj5.__dict__

        card_not_present.processors = processors3
        features2.card_not_present = card_not_present.__dict__
        configurations.features = features2.__dict__
        configuration_information.configurations = configurations.__dict__
        template_id = uuid.UUID("2B80A3C7-5A39-4CC3-9882-AC4A828D3646").__dict__
        configuration_information.template_id = template_id
        card_processing.configuration_information = configuration_information.__dict__
        payments.card_processing = card_processing.__dict__

        virtual_terminal = PaymentsProductsVirtualTerminal()
        subscription_information2 = PaymentsProductsPayerAuthenticationSubscriptionInformation()

        subscription_information2.enabled = True
        virtual_terminal.subscription_information = subscription_information2.__dict__

        configuration_information3 = PaymentsProductsVirtualTerminalConfigurationInformation()

        template_id2 = uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5").__dict__
        configuration_information3.template_id = template_id2
        virtual_terminal.configuration_information = configuration_information3.__dict__
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
        configuration_information4 = CommerceSolutionsProductsTokenManagementConfigurationInformation()

        template_id3 = uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA").__dict__
        configuration_information4.template_id = template_id3
        token_management.configuration_information = configuration_information4.__dict__
        commerce_solutions.token_management = token_management.__dict__
        selected_products.commerce_solutions = commerce_solutions.__dict__

        value_added_services = ValueAddedServicesProducts()
        transaction_search = PaymentsProductsTax()
        subscription_information8 = PaymentsProductsPayerAuthenticationSubscriptionInformation()

        subscription_information8.enabled = True
        transaction_search.subscription_information = subscription_information8.__dict__

        value_added_services.transaction_search = transaction_search.__dict__
        reporting = PaymentsProductsTax()
        subscription_information9 = PaymentsProductsPayerAuthenticationSubscriptionInformation()

        subscription_information9.enabled = True
        reporting.subscription_information = subscription_information9.__dict__
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
    merchant_boarding_amex_direct()
