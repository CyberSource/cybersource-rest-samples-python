from CyberSource import *
import samples.tms.coreservices.create_payment_instrument

def retrieve_payment_instrument():
    try:
        api_payment_response=samples.tms.coreservices.create_payment_instrument.create_payment_instrument()
        payment_instruments = PaymentInstrumentApi()
        return_data, status, body =payment_instruments.paymentinstruments_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_payment_instrument()
