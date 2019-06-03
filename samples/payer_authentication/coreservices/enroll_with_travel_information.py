from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def enrol_with_travel_information():
    try:
        # Setting the json message body
        request = CheckPayerAuthEnrollmentRequest()
        client_reference = Riskv1authenticationsClientReferenceInformation("cybs_test")
        request.client_reference_information = client_reference.__dict__

        order_information = Riskv1authenticationsOrderInformation()
		
        bill_to = Riskv1authenticationsOrderInformationBillTo("1 Market St","Address 2","CA","US","san francisco","James","Doe","4158880000","test@cybs.com","94105")

        amount_details = Riskv1decisionsOrderInformationAmountDetails("USD")
        amount_details.total_amount = "10.99"

        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = Riskv1authenticationsPaymentInformation()
        card = Riskv1authenticationsPaymentInformationCard("002","12","2025","5200340000000015")
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__

        request.order_information = order_information.__dict__

        travel_information = Riskv1authenticationsTravelInformation()

        legs = []
        leg0 = Riskv1authenticationsTravelInformationLegs()
        leg0.carrier_code = "UA"
        leg0.departure_date = "2019-01-01"
        leg0.origination = "LAX"
        leg0.destination = "DEF"

        leg1 = Riskv1authenticationsTravelInformationLegs()
        leg1.carrier_code = "AS"
        leg1.departure_date = "2019-02-21"
        leg1.origination = "ECF"
        leg1.destination = "RES"
		
        legs.append(leg0.__dict__)
        legs.append(leg1.__dict__)
        travel_information.legs = legs
        travel_information.number_of_passengers = "2"

        passengers = []
        passenger0 = Riskv1authenticationsTravelInformationPassengers()
        passenger0.first_name = "Raj"
        passenger0.last_name = "Charles"

        passenger1 = Riskv1authenticationsTravelInformationPassengers()
        passenger1.first_name = "Potter"
        passenger1.last_name = "Suhember"

        passengers.append(passenger0.__dict__)
        passengers.append(passenger1.__dict__)
        travel_information.passengers = passengers

        request.travel_information = travel_information.__dict__

        buyer_information = Riskv1authenticationsBuyerInformation()
        buyer_information.mobile_phone = "1245789632"

        request.buyer_information = buyer_information.__dict__

        consumer_authentication_information = Riskv1authenticationsConsumerAuthenticationInformation(mcc = '', reference_id = '', transaction_mode = 'MOTO')

        request.consumer_authentication_information = consumer_authentication_information.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        dm_obj = PayerAuthenticationApi(details_dict1)
        return_data, status, body = dm_obj.check_payer_auth_enrollment(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling PayerAuthenticationApi->enrol_with_travel_information: %s\n" % e)


if __name__ == "__main__":
    enrol_with_travel_information()

