from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.tms.coreservices.retrieve_payment_instrument



def remove_payment_instruments():
    try:
        api_payment_response=cybersource_rest_samples_python.samples.tms.coreservices.retrieve_payment_instrument.retrieve_payment_instrument()
        payment_instrument_obj = PaymentInstrumentApi()
        payment_instrument_obj.paymentinstruments_token_id_delete("93B32398-AD51-4CC2-A682-EA3E93614EB1", api_payment_response.id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    remove_payment_instruments()
