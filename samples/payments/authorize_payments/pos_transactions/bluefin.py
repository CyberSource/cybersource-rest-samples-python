from cybersource_rest_client_python import *
import json


def bluefin():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "demomerchant"
        request.client_reference_information = client_reference.__dict__

        point_of_sale = V2paymentsPointOfSaleInformation()
        point_of_sale.card_present = "Y"
        point_of_sale.cat_level = 1
        point_of_sale.entry_mode = "keyed"
        point_of_sale.terminal_capability = 2
        request.point_of_sale_information = point_of_sale.__dict__

        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "retail"
        request.processing_information = processing_info.__dict__

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
        amount_details.currency = "USD"
        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__

        payment_info = V2paymentsPaymentInformation()
        card = V2paymentsPaymentInformationCard()
        card.expiration_year = "2050"
        card.expiration_month = "12"
        fluid_data = V2paymentsPaymentInformationFluidData()
        fluid_data.descriptor = "Ymx1ZWZpbg=="
        fluid_data.value = "02d700801f3c20008383252a363031312a2a2a2a2a2a2a2a303030395e46444d53202020202020202020202020202020202020202020205e323231322a2a2a2a2a2a2a2a3f2a3b363031312a2a2a2a2a2a2a2a303030393d323231322a2a2a2a2a2a2a2a3f2a7a75ad15d25217290c54b3d9d1c3868602136c68d339d52d98423391f3e631511d548fff08b414feac9ff6c6dede8fb09bae870e4e32f6f462d6a75fa0a178c3bd18d0d3ade21bc7a0ea687a2eef64551751e502d97cb98dc53ea55162cdfa395431323439323830303762994901000001a000731a8003"
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
    bluefin()
