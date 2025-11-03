import requests

class Twilio:

    def __init__(account_sid: str, auth_token: str):
        self.account_sid = account_sid
        self.auth_token = auth_token

    def send_text_message(phone_number_from:str, phone_number_to: str, body: str):
        payload = {
            "From": phone_number_from,
            "To": phone_number_to,
            "Body": body
        }
        try:
            response = requests.post(
                f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json",
                data=payload,
                auth=(self.account_sid, self.api_key)
            )
            print(f"response json: {response.json()}")
        except Exception as e:
            print(f"response failed, {e}")