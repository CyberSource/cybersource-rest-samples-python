from lib.sampleapiclient.model.AggregatorInformation import *
from lib.sampleapiclient.model.AmountDetails import *
from lib.sampleapiclient.model.BillTo import *
from lib.sampleapiclient.model.Card import *
from lib.sampleapiclient.model.ClientReferenceInformation import *
from lib.sampleapiclient.model.OrderInformation import *
from lib.sampleapiclient.model.PaymentInformation import *
from lib.sampleapiclient.model.Payments import *
from lib.sampleapiclient.model.ProcessingInformation import *
from lib.sampleapiclient.model.SubMerchant import *
from authenticationsdk.payloaddigest.PayLoadDigest import *
import authenticationsdk.util.ExceptionAuth
from authenticationsdk.core.ExceptionHandling import *
from authenticationsdk.util.GlobalLabelParameters import *
import json


def json_file_data(path, mconfig):
    logger = mconfig.log
    try:
        if path == "" or path is None:
            raise ApiException(0, GlobalLabelParameters.REQUEST_JSON_EMPTY)

        else:
            digest_obj = DigestAndPayload()
            return digest_obj.string_payload_generation(path)
    except IOError as e:

        authenticationsdk.util.ExceptionAuth.log_exception(logger,
                                                           GlobalLabelParameters.REQUEST_JSON_ERROR + str(e.filename),
                                                           mconfig)


# This method sets the data to the properties in model classes if request json is not provided
def sample_payment_data():
    client_reference_information = ClientReferenceInformation()
    client_reference_information.set_code("TC50171_3")
    processing_information = ProcessingInformation()
    processing_information.set_commerce_indicator("internet")
    sub_merchant = SubMerchant()
    sub_merchant.set_name("Visa Inc")
    sub_merchant.set_address1("900 Metro Center")
    sub_merchant.set_administrative_area("CA")
    sub_merchant.set_card_acceptor_id("1234567890")
    sub_merchant.set_country("US")
    sub_merchant.set_email("test@cybs.com")
    sub_merchant.set_locality("Foster Cit")
    sub_merchant.set_phone_number("650-432-0000")
    sub_merchant.set_postal_code("94404-2775")
    sub_merchant.set_region("PEN")
    aggregator_information = AggregatorInformation()

    aggregator_information.set_submerchant(sub_merchant.__dict__)
    aggregator_information.set_name("V-Internatio")
    aggregator_information.set_aggregator_id("123456789")
    bill_to = BillTo()
    bill_to.set_postal_code("48104-2201")
    bill_to.set_phone_number("999999999")
    bill_to.set_locality("Ann Arbor")
    bill_to.set_email("test@cybs.com")
    bill_to.set_country("US")
    bill_to.set_administrative_area("MI")
    bill_to.set_address1("201 S. Division St.")
    bill_to.set_address2("Address 2")
    bill_to.set_building_number("123")
    bill_to.set_company("Visa")
    bill_to.set_district("MI")
    bill_to.set_first_name("RTS")
    bill_to.set_last_name("VDP")
    amount_details = AmountDetails()
    amount_details.set_currency("USD")
    amount_details.set_total_amount("102.21")
    order_information = OrderInformation()
    order_information.set_amount_details(amount_details.__dict__)
    order_information.set_bill_to(bill_to.__dict__)
    card = Card()
    card.set_espiration_year("2031")
    card.set_expiration_month("12")
    card.set_number("5555555555554444")
    card.set_security_code("123")
    card.set_type("002")
    payment_information = PaymentInformation()
    payment_information.set_card(card.__dict__)
    payments = Payments()
    payments.set_aggregator_information(aggregator_information.__dict__)
    payments.set_client_reference_information(client_reference_information.__dict__)
    payments.set_order_information(order_information.__dict__)
    payments.set_payment_information(payment_information.__dict__)
    payments.set_processing_information(processing_information.__dict__)

    return json.dumps(payments.__dict__)
