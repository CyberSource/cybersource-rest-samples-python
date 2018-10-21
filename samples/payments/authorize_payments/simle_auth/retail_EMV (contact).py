from cybersource_rest_client_python import *
import json


def retail_emv_contact():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_16"
        request.client_reference_information = client_reference.__dict__
    
        point_of_sale = V2paymentsPointOfSaleInformation()
        point_of_sale.card_present = "Y"
        point_of_sale.cat_level = 1
        point_of_sale.endlessAisleTransactionIndicator = "true"
        point_of_sale.entry_mode = "contact"
        point_of_sale.terminal_capability = 1
    
        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "retail"
        processing_info.payment_solution = "011"
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
        amount_details.total_amount = "115.0"
        amount_details.currency = "USD"
        order_information.bill_to = bill_to.__dict__
        order_information.amount_details = amount_details.__dict__
    
        payment_info = V2paymentsPaymentInformation()
        fluid_data = V2paymentsPaymentInformationFluidData()
        fluid_data.descriptor = "EMV.PAYMENT.AnywhereCommerce.Walker"
        fluid_data.value = "ewogICJkYXRhIiA6ICJOZmNwRURiK1dLdzBnQkpsaTRcL1hlWm1ITzdUSng0bnRoMnc2Mk9ITVJQK3hCRlFPdFE0WWpRcnY0RmFkOHh6VExqT2VFQm5iNHFzeGZMYTNyNXcxVEdXblFGQnNzMWtPYnA0XC95alNtVE1JSGVjbGc5OFROaEhNb0VRcjJkRkFqYVpBTFAxSlBsdVhKSVwvbTZKSmVwNGh3VHRWZE16Z2laSUhnaWFCYzNXZVd1ZnYzc1l0cGRaZDZYZENEUFdLeXFkYjBJdUtkdkpBPT0iLAogICJzaWduYXR1cmUiIDogIkFxck1pKzc0cm1GeVBKVE9HN3NuN2p5K1YxTlpBZUNJVE56TW01N1B5cmc9IiwKICAic2lnbmF0dXJlQWxnSW5mbyIgOiAiSE1BQ3dpdGhTSEEyNTYiLAogICJoZWFkZXIiIDogewogICAgInRyYW5zYWN0aW9uSWQiIDogIjE1MTU2MjI2NjIuMTcyMjIwIiwKICAgICJwdWJsaWNLZXlIYXNoIiA6ICJcLzdmdldqRVhMazJPRWpcL3Z5bk1jeEZvMmRWSTlpRXVoT2Nab0tHQnpGTmM9IiwKICAgICJhcHBsaWNhdGlvbkRhdGEiIDogIkN5YmVyU291cmNlLlZNcG9zS2l0IiwKICAgICJlcGhlbWVyYWxQdWJsaWNLZXkiIDogIk1Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRW1JN0tScnRNN2NNelk5Zmw2UWt2NEQzdE9jU0NYR1hoOFwvK2R4K2s5c1Zrbk05UFQrOXRqMzk2YWF6QjRcL0hYaWlLRW9DXC9jUzdoSzF6UFk3MVwvN0pUUT09IgogIH0sCiAgInZlcnNpb24iIDogIjEuMCIKfQ=="
        payment_info.fluid_data = fluid_data.__dict__
        request.payment_information = payment_info.__dict__
        request.order_information = order_information.__dict__
        request.point_of_sale_information = point_of_sale.__dict__
        
        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    retail_emv_contact()
