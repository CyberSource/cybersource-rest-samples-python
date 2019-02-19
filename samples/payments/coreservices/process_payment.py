from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()



def process_a_payment(flag):

    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        request = CreatePaymentRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_payment"
        request.client_reference_information = client_reference.__dict__

        processing_info = Ptsv2paymentsProcessingInformation()
        if flag:
            processing_info.capture = "true"

        request.processing_information = processing_info.__dict__

        aggregator_info = Ptsv2paymentsAggregatorInformation()
        sub_merchant = Ptsv2paymentsAggregatorInformationSubMerchant()
        sub_merchant.card_acceptor_id = "1234567890"
        sub_merchant.country = "US"
        sub_merchant.phone_number = "650-432-0000"
        sub_merchant.address1 = "900 Metro Center"
        sub_merchant.postal_code = "94404-2775"
        sub_merchant.locality = "Foster City"
        sub_merchant.name = "Visa Inc"
        sub_merchant.administrative_area = "CA"
        sub_merchant.region = "PEN"
        sub_merchant.email = "test@cybs.com"
        aggregator_info.sub_merchant = sub_merchant.__dict__
        aggregator_info.name = "V-Internatio"
        aggregator_info.aggregator_id = "123456789"
        request.aggregator_information = aggregator_info.__dict__

        order_information = Ptsv2paymentsOrderInformation()
        bill_to = Ptsv2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "Doe"
        bill_to.address2 = "1 Market St"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.first_name = "John"
        bill_to.phone_number = "999999999"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"

        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = Ptsv2paymentsPaymentInformation()
        card = Ptsv2paymentsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "5555555555554444"
        card.security_code = "123"
        card.expiration_month = "12"
        card.type = "002"
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        payment_obj = PaymentsApi(details_dict1)
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = payment_obj.create_payment(message_body)
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

        return json.loads(response_data.data)
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)
    finally:

        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    process_a_payment(False)
