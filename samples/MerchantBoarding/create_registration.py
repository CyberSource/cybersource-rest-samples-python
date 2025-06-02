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
    

    

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
    first_name="Stuart",
    last_name="Stuart",
    phone_number="6574567813",
    email="svc_email_bt@corpdev.visa.com"
    )

    # Business Address
    business_address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
    country="US",
    address1="123456 SandMarket",
    locality="ORMOND BEACH",
    administrative_area="FL",
    postal_code="32176"
    )

    # Business Information
    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation(
    name="StuartWickedFastEatz",
    address=business_address.__dict__,
    website_url="https://www.StuartWickedEats.com",
    phone_number="6574567813",
    business_contact=business_contact.__dict__,
    merchant_category_code="5999"
    )

    # Organization Information
    organization_information = Boardingv1registrationsOrganizationInformation(
    parent_organization_id="apitester00",
    type="MERCHANT",
    configurable=True,
    business_information=business_information.__dict__
    )

    # Payer Authentication
    currency1 = PayerAuthConfigCardTypesVerifiedByVisaCurrencies(
    currency_codes=["ALL"],
    acquirer_id="469216",
    processor_merchant_id="678855"
    )
    verified_by_visa = PayerAuthConfigCardTypesVerifiedByVisa(
    currencies=[currency1.__dict__]
    )
    card_types = PayerAuthConfigCardTypes(
    verified_by_visa=verified_by_visa.__dict__
    )
    configurations = PayerAuthConfig(
    card_types=card_types.__dict__
    )
    configuration_information = PaymentsProductsPayerAuthenticationConfigurationInformation(
    configurations=configurations.__dict__
    )
    payer_authentication = PaymentsProductsPayerAuthentication(
    configuration_information=configuration_information.__dict__
    )

    # Card Processing
    merchant_descriptor_information = CardProcessingConfigCommonMerchantDescriptorInformation(
    name="r4ef",
    city="Bellevue",
    country="US",
    phone="4255547845",
    state="WA",
    street="StreetName",
    zip="98007"
    )
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
    common = CardProcessingConfigCommon(
    merchant_category_code="1234",
    merchant_descriptor_information=merchant_descriptor_information.__dict__,
    processors=processors
    )
    features = CardProcessingConfigFeatures(
    card_not_present=CardProcessingConfigFeaturesCardNotPresent(
        visa_straight_through_processing_only=True
    ).__dict__
    )
    configurations2 = CardProcessingConfig(
    common=common.__dict__,
    features=features.__dict__
    )
    configuration_information2 = PaymentsProductsCardProcessingConfigurationInformation(
    configurations=configurations2.__dict__
    )
    card_processing = PaymentsProductsCardProcessing(
    subscription_information=PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features={"cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__}
    ).__dict__,
    configuration_information=configuration_information2.__dict__
    )

    # Virtual Terminal
    virtual_terminal = PaymentsProductsVirtualTerminal(
    )

    # Customer Invoicing
    customer_invoicing = PaymentsProductsTax(
    )

    # Payouts
    payouts = PaymentsProductsPayouts(
    )

    # Commerce Solutions
    token_management = CommerceSolutionsProductsTokenManagement(
    )
    commerce_solutions = CommerceSolutionsProducts(
    token_management=token_management.__dict__
    )

    # Risk
    configuration_information5 = RiskProductsFraudManagementEssentialsConfigurationInformation(
    template_id="E4EDB280-9DAC-4698-9EB9-9434D40FF60C"
    )
    fraud_management_essentials = RiskProductsFraudManagementEssentials(
    configuration_information=configuration_information5.__dict__
    )
    risk = RiskProducts(
    fraud_management_essentials=fraud_management_essentials.__dict__
    )

    # Selected Products
    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
    payments=PaymentsProducts(
        payer_authentication=payer_authentication.__dict__,
        card_processing=card_processing.__dict__,
        virtual_terminal=virtual_terminal.__dict__,
        customer_invoicing=customer_invoicing.__dict__,
        payouts=payouts.__dict__
    ).__dict__,
    commerce_solutions=commerce_solutions.__dict__,
    risk=risk.__dict__
    )

    # Product Information
    product_information = Boardingv1registrationsProductInformation(
    selected_products=selected_products.__dict__
    )

    # Final Request Object
    req_obj = PostRegistrationBody(
    organization_information=organization_information.__dict__,
    product_information=product_information.__dict__
    )

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
