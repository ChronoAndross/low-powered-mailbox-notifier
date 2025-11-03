from twilio.twilio import Twilio
import time

def main():
    # keys.txt should be a text file that is created locally and contains the twilio account sid, access key, a from number, and a to number.
    keys = open("keys.txt").readline().split(",")
    account_sid = keys[0]
    auth_token = keys[1]
    phone_number_from = keys[2]
    phone_number_to = keys[3]
    twilio_api = Twilio(account_sid, auth_token)
    while 1:
        # this doesn't stop for now
        time.sleep(5)
        twilio_api.send_text_message(phone_number_from, phone_number_to, "this is a sample message!!!")

if __name__ == "__main__":    
    main()