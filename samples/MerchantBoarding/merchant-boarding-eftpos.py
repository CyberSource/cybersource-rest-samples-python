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

    req_obj = PostRegistrationBody()

    organization_information = Boardingv1registrationsOrganizationInformation()
    organization_information.parent_organization_id = "apitester00"
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
    card_processing = PaymentsProductsCardProcessing()
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation()
    subscription_information.enabled = True

    features = {}

    obj1 = PaymentsProductsCardProcessingSubscriptionInformationFeatures()
    obj1.enabled = True
    features["cardNotPresent"] = obj1.__dict__

    obj1.enabled = False
    features["cardPresent"] = obj1.__dict__

    subscription_information.features = features
    card_processing.subscription_information = subscription_information.__dict__

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation()
    configurations = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "5999"
    common.prefer_cobadged_secondary_brand = True

    processors = {}

    obj5 = CardProcessingConfigCommonProcessors()
    acquirer = CardProcessingConfigCommonAcquirer()
    acquirer.country_code = "344_hongkong"
    acquirer.institution_id = "22344"

    obj5.acquirer = acquirer.__dict__

    currencies = {}

    obj6 = CardProcessingConfigCommonCurrencies1()
    obj6.enabled = True
    obj6.merchant_id = "12345612344"
    obj6.terminal_id = "12121212"
    currencies["AUD"] = obj6.__dict__

    obj5.currencies = currencies

    payment_types = {}

    obj7 = CardProcessingConfigCommonPaymentTypes()
    obj7.enabled = True
    payment_types["EFTPOS"] = obj7.__dict__

    obj5.payment_types = payment_types
    obj5.enable_cvv_response_indicator = True
    obj5.enable_least_cost_routing = True
    obj5.merchant_tier = "000"

    processors["EFTPOS"] = obj5.__dict__

    common.processors = processors
    configurations.common = common.__dict__

    features2 = CardProcessingConfigFeatures()
    configurations.features = features2.__dict__
    configuration_information.configurations = configurations.__dict__

    template_id = uuid.UUID("1F9B7F6E-F0DB-44C8-BF8E-5013E34C0F87").__dict__
    configuration_information.template_id = template_id

    card_processing.configuration_information = configuration_information.__dict__
    payments.card_processing = card_processing.__dict__
    selected_products.payments = payments.__dict__

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
    merchant_boarding_eftpos()
