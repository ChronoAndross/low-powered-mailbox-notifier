from twilio.twilio import Twilio
from sensors.sensors import Sensors
import time

def main():
    # instantiate sensors
    sensors_api = Sensors(31, 33, 37)

    # keys.txt should be a text file that is created locally and contains the twilio account sid, access key, a from number, and a to number.
    keys = open("keys.txt").readline().split(",")
    account_sid = keys[0]
    auth_token = keys[1]
    phone_number_from = keys[2]
    phone_number_to = keys[3]
    twilio_api = Twilio(account_sid, auth_token)
    while 1:
        # this doesn't stop for now
        print("sleep for 0.5 seconds...")
        time.sleep(0.5)
        if sensors_api.detect():
            print("detection found! sending text message and email via twilio!!")
            twilio_api.send_text_message(phone_number_from, phone_number_to, "this is a sample message!!!")
        else:
            print("didn't detect anything...")

if __name__ == "__main__":    
    main()
