from CyberSource import *
import samples.flex.keygeneration_noenc
import json

def tokenize_card():
    try:
        tokenize_card = TokenizeRequest()
        card_info = Paymentsflexv1tokensCardInfo()
        api_response = samples.flex.keygeneration_noenc.keygeneration_noenc()
        tokenize_card.key_id = api_response.key_id

        card_info.card_expiration_year = "2031"
        card_info.card_number = "5555555555554444"
        card_info.card_type = "002"
        card_info.card_expiration_month = "03"
        tokenize_card.card_info = card_info.__dict__

        message_body = json.dumps(tokenize_card.__dict__)

        tokenize_obj = TokenizationApi()
        return_data, status, body = tokenize_obj.tokenize(tokenize_request=message_body)
        print(status)
        print(body)
    except Exception as e:
        print(e)






if __name__ == "__main__":
    tokenize_card()
