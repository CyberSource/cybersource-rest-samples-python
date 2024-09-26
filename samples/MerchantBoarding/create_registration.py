from CyberSource import *
from pathlib import Path
import os
import json
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

def create_registration():
    

    

    req_obj = PostRegistrationBody()

    organization_information = Boardingv1registrationsOrganizationInformation()
    organization_information.parent_organization_id = "apitester00"
    #organization_information.type = Boardingv1registrationsOrganizationInformation.TypeEnum.MERCHANT
    organization_information.type = "MERCHANT"
    organization_information.configurable = True

    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation()
    business_information.name = "StuartWickedFastEatz"

    address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress()
    address.country = "US"
    address.address1 = "123456 SandMarket"
    address.locality = "ORMOND BEACH"
    address.administrative_area = "FL"
    address.postal_code = "32176"
    business_information.address = address.__dict__

    business_information.website_url = "https://www.StuartWickedEats.com"
    business_information.phone_number = "6574567813"

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact()
    business_contact.first_name = "Stuart"
    business_contact.last_name = "Stuart"
    business_contact.phone_number = "6574567813"
    business_contact.email = "svc_email_bt@corpdev.visa.com"
    business_information.business_contact = business_contact.__dict__
    business_information.merchant_category_code = "5999"
    organization_information.business_information = business_information.__dict__

    req_obj.organization_information = organization_information.__dict__

    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    payments = PaymentsProducts()

    # Payer Authentication
    payer_authentication = PaymentsProductsPayerAuthentication()
    subscription_information = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information.enabled = True
    payer_authentication.subscription_information = subscription_information.__dict__

    configuration_information = PaymentsProductsPayerAuthenticationConfigurationInformation()
    configurations = PayerAuthConfig()
    card_types = PayerAuthConfigCardTypes()
    verified_by_visa = PayerAuthConfigCardTypesVerifiedByVisa()
    currencies = []

    currency1 = PayerAuthConfigCardTypesVerifiedByVisaCurrencies()
    currency1.currency_codes = ["ALL"]
    currency1.acquirer_id = "469216"
    currency1.processor_merchant_id = "678855"
    currencies.append(currency1.__dict__)

    verified_by_visa.currencies = currencies
    card_types.verified_by_visa = verified_by_visa.__dict__
    configurations.card_types = card_types.__dict__
    configuration_information.configurations = configurations.__dict__
    payer_authentication.configuration_information = configuration_information.__dict__
    payments.payer_authentication = payer_authentication.__dict__

    # Card Processing
    card_processing = PaymentsProductsCardProcessing()
    subscription_information2 = PaymentsProductsCardProcessingSubscriptionInformation()
    subscription_information2.enabled = True
    features = {"cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__}
    subscription_information2.features = features
    card_processing.subscription_information = subscription_information2.__dict__

    configuration_information2 = PaymentsProductsCardProcessingConfigurationInformation()
    configurations2 = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "1234"

    merchant_descriptor_information = CardProcessingConfigCommonMerchantDescriptorInformation()
    merchant_descriptor_information.name = "r4ef"
    merchant_descriptor_information.city = "Bellevue"
    merchant_descriptor_information.country = "US"
    merchant_descriptor_information.phone = "4255547845"
    merchant_descriptor_information.state = "WA"
    merchant_descriptor_information.street = "StreetName"
    merchant_descriptor_information.zip = "98007"
    common.merchant_descriptor_information = merchant_descriptor_information.__dict__

    processors = {"tsys": CardProcessingConfigCommonProcessors(
        merchant_id="123456789101",
        terminal_id="1231",
        industry_code="D",
        vital_number="71234567",
        merchant_bin_number="123456",
        merchant_location_number="00001",
        store_id="1234",
        settlement_currency="USD"
    ).__dict__}
    common.processors = processors
    configurations2.common = common.__dict__

    features2 = CardProcessingConfigFeatures()
    card_not_present = CardProcessingConfigFeaturesCardNotPresent()
    card_not_present.visa_straight_through_processing_only = True
    features2.card_not_present = card_not_present.__dict__
    configurations2.features = features2.__dict__
    configuration_information2.configurations = configurations2.__dict__
    card_processing.configuration_information = configuration_information2.__dict__
    payments.card_processing = card_processing.__dict__

    # Virtual Terminal
    virtual_terminal = PaymentsProductsVirtualTerminal()
    subscription_information3 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information3.enabled = True
    virtual_terminal.subscription_information = subscription_information3.__dict__
    payments.virtual_terminal = virtual_terminal.__dict__

    # Customer Invoicing
    customer_invoicing = PaymentsProductsTax()
    subscription_information4 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information4.enabled = True
    customer_invoicing.subscription_information = subscription_information4.__dict__
    payments.customer_invoicing = customer_invoicing.__dict__

    # Payouts
    payouts = PaymentsProductsPayouts()
    subscription_information5 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information5.enabled = True
    payouts.subscription_information = subscription_information5.__dict__
    payments.payouts = payouts.__dict__

    selected_products.payments = payments.__dict__

    # Commerce Solutions
    commerce_solutions = CommerceSolutionsProducts()
    token_management = CommerceSolutionsProductsTokenManagement()
    subscription_information6 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information6.enabled = True
    token_management.subscription_information = subscription_information6.__dict__
    commerce_solutions.token_management = token_management.__dict__
    selected_products.commerce_solutions = commerce_solutions.__dict__

    # Risk
    risk = RiskProducts()
    fraud_management_essentials = RiskProductsFraudManagementEssentials()
    subscription_information7 = PaymentsProductsPayerAuthenticationSubscriptionInformation()
    subscription_information7.enabled = True
    fraud_management_essentials.subscription_information = subscription_information7.__dict__

    configuration_information5 = RiskProductsFraudManagementEssentialsConfigurationInformation()
    template_id = "E4EDB280-9DAC-4698-9EB9-9434D40FF60C"
    configuration_information5.template_id = template_id
    fraud_management_essentials.configuration_information = configuration_information5.__dict__
    risk.fraud_management_essentials = fraud_management_essentials.__dict__

    selected_products.risk = risk.__dict__
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
    create_registration()
