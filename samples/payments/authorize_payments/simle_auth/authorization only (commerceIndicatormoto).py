from cybersource_rest_client_python import *
import json


def authorization_only_commerce_indicatormoto():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_9"
        request.client_reference_information = client_reference.__dict__

        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "moto"
        request.processing_information = processing_info.__dict__

        aggregator_info = V2paymentsAggregatorInformation()
        sub_merchant = V2paymentsAggregatorInformationSubMerchant()
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

        order_information = V2paymentsOrderInformation()
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "VDP"
        bill_to.address2 = "Address 2"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.first_name = "RTS"
        bill_to.phone_number = "999999999"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        bill_to.company = "Visa"
        bill_to.email = "test@cybs.com"

        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "109.00"
        amount_details.currency = "USD"
        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = V2paymentsPaymentInformation()
        card = V2paymentsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "5555555555554444"
        card.security_code = "123"
        card.expiration_month = "12"
        card.type = "002"
        payment_info.card = card.__dict__
        request.payment_information = payment_info.__dict__
        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    authorization_only_commerce_indicatormoto()
