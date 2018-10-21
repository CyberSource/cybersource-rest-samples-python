from cybersource_rest_client_python import *
import json


def emv():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "123456"
        request.client_reference_information = client_reference.__dict__

        point_of_sale = V2paymentsPointOfSaleInformation()
        point_of_sale.card_present = "Y"
        point_of_sale.cat_level = 2
        point_of_sale_emv = V2paymentsPointOfSaleInformationEmv()
        point_of_sale_emv.fallback_condition = "swiped"
        point_of_sale_emv.fallback = "Y"
        point_of_sale.terminal_capability = 4
        point_of_sale.emv = point_of_sale_emv.__dict__
        request.point_of_sale_information = point_of_sale.__dict__

        order_information = V2paymentsOrderInformation()
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.last_name = "VDP"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.first_name = "RTS"
        bill_to.phone_number = "999999999"
        bill_to.email = "test@cybs.com"
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "100.00"
        amount_details.currency = "usd"
        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = V2paymentsPaymentInformation()
        card = V2paymentsPaymentInformationCard()
        card.expiration_year = "2031"
        card.number = "372425119311008"
        card.security_code = "123"
        card.expiration_month = "12"
        fluid_data = V2paymentsPaymentInformationFluidData()
        fluid_data.value = "%B373235387881007^SMITH/JOHN         ^31121019761100      00868000000?;373235387881007=31121019761186800000?"
        payment_info.card = card.__dict__
        payment_info.fluid_data = fluid_data.__dict__
        request.payment_information = payment_info.__dict__
        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    emv()
