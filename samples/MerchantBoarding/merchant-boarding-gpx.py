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

def merchant_boarding_gpx():

    
    req_obj = PostRegistrationBody()

    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address={
            "country": "US",
            "address1": "123456 SandMarket",
            "locality": "ORMOND BEACH",
            "administrative_area": "FL",
            "postal_code": "32176"
        },
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact={
            "first_name": "Stuart",
            "last_name": "Stuart",
            "phone_number": "6574567813",
            "email": "svc_email_bt@corpdev.visa.com"
        },
        merchant_category_code="5999"
    )

    organization_info.business_information = business_info.__dict__
    req_obj.organization_information = organization_info.__dict__

    # Product Information
    product_information = Boardingv1registrationsProductInformation()
    selected_products = Boardingv1registrationsProductInformationSelectedProducts()

    # Payments Products
    payments = PaymentsProducts()
    card_processing = PaymentsProductsCardProcessing()
    subscription_information = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features={
            "cardNotPresent": {"enabled": True},
            "cardPresent": {"enabled": True}
        }
    )
    card_processing.subscription_information = subscription_information.__dict__

    # Configuration Information
    configuration_information = PaymentsProductsCardProcessingConfigurationInformation()
    common = CardProcessingConfigCommon(
        merchant_category_code="1799",
        default_auth_type_code="FINAL",
        food_and_consumer_service_id="1456",
        master_card_assigned_id="4567",
        sic_code="1345",
        enable_partial_auth=False,
        allow_captures_greater_than_authorizations=False,
        enable_duplicate_merchant_reference_number_blocking=False,
        credit_card_refund_limit_percent="2",
        business_center_credit_card_refund_limit_percent="3",
        processors={
            "gpx": {
                "acquirer": {
                    "country_code": "840_usa",
                    "file_destination_bin": "123456",
                    "interbank_card_association_id": "1256",
                    "institution_id": "113366",
                    "discover_institution_id": "1567"
                },
                "currencies": {
                    "AED": {
                        "enabled": True,
                        "enabled_card_present": False,
                        "enabled_card_not_present": True,
                        "terminal_id": "",
                        "service_enablement_number": ""
                    }
                },
                "payment_types": {
                    "MASTERCARD": {"enabled": True},
                    "DISCOVER": {"enabled": True},
                    "JCB": {"enabled": True},
                    "VISA": {"enabled": True},
                    "DINERS_CLUB": {"enabled": True},
                    "PIN_DEBIT": {"enabled": True}
                },
                "allow_multiple_bills": True,
                "batch_group": "gpx",
                "business_application_id": "AA",
                "enhanced_data": "disabled",
                "fire_safety_indicator": False,
                "aba_number": "1122445566778",
                "merchant_verification_value": "234",
                "quasi_cash": False,
                "merchant_id": "112233",
                "terminal_id": "112244"
            }
        }
    )
    configuration_information.configurations = {"common": common.__dict__}
    configuration_information.template_id = str(uuid.UUID("D2A7C000-5FCA-493A-AD21-469744A19EEA"))
    card_processing.configuration_information = configuration_information.__dict__

    payments.card_processing = card_processing.__dict__
    payments.virtual_terminal = {
        "subscription_information": {"enabled": True},
        "configuration_information": {"template_id": str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))}
    }

    payments.customer_invoicing = {"subscription_information": {"enabled": True}}
    selected_products.payments = payments.__dict__

    risk = RiskProducts()
    selected_products.risk = risk.__dict__

    commerce_solutions = CommerceSolutionsProducts()
    commerce_solutions.token_management = {
        "subscription_information": {"enabled": True},
        "configuration_information": {"template_id": str(uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA"))}
    }
    selected_products.commerce_solutions = commerce_solutions.__dict__

    value_added_services = ValueAddedServicesProducts()
    value_added_services.transaction_search = {"subscription_information": {"enabled": True}}
    value_added_services.reporting = {"subscription_information": {"enabled": True}}
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
    merchant_boarding_gpx()
