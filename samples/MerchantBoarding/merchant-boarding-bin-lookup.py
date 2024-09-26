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

def merchant_boarding_bin_lookup():

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
    selected_products.payments = payments.__dict__

    # Risk Product
    risk = RiskProducts()
    selected_products.risk = risk.__dict__

    # Commerce Solutions Product
    commerce_solutions = CommerceSolutionsProducts()
    bin_lookup = CommerceSolutionsProductsBinLookup()
    subscription_information = PaymentsProductsPayerAuthenticationSubscriptionInformation()

    subscription_information.enabled = True
    bin_lookup.subscription_information = subscription_information.__dict__

    configuration_information = CommerceSolutionsProductsBinLookupConfigurationInformation()
    configurations = CommerceSolutionsProductsBinLookupConfigurationInformationConfigurations()

    configurations.is_payout_options_enabled = False
    configurations.is_account_prefix_enabled = True

    configuration_information.configurations = configurations.__dict__
    bin_lookup.configuration_information = configuration_information.__dict__

    commerce_solutions.bin_lookup = bin_lookup.__dict__
    selected_products.commerce_solutions = commerce_solutions.__dict__

    # Value Added Services
    value_added_services = ValueAddedServicesProducts()
    selected_products.value_added_services = value_added_services.__dict__

    # Assigning selected products to product information
    product_information.selected_products = selected_products.__dict__

    # Assigning product information to request object
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
    merchant_boarding_bin_lookup()
