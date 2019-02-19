from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def process_a_credit():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        request = CreateCreditRequest()
        client_reference = Ptsv2paymentsClientReferenceInformation()
        client_reference.code = "test_credits"
        request.client_reference_information = client_reference.__dict__

        order_information = Ptsv2paymentsOrderInformation()
        amount_details = Ptsv2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "200"
        amount_details.currency = "usd"
        bill_to = Ptsv2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "John"
        bill_to.last_name = "Doe"
        bill_to.address1 = "1 Market St"
        bill_to.phone_number = "9999999999"
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        order_information.amount_details = amount_details.__dict__
        order_information.bill_to = bill_to.__dict__

        payment_information = Ptsv2paymentsPaymentInformation()
        card_information = Ptsv2paymentsPaymentInformationCard()
        card_information.expiration_month = "03"
        card_information.expiration_year = "2031"
        card_information.type = "001"
        card_information.number = "4111111111111111"
        payment_information.card = card_information.__dict__
        request.order_information = order_information.__dict__
        request.payment_information = payment_information.__dict__
        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        credit_obj = CreditApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = credit_obj.create_credit(message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
        return json.loads(response_data.data)

    except Exception as e:
        print("\nException when calling CreditApi->create_credit: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    process_a_credit()
