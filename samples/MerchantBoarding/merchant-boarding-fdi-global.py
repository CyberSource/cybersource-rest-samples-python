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

def merchant_boarding_fdi_global():


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
    features["cardPresent"] = obj1.__dict__
    subscription_information.features = features
    card_processing.subscription_information = subscription_information.__dict__

    configuration_information = PaymentsProductsCardProcessingConfigurationInformation()

    configurations = CardProcessingConfig()
    common = CardProcessingConfigCommon()
    common.merchant_category_code = "0742"
    common.default_auth_type_code = "PRE"
    common.process_level3_data = "ignored"
    common.master_card_assigned_id = "123456789"
    common.enable_partial_auth = True

    processors = {}
    obj5 = CardProcessingConfigCommonProcessors()
    acquirer = CardProcessingConfigCommonAcquirer()
    obj5.acquirer = acquirer.__dict__

    currencies = {}
    obj6 = CardProcessingConfigCommonCurrencies1()
    obj6.enabled = True
    obj6.enabled_card_present = False
    obj6.enabled_card_not_present = True
    obj6.merchant_id = "123456789mer"
    obj6.terminal_id = "12345ter"
    obj6.service_enablement_number = ""
    currencies["CHF"] = obj6.__dict__
    currencies["HRK"] = obj6.__dict__
    currencies["ERN"] = obj6.__dict__
    currencies["USD"] = obj6.__dict__

    obj5.currencies = currencies

    payment_types = {}
    obj7 = CardProcessingConfigCommonPaymentTypes()
    obj7.enabled = True
    payment_types["MASTERCARD"] = obj7.__dict__
    payment_types["DISCOVER"] = obj7.__dict__
    payment_types["JCB"] = obj7.__dict__
    payment_types["VISA"] = obj7.__dict__
    payment_types["AMERICAN_EXPRESS"] = obj7.__dict__
    payment_types["DINERS_CLUB"] = obj7.__dict__
    payment_types["CUP"] = obj7.__dict__
    currencies2 = {}
    ob1 = CardProcessingConfigCommonCurrencies()
    ob1.enabled = True
    ob1.terminal_id = "pint123"
    ob1.merchant_id = "pinm123"
    ob1.service_enablement_number = None
    currencies2["USD"] = ob1.__dict__
    obj7.currencies = currencies2
    payment_types["PIN_DEBIT"] = obj7.__dict__

    obj5.payment_types = payment_types
    obj5.batch_group = "fdiglobal_vme_default"
    obj5.enhanced_data = "disabled"
    obj5.enable_pos_network_switching = True
    obj5.enable_transaction_reference_number = True

    processors["fdiglobal"] = obj5.__dict__

    common.processors = processors
    configurations.common = common.__dict__

    features2 = CardProcessingConfigFeatures()

    card_not_present = CardProcessingConfigFeaturesCardNotPresent()

    processors3 = {}
    obj9 = CardProcessingConfigFeaturesCardNotPresentProcessors()
    obj9.relax_address_verification_system = True
    obj9.relax_address_verification_system_allow_expired_card = True
    obj9.relax_address_verification_system_allow_zip_without_country = True

    processors3["fdiglobal"] = obj9.__dict__
    card_not_present.processors = processors3

    card_not_present.visa_straight_through_processing_only = True
    card_not_present.amex_transaction_advice_addendum1 = "amex12345"
    card_not_present.ignore_address_verification_system = True
    features2.card_not_present = card_not_present.__dict__

    configurations.features = features2.__dict__
    configuration_information.configurations = configurations.__dict__
    template_id = str(uuid.UUID("685A1FC9-3CEC-454C-9D8A-19205529CE45"))
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
    merchant_boarding_fdi_global()
