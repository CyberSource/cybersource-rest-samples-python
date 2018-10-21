from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.tms.coreservices.create_payment_instrument

def retrieve_payment_instrument():
    try:
        api_payment_response=cybersource_rest_samples_python.samples.tms.coreservices.create_payment_instrument.create_payment_instrument()
        payment_instruments = PaymentInstrumentApi()
        return payment_instruments.paymentinstruments_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_payment_instrument()
