from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def authorization_for_incremental_authorization_flow():
    processingInformationCapture = False
    processingInformationIndustryDataType = "lodging"
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        industry_data_type = processingInformationIndustryDataType
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2021"
    paymentInformationCardType = "001"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        type = paymentInformationCardType
    )

    paymentInformationTokenizedCardSecurityCode = "123"
    paymentInformationTokenizedCard = Ptsv2paymentsPaymentInformationTokenizedCard(
        security_code = paymentInformationTokenizedCardSecurityCode
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__,
        tokenized_card = paymentInformationTokenizedCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "20"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Smith"
    orderInformationBillToAddress1 = "201 S. Division St."
    orderInformationBillToAddress2 = "Suite 500"
    orderInformationBillToLocality = "Ann Arbor"
    orderInformationBillToAdministrativeArea = "MI"
    orderInformationBillToPostalCode = "12345"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "null@cybersource.com"
    orderInformationBillToPhoneNumber = "514-670-8700"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformationShipToFirstName = "Olivia"
    orderInformationShipToLastName = "White"
    orderInformationShipToAddress1 = "1295 Charleston Rd"
    orderInformationShipToAddress2 = "Cube 2386"
    orderInformationShipToLocality = "Mountain View"
    orderInformationShipToAdministrativeArea = "CA"
    orderInformationShipToPostalCode = "94041"
    orderInformationShipToCountry = "AE"
    orderInformationShipToPhoneNumber = "650-965-6000"
    orderInformationShipTo = Ptsv2paymentsOrderInformationShipTo(
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName,
        address1 = orderInformationShipToAddress1,
        address2 = orderInformationShipToAddress2,
        locality = orderInformationShipToLocality,
        administrative_area = orderInformationShipToAdministrativeArea,
        postal_code = orderInformationShipToPostalCode,
        country = orderInformationShipToCountry,
        phone_number = orderInformationShipToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__
    )

    merchantInformationMerchantDescriptorContact = "965-6000"
    merchantInformationMerchantDescriptor = Ptsv2paymentsMerchantInformationMerchantDescriptor(
        contact = merchantInformationMerchantDescriptorContact
    )

    merchantInformation = Ptsv2paymentsMerchantInformation(
        merchant_descriptor = merchantInformationMerchantDescriptor.__dict__
    )

    consumerAuthenticationInformationCavv = "ABCDEabcde12345678900987654321abcdeABCDE"
    consumerAuthenticationInformationXid = "12345678909876543210ABCDEabcdeABCDEF1234"
    consumerAuthenticationInformation = Ptsv2paymentsConsumerAuthenticationInformation(
        cavv = consumerAuthenticationInformationCavv,
        xid = consumerAuthenticationInformationXid
    )

    installmentInformationAmount = "1200"
    installmentInformationFrequency = "W"
    installmentInformationSequence = 34
    installmentInformationTotalAmount = "2000"
    installmentInformationTotalCount = 12
    installmentInformation = Ptsv2paymentsInstallmentInformation(
        amount = installmentInformationAmount,
        frequency = installmentInformationFrequency,
        sequence = installmentInformationSequence,
        total_amount = installmentInformationTotalAmount,
        total_count = installmentInformationTotalCount
    )

    travelInformationDuration = "3"
    travelInformationLodgingCheckInDate = "110619"
    travelInformationLodgingCheckOutDate = "110919"

    travelInformationLodgingRoom = []
    travelInformationLodgingRoom1 = Ptsv2paymentsTravelInformationLodgingRoom(
        daily_rate = "1.50",
        number_of_nights = 5
    )

    travelInformationLodgingRoom.append(travelInformationLodgingRoom1.__dict__)

    travelInformationLodgingRoom2 = Ptsv2paymentsTravelInformationLodgingRoom(
        daily_rate = "11.50",
        number_of_nights = 5
    )

    travelInformationLodgingRoom.append(travelInformationLodgingRoom2.__dict__)

    travelInformationLodgingSmokingPreference = "Y"
    travelInformationLodgingNumberOfRooms = 1
    travelInformationLodgingNumberOfGuests = 3
    travelInformationLodgingRoomBedType = "king"
    travelInformationLodgingRoomTaxType = "tourist"
    travelInformationLodgingRoomRateType = "sr citizen"
    travelInformationLodgingGuestName = "Tulasi"
    travelInformationLodgingCustomerServicePhoneNumber = "+13304026334"
    travelInformationLodgingCorporateClientCode = "HDGGASJDGSUY"
    travelInformationLodgingAdditionalDiscountAmount = "99.123456781"
    travelInformationLodgingRoomLocation = "seaview"
    travelInformationLodgingSpecialProgramCode = "2"
    travelInformationLodgingTotalTaxAmount = "99.12345"
    travelInformationLodgingPrepaidCost = "9999.99"
    travelInformationLodgingFoodAndBeverageCost = "9999.99"
    travelInformationLodgingRoomTaxAmount = "9999.99"
    travelInformationLodgingAdjustmentAmount = "9999.99"
    travelInformationLodgingPhoneCost = "9999.99"
    travelInformationLodgingRestaurantCost = "9999.99"
    travelInformationLodgingRoomServiceCost = "9999.99"
    travelInformationLodgingMiniBarCost = "9999.99"
    travelInformationLodgingLaundryCost = "9999.99"
    travelInformationLodgingMiscellaneousCost = "9999.99"
    travelInformationLodgingGiftShopCost = "9999.99"
    travelInformationLodgingMovieCost = "9999.99"
    travelInformationLodgingHealthClubCost = "9999.99"
    travelInformationLodgingValetParkingCost = "9999.99"
    travelInformationLodgingCashDisbursementCost = "9999.99"
    travelInformationLodgingNonRoomCost = "9999.99"
    travelInformationLodgingBusinessCenterCost = "9999.99"
    travelInformationLodgingLoungeBarCost = "9999.99"
    travelInformationLodgingTransportationCost = "9999.99"
    travelInformationLodgingGratuityAmount = "9999.99"
    travelInformationLodgingConferenceRoomCost = "9999.99"
    travelInformationLodgingAudioVisualCost = "9999.99"
    travelInformationLodgingNonRoomTaxAmount = "9999.99"
    travelInformationLodgingEarlyCheckOutCost = "9999.99"
    travelInformationLodgingInternetAccessCost = "9999.99"
    travelInformationLodging = Ptsv2paymentsTravelInformationLodging(
        check_in_date = travelInformationLodgingCheckInDate,
        check_out_date = travelInformationLodgingCheckOutDate,
        room = travelInformationLodgingRoom,
        smoking_preference = travelInformationLodgingSmokingPreference,
        number_of_rooms = travelInformationLodgingNumberOfRooms,
        number_of_guests = travelInformationLodgingNumberOfGuests,
        room_bed_type = travelInformationLodgingRoomBedType,
        room_tax_type = travelInformationLodgingRoomTaxType,
        room_rate_type = travelInformationLodgingRoomRateType,
        guest_name = travelInformationLodgingGuestName,
        customer_service_phone_number = travelInformationLodgingCustomerServicePhoneNumber,
        corporate_client_code = travelInformationLodgingCorporateClientCode,
        additional_discount_amount = travelInformationLodgingAdditionalDiscountAmount,
        room_location = travelInformationLodgingRoomLocation,
        special_program_code = travelInformationLodgingSpecialProgramCode,
        total_tax_amount = travelInformationLodgingTotalTaxAmount,
        prepaid_cost = travelInformationLodgingPrepaidCost,
        food_and_beverage_cost = travelInformationLodgingFoodAndBeverageCost,
        room_tax_amount = travelInformationLodgingRoomTaxAmount,
        adjustment_amount = travelInformationLodgingAdjustmentAmount,
        phone_cost = travelInformationLodgingPhoneCost,
        restaurant_cost = travelInformationLodgingRestaurantCost,
        room_service_cost = travelInformationLodgingRoomServiceCost,
        mini_bar_cost = travelInformationLodgingMiniBarCost,
        laundry_cost = travelInformationLodgingLaundryCost,
        miscellaneous_cost = travelInformationLodgingMiscellaneousCost,
        gift_shop_cost = travelInformationLodgingGiftShopCost,
        movie_cost = travelInformationLodgingMovieCost,
        health_club_cost = travelInformationLodgingHealthClubCost,
        valet_parking_cost = travelInformationLodgingValetParkingCost,
        cash_disbursement_cost = travelInformationLodgingCashDisbursementCost,
        non_room_cost = travelInformationLodgingNonRoomCost,
        business_center_cost = travelInformationLodgingBusinessCenterCost,
        lounge_bar_cost = travelInformationLodgingLoungeBarCost,
        transportation_cost = travelInformationLodgingTransportationCost,
        gratuity_amount = travelInformationLodgingGratuityAmount,
        conference_room_cost = travelInformationLodgingConferenceRoomCost,
        audio_visual_cost = travelInformationLodgingAudioVisualCost,
        non_room_tax_amount = travelInformationLodgingNonRoomTaxAmount,
        early_check_out_cost = travelInformationLodgingEarlyCheckOutCost,
        internet_access_cost = travelInformationLodgingInternetAccessCost
    )

    travelInformation = Ptsv2paymentsTravelInformation(
        duration = travelInformationDuration,
        lodging = travelInformationLodging.__dict__
    )

    promotionInformationAdditionalCode = "999999.99"
    promotionInformation = Ptsv2paymentsPromotionInformation(
        additional_code = promotionInformationAdditionalCode
    )

    requestObj = CreatePaymentRequest(
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__,
        consumer_authentication_information = consumerAuthenticationInformation.__dict__,
        installment_information = installmentInformation.__dict__,
        travel_information = travelInformation.__dict__,
        promotion_information = promotionInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_alternative_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    authorization_for_incremental_authorization_flow()
