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


    req_obj = PostRegistrationBody()

    # Organization Information
    organization_information = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    # Address Information
    address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
        country="US",
        address1="123456 SandMarket",
        locality="ORMOND BEACH",
        administrative_area="FL",
        postal_code="32176"
    )

    # Business Contact Information
    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
        first_name="Stuart",
        last_name="Stuart",
        phone_number="6574567813",
        email="svc_email_bt@corpdev.visa.com"
    )

    # Business Information
    business_information = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=address.__dict__,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=business_contact.__dict__,
        merchant_category_code="5999"
    )

    # Assigning business information to organization information
    organization_information.business_information = business_information.__dict__

    # Assigning organization information to request object
    req_obj.organization_information = organization_information.__dict__


    # Configurations
    configurations = CommerceSolutionsProductsBinLookupConfigurationInformationConfigurations(
        is_payout_options_enabled=False,
        is_account_prefix_enabled=True
    )

    # Configuration Information
    configuration_information = CommerceSolutionsProductsBinLookupConfigurationInformation(
        configurations=configurations.__dict__
    )

    # Bin Lookup
    bin_lookup = CommerceSolutionsProductsBinLookup(
        configuration_information=configuration_information.__dict__
    )

    # Commerce Solutions Product
    commerce_solutions = CommerceSolutionsProducts(
        bin_lookup=bin_lookup.__dict__
    )

    # Selected Products
    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
        payments=PaymentsProducts().__dict__,
        risk=RiskProducts().__dict__,
        commerce_solutions=commerce_solutions.__dict__,
        value_added_services=ValueAddedServicesProducts().__dict__
    )

    # Product Information
    product_information = Boardingv1registrationsProductInformation(
        selected_products=selected_products.__dict__
    )

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
