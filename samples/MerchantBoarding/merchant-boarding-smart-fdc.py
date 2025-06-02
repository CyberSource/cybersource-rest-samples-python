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

def merchant_boarding_smart_fdc():

        
    req_obj = PostRegistrationBody()

    organization_info = Boardingv1registrationsOrganizationInformation(
        parent_organization_id="apitester00",
        type="MERCHANT",
        configurable=True
    )

    business_address = Boardingv1registrationsOrganizationInformationBusinessInformationAddress(
        country="US",
        address1="123456 SandMarket",
        locality="ORMOND BEACH",
        administrative_area="FL",
        postal_code="32176"
    ).__dict__

    business_contact = Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(
        first_name="Stuart",
        last_name="Stuart",
        phone_number="6574567813",
        email="svc_email_bt@corpdev.visa.com"
    ).__dict__

    business_info = Boardingv1registrationsOrganizationInformationBusinessInformation(
        name="StuartWickedFastEatz",
        address=business_address,
        website_url="https://www.StuartWickedEats.com",
        phone_number="6574567813",
        business_contact=business_contact,
        merchant_category_code="5999"
    ).__dict__

    organization_info.business_information = business_info
    req_obj.organization_information = organization_info.__dict__

    subscription_features = {
        "cardNotPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__,
        "cardPresent": PaymentsProductsCardProcessingSubscriptionInformationFeatures(enabled=True).__dict__
    }

    subscription_info = PaymentsProductsCardProcessingSubscriptionInformation(
        enabled=True,
        features=subscription_features
    ).__dict__

    payment_types = {
        "MASTERCARD": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "DISCOVER": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "JCB": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "VISA": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "DINERS_CLUB": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__,
        "AMERICAN_EXPRESS": CardProcessingConfigCommonPaymentTypes(enabled=True).__dict__
    }

    processors = {
        "smartfdc": CardProcessingConfigCommonProcessors(
            acquirer=CardProcessingConfigCommonAcquirer().__dict__,
            payment_types=payment_types,
            batch_group="smartfdc_00",
            merchant_id="00001234567",
            terminal_id="00007654321"
        ).__dict__
    }

    common_config = CardProcessingConfigCommon(
        merchant_category_code="1799",
        default_auth_type_code="FINAL",
        enable_partial_auth=True,
        processors=processors
    ).__dict__

    configurations = CardProcessingConfig(common=common_config).__dict__

    configuration_info = PaymentsProductsCardProcessingConfigurationInformation(
        configurations=configurations,
        template_id=str(uuid.UUID("3173DA78-A71E-405B-B79C-928C1A9C6AB2"))
    ).__dict__

    card_processing = PaymentsProductsCardProcessing(
        subscription_information=subscription_info,
        configuration_information=configuration_info
    ).__dict__

    virtual_terminal_config = PaymentsProductsVirtualTerminalConfigurationInformation(
        template_id=str(uuid.UUID("9FA1BB94-5119-48D3-B2E5-A81FD3C657B5"))
    ).__dict__

    virtual_terminal = PaymentsProductsVirtualTerminal(
        configuration_information=virtual_terminal_config
    ).__dict__

    customer_invoicing = PaymentsProductsTax(
    ).__dict__

    payments = PaymentsProducts(
        card_processing=card_processing,
        virtual_terminal=virtual_terminal,
        customer_invoicing=customer_invoicing
    ).__dict__

    token_management_config = CommerceSolutionsProductsTokenManagementConfigurationInformation(
        template_id=str(uuid.UUID("D62BEE20-DCFD-4AA2-8723-BA3725958ABA"))
    ).__dict__

    token_management = CommerceSolutionsProductsTokenManagement(
        configuration_information=token_management_config
    ).__dict__

    commerce_solutions = CommerceSolutionsProducts(token_management=token_management).__dict__

    transaction_search = PaymentsProductsTax(
    ).__dict__

    reporting = PaymentsProductsTax(
    ).__dict__

    value_added_services = ValueAddedServicesProducts(
        transaction_search=transaction_search,
        reporting=reporting
    ).__dict__

    selected_products = Boardingv1registrationsProductInformationSelectedProducts(
        payments=payments,
        risk=RiskProducts().__dict__,
        commerce_solutions=commerce_solutions,
        value_added_services=value_added_services
    ).__dict__

    product_information = Boardingv1registrationsProductInformation(
        selected_products=selected_products
    ).__dict__

    req_obj.product_information = product_information
    
    
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
    merchant_boarding_smart_fdc()
