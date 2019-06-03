from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def validate_authentication_results():
    try:
        # Setting the json message body
        request = Request()
        client_reference = Riskv1authenticationsClientReferenceInformation("pavalidatecheck")
        request.client_reference_information = client_reference.__dict__

        order_information = Riskv1authenticationresultsOrderInformation()
		
        amount_details = Riskv1decisionsOrderInformationAmountDetails("USD")
        amount_details.total_amount = "200.00"

        line_items = Riskv1authenticationresultsOrderInformationLineItems("10")
        line_items.quantity = 2
        line_items.tax_amount = "32.40"

        order_information.line_items = line_items.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = Riskv1authenticationresultsPaymentInformation()
        card = Riskv1authenticationresultsPaymentInformationCard("002","12","2025","5200000000000007")
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        request.order_information = order_information.__dict__

        consumer_authentication_information = Riskv1authenticationresultsConsumerAuthenticationInformation('PYffv9G3sa1e0CQr5fV0','eNqdmFmT4jgSgN+J4D90zD4yMz45PEFVhHzgA2zwjXnzhQ984Nvw61dAV1')

        request.consumer_authentication_information = consumer_authentication_information.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        dm_obj = PayerAuthenticationApi(details_dict1)
        return_data, status, body = dm_obj.risk_v1_authentication_results_post(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling PayerAuthenticationApi->validate_authentication_results: %s\n" % e)


if __name__ == "__main__":
    validate_authentication_results()

