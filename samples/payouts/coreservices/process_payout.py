from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def process_a_payout():
    try:

        request = OctCreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "33557799"
        request.client_reference_information = client_reference.__dict__

        sender_info = V2payoutsSenderInformation()
        account_info = V2payoutsSenderInformationAccount()
        sender_info.reference_number = "1234567890"
        sender_info.address1 = "900 Metro Center Blvd.900"
        sender_info.country_code = "US"
        sender_info.locality = "Foster City"
        sender_info.name = "Thomas Jefferson"
        sender_info.administrative_area = "CA"
        account_info.funds_source = "05"
        account_info.number = "1234567890123456789012345678901234"
        sender_info.account = account_info.__dict__
        request.sender_information = sender_info.__dict__

        processing_info = V2payoutsProcessingInformation()
        processing_info.commerce_indicator = "internet"
        processing_info.business_application_id = "FD"
        processing_info.network_routing_order = "ECG"

        payouts_details = V2payoutsProcessingInformationPayoutsOptions()
        payouts_details.retrieval_reference_number = "123456789012"
        payouts_details.acquirer_bin = "567890124"
        processing_info.reconciliation_id = "1087488702VIAQNSPQ"
        processing_info.payouts_options = payouts_details.__dict__
        request.processing_information = processing_info.__dict__

        order_information = V2payoutsOrderInformation()
        amount_details = V2payoutsOrderInformationAmountDetails()
        amount_details.total_amount = "100.00"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        merchant_details = V2payoutsMerchantInformation()
        merchant_details.category_code = 123
        merchant_description = V2payoutsMerchantInformationMerchantDescriptor()
        merchant_description.country = "US"
        merchant_description.postal_code = "94440"
        merchant_description.locality = "FC"
        merchant_description.name = "Thomas"
        merchant_description.administrative_area = "CA"
        merchant_details.merchant_descriptor = merchant_description.__dict__
        request.merchant_information = merchant_details.__dict__

        payment_info = V2payoutsPaymentInformation()
        card_details = V2payoutsPaymentInformationCard()
        card_details.expiration_year = "2025"
        card_details.number = "4111111111111111"
        card_details.expiration_month = "12"
        card_details.type = "001"
        card_details.source_account_type = "CH"
        payment_info.card = card_details.__dict__
        request.payment_information = payment_info.__dict__

        recepient_info = V2payoutsRecipientInformation()
        recepient_info.first_name = "John"
        recepient_info.last_name = "Doe"
        recepient_info.address1 = "Paseo Padre Boulevard"
        recepient_info.locality = "Foster City"
        recepient_info.administrative_area = "CA"
        recepient_info.postal_code = "94400"
        recepient_info.phone_number = "6504320556"
        recepient_info.country = "US"
        recepient_info.date_of_birth = "19801009"
        request.recipient_information = recepient_info.__dict__

        message_body = json.dumps(request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        default_api_object = DefaultApi(details_dict1)
        return_data, status, body=default_api_object.oct_create_payment(message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    process_a_payout()
