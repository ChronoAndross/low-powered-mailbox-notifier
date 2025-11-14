from twilio.twilio import Twilio
from sensors.sensors import Sensors
import time
import sys
import signal

def _signal_handler():
    sys.exit(0)

def _low_powered_implementation(sensors_api: Sensors, twilio_api: Twilio, phone_number_from: str, phone_number_to: str):
    sensors_api.setup_event_callbacks(twilio_api.send_text_message, [phone_number_from, phone_number_to, "this is a sample message!!!"])
    signal.signal(signal.SIGINT, _signal_handler)
    print("pausing on main thread for low power")
    signal.pause()
    

def _high_powered_implementation(sensors_api: Sensors, twilio_api: Twilio, phone_number_from: str, phone_number_to: str):
    while 1:
        # this doesn't stop for now
        print("sleep for 0.5 seconds...")
        time.sleep(0.5)
        if sensors_api.detect():
            print("detection found! sending text message and email via twilio!!")
            twilio_api.send_text_message(phone_number_from, phone_number_to, "this is a sample message!!!")
        else:
            print("didn't detect anything...")

def main(low_power_execution: bool):
    # instantiate sensors
    
    # these are the numbered pins on the RPi
    board_pin_pir_1 = 31
    board_pin_pir_2 = 33
    board_pin_microphone = 37
    
    # this is the GPIO pin, not the numbered pin on RPi
    gpio_pin_dht11 = 17
    
    sensors_api = Sensors(board_pin_pir_1, board_pin_pir_2, board_pin_microphone, gpio_pin_dht11)

    # keys.txt should be a text file that is created locally and contains the twilio account sid, access key, a from number, and a to number.
    keys = open("keys.txt").readline().split(",")
    account_sid = keys[0]
    auth_token = keys[1]
    phone_number_from = keys[2]
    phone_number_to = keys[3]
    twilio_api = Twilio(account_sid, auth_token)

    if low_power_execution:
        _low_powered_implementation(sensors_api, twilio_api, phone_number_from, phone_number_to)
    else:
        _high_powered_implementation(sensors_api, twilio_api, phone_number_from, phone_number_to)

if __name__ == "__main__":    
    low_power_execution = False
    if len(sys.argv) > 1 and (sys.argv[1] == "low_power" or sys.argv[1] == "lp"):
        low_power_execution = True
    main(low_power_execution)
